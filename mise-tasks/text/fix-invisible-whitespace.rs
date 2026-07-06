// Normalize invisible paste-artifact characters in UTF-8 text files.
//
// These characters are near-always accidental in this Markdown garden (they slip
// in from copy-pasting rich text) and cause subtle bugs: an editor search for a
// normal space misses a no-break space, so a line looks impossible to match.
//
// Pure std, no crates. Compiled to a cached binary by the `text:fix-invisible`
// mise task. Usage: `fix-invisible-whitespace [--check] FILE...`
//   default : rewrite each file in place, replacing the characters below
//   --check : report offending files and exit non-zero; change nothing
//
// Files that are not valid UTF-8 (e.g. images and PDFs under assets/) are skipped.

use std::env;
use std::fs;
use std::process::ExitCode;

// (character, replacement). Empty replacement means the character is removed.
const REPLACEMENTS: &[(char, &str)] = &[
    ('\u{00A0}', " "), // no-break space -> regular space
    ('\u{202F}', " "), // narrow no-break space -> regular space
    ('\u{200B}', ""),  // zero-width space -> removed
    ('\u{FEFF}', ""),  // byte-order mark / zero-width no-break space -> removed
];

fn normalize(content: &str) -> (String, usize) {
    let mut out = String::with_capacity(content.len());
    let mut count = 0usize;
    for ch in content.chars() {
        match REPLACEMENTS.iter().find(|(c, _)| *c == ch) {
            Some((_, replacement)) => {
                out.push_str(replacement);
                count += 1;
            }
            None => out.push(ch),
        }
    }
    (out, count)
}

fn main() -> ExitCode {
    let mut check = false;
    let mut files: Vec<String> = Vec::new();
    for arg in env::args().skip(1) {
        match arg.as_str() {
            "--check" => check = true,
            "--" => {} // argument separator, ignore
            _ => files.push(arg),
        }
    }

    let mut fixed_files = 0usize;
    let mut fixed_chars = 0usize;
    let mut had_error = false;

    for path in &files {
        let bytes = match fs::read(path) {
            Ok(b) => b,
            Err(err) => {
                eprintln!("skip {path}: {err}");
                continue;
            }
        };
        let content = match String::from_utf8(bytes) {
            Ok(text) => text,
            Err(_) => continue, // not UTF-8: binary asset, leave untouched
        };
        let (normalized, count) = normalize(&content);
        if count == 0 {
            continue;
        }
        fixed_files += 1;
        fixed_chars += count;
        if check {
            println!("{path}: {count} invisible character(s)");
        } else if let Err(err) = fs::write(path, &normalized) {
            eprintln!("write {path}: {err}");
            had_error = true;
        } else {
            println!("fixed {path}: {count} invisible character(s)");
        }
    }

    if check && fixed_files > 0 {
        eprintln!(
            "{fixed_chars} invisible character(s) in {fixed_files} file(s); run `mise run text:fix-invisible` to normalize"
        );
        return ExitCode::FAILURE;
    }
    if had_error {
        return ExitCode::FAILURE;
    }
    ExitCode::SUCCESS
}
