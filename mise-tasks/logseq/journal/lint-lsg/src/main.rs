//! Lint the change log at the end of each journal page, as [[Logseq/Journal]] describes it.
//!
//! Rule: a page appears under only one of [[Filed]] and [[Updated]] on the same day.
//! Names are compared through Logseq Gardener's page catalog, so a title and its alias
//! count as one page.

use std::collections::BTreeMap;
use std::path::{Path, PathBuf};
use std::process::ExitCode;

use logseq_gardener_sdk::ast::{Block, Inline, Projection, Url};
use logseq_gardener_sdk::garden::{DocumentKind, load_garden};
use logseq_gardener_sdk::garden_settings::GardenSettings;
use logseq_gardener_sdk::inline_references::tag_page_name;
use logseq_gardener_sdk::journals::JournalFormats;
use logseq_gardener_sdk::outline::Outline;
use logseq_gardener_sdk::page_lookup::PageCatalog;
use logseq_gardener_sdk::page_names::lookup_key;
use logseq_gardener_sdk::page_titles::FilenameFormat;

const USAGE: &str = "usage: journal-lint --graph PATH [JOURNAL.md ...]";

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum Section {
    Filed,
    Updated,
}

/// A page listed under both sections of one journal, with the first line of each listing.
#[derive(Debug, PartialEq, Eq)]
struct Finding {
    name: String,
    filed_line: usize,
    updated_line: usize,
}

/// Page names a run of inline syntax links to, including tags.
fn page_refs(nodes: &[Inline], out: &mut Vec<String>) {
    for node in nodes {
        match node {
            Inline::Link {
                url: Url::PageRef { v },
                ..
            } => out.push(v.clone()),
            Inline::Link { label, .. } => page_refs(label, out),
            Inline::Tag { children, .. } => out.push(tag_page_name(children)),
            Inline::Emphasis { children, .. }
            | Inline::Subscript { children, .. }
            | Inline::Superscript { children, .. } => page_refs(children, out),
            _ => {}
        }
    }
}

/// Page names in a bullet's own text: its first line and any paragraphs before the next bullet.
fn bullet_refs(blocks: &[Block], index: usize) -> Vec<String> {
    let mut out = Vec::new();
    if let Block::Bullet { inline, .. } = &blocks[index] {
        page_refs(inline, &mut out);
    }
    for block in &blocks[index + 1..] {
        match block {
            Block::Bullet { .. } => break,
            Block::Paragraph { inline, .. } => page_refs(inline, &mut out),
            _ => {}
        }
    }
    out
}

fn section_of(refs: &[String]) -> Option<Section> {
    match refs {
        [only] if lookup_key(only) == "filed" => Some(Section::Filed),
        [only] if lookup_key(only) == "updated" => Some(Section::Updated),
        _ => None,
    }
}

fn line_of(source: &str, byte: usize) -> usize {
    source[..byte.min(source.len())].matches('\n').count() + 1
}

/// Pages listed under both [[Filed]] and [[Updated]]. `identity` maps an authored
/// name to the page it reaches, so different spellings of one page compare equal.
fn findings(source: &str, parsed: &Projection, identity: &dyn Fn(&str) -> String) -> Vec<Finding> {
    let outline = Outline::from_blocks(&parsed.blocks);
    // identity -> (name as first written, first Filed line, first Updated line)
    let mut seen: BTreeMap<String, (String, Option<usize>, Option<usize>)> = BTreeMap::new();
    let mut section = None;
    for block in &outline.blocks {
        let refs = bullet_refs(&parsed.blocks, block.index);
        if block.depth == 1 {
            section = section_of(&refs);
            continue;
        }
        let Some(current) = section else { continue };
        let line = line_of(source, block.start.unwrap_or(0));
        for name in refs {
            let entry = seen
                .entry(identity(&name))
                .or_insert_with(|| (name.clone(), None, None));
            let slot = match current {
                Section::Filed => &mut entry.1,
                Section::Updated => &mut entry.2,
            };
            slot.get_or_insert(line);
        }
    }
    let mut found: Vec<Finding> = seen
        .into_values()
        .filter_map(|(name, filed, updated)| {
            Some(Finding {
                name,
                filed_line: filed?,
                updated_line: updated?,
            })
        })
        .collect();
    found.sort_by_key(|f| f.updated_line);
    found
}

struct Args {
    graph: PathBuf,
    journals: Vec<PathBuf>,
}

fn parse_args() -> Result<Args, String> {
    let mut graph = None;
    let mut journals = Vec::new();
    let mut args = std::env::args().skip(1);
    while let Some(arg) = args.next() {
        match arg.as_str() {
            "--graph" => graph = Some(PathBuf::from(args.next().ok_or(USAGE)?)),
            "-h" | "--help" => return Err(USAGE.to_owned()),
            "--" => {}
            _ => journals.push(PathBuf::from(arg)),
        }
    }
    Ok(Args {
        graph: graph.ok_or(USAGE)?,
        journals,
    })
}

/// A journal argument as a path relative to the garden root.
fn relative(graph: &Path, journal: &Path) -> PathBuf {
    let journal = journal.strip_prefix("./").unwrap_or(journal);
    match (journal.canonicalize(), graph.canonicalize()) {
        (Ok(full), Ok(root)) if journal.is_absolute() => full
            .strip_prefix(&root)
            .map(Path::to_path_buf)
            .unwrap_or(full),
        _ => journal.to_path_buf(),
    }
}

fn main() -> ExitCode {
    let args = match parse_args() {
        Ok(args) => args,
        Err(message) => {
            eprintln!("{message}");
            return ExitCode::from(2);
        }
    };
    let garden = match load_garden(&args.graph) {
        Ok(garden) => garden,
        Err(error) => {
            eprintln!("error: {error}");
            return ExitCode::from(2);
        }
    };
    let (settings, _) = GardenSettings::read(&args.graph);
    let formats = JournalFormats::from_settings(&settings);
    let (catalog, _) = PageCatalog::build(&garden, FilenameFormat::TripleLowbar, &formats);
    let identity = |name: &str| match catalog.find(name).as_slice() {
        [page] => page.relative_path.display().to_string(),
        _ => format!("unresolved:{}", lookup_key(name)),
    };

    let wanted: Vec<PathBuf> = args
        .journals
        .iter()
        .map(|j| relative(&args.graph, j))
        .collect();
    let journals: Vec<_> = garden
        .documents
        .iter()
        .filter(|d| d.kind == DocumentKind::Journal)
        .filter(|d| wanted.is_empty() || wanted.contains(&d.relative_path))
        .collect();
    for path in &wanted {
        if !journals.iter().any(|d| &d.relative_path == path) {
            eprintln!("error: not a journal in this garden: {}", path.display());
            return ExitCode::from(2);
        }
    }

    let mut count = 0;
    for document in journals {
        for finding in findings(&document.source, &document.parsed, &identity) {
            count += 1;
            println!(
                "{}:{}: [[{}]] is under both [[Filed]] (line {}) and [[Updated]] (line {})",
                document.relative_path.display(),
                finding.updated_line,
                finding.name,
                finding.filed_line,
                finding.updated_line,
            );
        }
    }
    if count > 0 {
        ExitCode::from(1)
    } else {
        ExitCode::SUCCESS
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use logseq_gardener_sdk::garden::parse_document;

    fn check(source: &str) -> Vec<Finding> {
        findings(source, &parse_document(source), &|name: &str| {
            lookup_key(name)
        })
    }

    #[test]
    fn a_page_under_both_sections_is_reported() {
        let source = "- # [[Filed]]\n\t- music\n\t\t- [[A]]\n\t\t- [[B]]\n- # [[Updated]]\n\t- [[b]]\n\t- [[C]]\n";
        assert_eq!(
            check(source),
            vec![Finding {
                name: "B".into(),
                filed_line: 4,
                updated_line: 6
            }]
        );
    }

    #[test]
    fn separate_pages_pass() {
        let source = "- # [[Filed]]\n\t- [[A]]\n- # [[Updated]]\n\t- [[C]]\n";
        assert!(check(source).is_empty());
    }

    #[test]
    fn links_above_the_change_log_do_not_count() {
        let source =
            "- Wrote about [[A]] today\n- # [[Filed]]\n\t- [[B]]\n- # [[Updated]]\n\t- [[A]]\n";
        assert!(check(source).is_empty());
    }

    #[test]
    fn an_unbulleted_first_heading_still_starts_a_section() {
        let source = "# [[Filed]]\n\t- [[A]]\n- # [[Updated]]\n\t- [[A]]\n";
        assert_eq!(check(source).len(), 1);
    }
}
