(ns generate-favorite-decks
  "Reconcile the Logseq/Flashcard/Review/Favorite deck pages with the graph's
   :favorites (logseq/config.edn). Run from the graph root via nbb-logseq.

   Idempotent + surgical: existing pages are merged, never overwritten, so the
   review-history children Logseq appends under {{cards}} blocks survive.

   Flags: --write (apply; default dry-run), --prune (delete stale subpages)."
  (:require ["fs" :as fs]
            ["process" :as process]
            ["path" :as path]
            [clojure.string :as str]))

;; ---------------------------------------------------------------------------
;; Constants
;; ---------------------------------------------------------------------------

(def pages-dir "pages")
(def config-path "logseq/config.edn")
(def root-page "Logseq/Flashcard/Review/Favorite")
(def root-file-prefix "Logseq___Flashcard___Review___Favorite")

;; ---------------------------------------------------------------------------
;; Filesystem helpers (shared shape with resolve-wikilinks.cljs)
;; ---------------------------------------------------------------------------

(defn exists? [p] (.existsSync fs p))
(defn read-file [p] (.readFileSync fs p "utf8"))
(defn write-file [p s] (.writeFileSync fs p s "utf8"))

(defn walk-md [dir]
  (if-not (exists? dir)
    []
    (let [entries (.readdirSync fs dir #js {:withFileTypes true})]
      (mapcat
       (fn [entry]
         (let [p (path/join dir (.-name entry))]
           (cond
             (.isDirectory entry) (walk-md p)
             (str/ends-with? p ".md") [p]
             :else [])))
       (seq entries)))))

(defn safe-decode [s]
  (try (js/decodeURIComponent s) (catch :default _ s)))

(defn file->title [p]
  (-> p
      (str/replace #"^pages/" "")
      (str/replace #"\.md$" "")
      (str/replace #"___" "/")
      safe-decode))

(defn title->file [title]
  (str pages-dir "/" (str/replace title "/" "___") ".md"))

(defn normalize [s]
  (-> s str/lower-case (str/replace #"[^a-z0-9]+" "") str/trim))

(defn bracket-links [s]
  (map second (re-seq #"\[\[([^\]]+)\]\]" s)))

;; ---------------------------------------------------------------------------
;; Favorites + canonical casing
;; ---------------------------------------------------------------------------

(defn read-favorites
  "Extract the :favorites vector from config.edn (single-line, plain strings)."
  []
  (let [content (read-file config-path)
        m (re-find #":favorites\s*\[([^\]]*)\]" content)]
    (when m
      (map second (re-seq #"\"([^\"]*)\"" (second m))))))

(defn build-casing-index
  "normalized-link -> {exact-casing -> frequency} across the whole graph,
   so config strings (zoxide, devcontainer) resolve to canonical casing
   (Zoxide, DevContainer) as actually written in links."
  []
  (let [files (concat (walk-md pages-dir) (walk-md "journals"))]
    (reduce
     (fn [idx p]
       (reduce
        (fn [m lk] (update-in m [(normalize lk) lk] (fnil inc 0)))
        idx
        (bracket-links (read-file p))))
     {}
     files)))

(defn canonicalize [casing-idx s]
  (let [cands (get casing-idx (normalize s))]
    (if (seq cands)
      (key (apply max-key val (seq cands)))
      s)))

(defn meta-favorite?
  "Skip self-referential review/meta favorites (e.g. logseq/flashcard/review)."
  [canonical]
  (str/starts-with? (str/lower-case canonical) "logseq/flashcard"))

;; ---------------------------------------------------------------------------
;; {{cards}} expression generation + comparison
;; ---------------------------------------------------------------------------

(defn or-expr [favs]
  (str "(or " (str/join " " (map #(str "[[" % "]]") favs)) ")"))

(defn pos-macro [favs] (str "{{cards " (or-expr favs) " }}"))
(defn neg-macro [favs] (str "{{cards (not " (or-expr favs) ") }}"))
(defn one-macro [fav] (str "{{cards [[" fav "]] }}"))

(defn expr-sig
  "Whitespace/order/case-insensitive signature of a cards expression:
   [negated? #{normalized-links}]. Cosmetic edits Logseq makes never trip it."
  [s]
  [(boolean (re-find #"\(\s*not" s))
   (set (map normalize (bracket-links s)))])

(defn replace-macro [line new-macro]
  (str/replace line #"\{\{cards[\s\S]*?\}\}" new-macro))

;; ---------------------------------------------------------------------------
;; Page templates (used only when a page does not yet exist)
;; ---------------------------------------------------------------------------

(defn subpage-template [fav]
  (str "- # Favorite Flashcards: [[" fav "]]\n"
       "\t- " (one-macro fav) "\n"
       "\t  favorite-deck:: [[" fav "]]\n"))

(defn aggregate-template [decks]
  (str "- # Favorite Flashcards\n"
       "\t- foregrounds flashcard scopes for my [[Logseq/Favorite]]s ([[Logseq/Queries]]).\n"
       "\t- ## All Favorite Flashcards\n"
       "\t\t- " (pos-macro decks) "\n"
       "\t\t  favorite-deck:: aggregate\n"
       "\t- ## Background / Non-Favorite\n"
       "\t  collapsed:: true\n"
       "\t\t- " (neg-macro decks) "\n"
       "\t\t  favorite-deck:: background\n"
       "\t\t  query-properties:: [:block]\n"
       "\t- ## By Favorite\n"
       (str/join "" (map (fn [f] (str "\t\t- [[" root-page "/" f "]]\n")) decks))))

;; ---------------------------------------------------------------------------
;; Surgical merge of existing pages
;; ---------------------------------------------------------------------------

(defn macro-line-idx
  "Index of the {{cards}} line anchored by `favorite-deck:: <anchor>`
   (search upward from the property line)."
  [lines anchor]
  (let [prop (str "favorite-deck:: " anchor)
        prop-idx (first (keep-indexed (fn [i l] (when (= (str/trim l) prop) i)) lines))]
    (when prop-idx
      (loop [j prop-idx]
        (cond
          (neg? j) nil
          (str/includes? (nth lines j) "{{cards") j
          :else (recur (dec j)))))))

(defn rewrite-anchor
  "Refresh the macro on the anchored cards line iff its link-set/negation drifted.
   Returns [lines changed?]."
  [lines anchor desired-macro]
  (if-let [idx (macro-line-idx lines anchor)]
    (let [line (nth lines idx)
          changed? (not= (expr-sig line) (expr-sig desired-macro))]
      [(if changed? (assoc lines idx (replace-macro line desired-macro)) lines) changed?])
    [lines false]))

(defn ensure-by-favorite
  "Append a link for any favorite missing from the `## By Favorite` section.
   Never reorders or removes existing links. Returns [lines changed?]."
  [lines decks]
  (let [hidx (first (keep-indexed (fn [i l] (when (= (str/trim l) "## By Favorite") i)) lines))]
    (if-not hidx
      [lines false]
      (let [indent (re-find #"^\s*" (nth lines hidx))
            link-indent (str indent "\t")
            end (loop [j (inc hidx)]
                  (cond
                    (>= j (count lines)) j
                    (let [t (str/trim (nth lines j))]
                      (or (str/starts-with? t "# ") (str/starts-with? t "## "))) j
                    :else (recur (inc j))))
            existing (set (map normalize (mapcat bracket-links (subvec lines (inc hidx) end))))
            missing (remove #(contains? existing (normalize (str root-page "/" %))) decks)
            new-lines (map #(str link-indent "- [[" root-page "/" % "]]") missing)]
        (if (empty? missing)
          [lines false]
          [(vec (concat (subvec lines 0 end) new-lines (subvec lines end))) true])))))

;; ---------------------------------------------------------------------------
;; Per-target processing
;; ---------------------------------------------------------------------------

(defn join-lines [lines] (str (str/join "\n" lines) "\n"))

(defn process-aggregate [decks write? report]
  (let [file (title->file root-page)]
    (if-not (exists? file)
      (do (when write? (write-file file (aggregate-template decks)))
          (swap! report conj [:create file "aggregate + background + by-favorite"]))
      (let [lines (vec (str/split-lines (read-file file)))
            [lines c1] (rewrite-anchor lines "aggregate" (pos-macro decks))
            [lines c2] (rewrite-anchor lines "background" (neg-macro decks))
            [lines c3] (ensure-by-favorite lines decks)
            changed? (or c1 c2 c3)
            notes (->> [(when c1 "all-deck") (when c2 "background-deck") (when c3 "by-favorite links")]
                       (remove nil?) (str/join ", "))]
        (when (and write? changed?) (write-file file (join-lines lines)))
        (swap! report conj [(if changed? :update :unchanged) file
                            (if changed? notes "in sync")])))))

(defn process-subpage [fav write? report]
  (let [file (title->file (str root-page "/" fav))
        desired (one-macro fav)]
    (if-not (exists? file)
      (do (when write? (write-file file (subpage-template fav)))
          (swap! report conj [:create file (str "deck [[" fav "]]")]))
      (let [lines (vec (str/split-lines (read-file file)))
            idx (or (macro-line-idx lines (str "[[" fav "]]"))
                    (first (keep-indexed (fn [i l] (when (str/includes? l "{{cards") i)) lines)))]
        (if idx
          (let [line (nth lines idx)
                changed? (not= (expr-sig line) (expr-sig desired))
                lines (if changed? (assoc lines idx (replace-macro line desired)) lines)]
            (when (and write? changed?) (write-file file (join-lines lines)))
            (swap! report conj [(if changed? :update :unchanged) file
                                (if changed? "deck expression" "in sync")]))
          (swap! report conj [:skip file "no {{cards}} block found"]))))))

(defn process-stale [decks prune? write? report]
  (let [keep-norm (set (map #(normalize (str root-page "/" %)) decks))]
    (doseq [f (walk-md pages-dir)
            :when (str/starts-with? f (str pages-dir "/" root-file-prefix "___"))
            :when (not (contains? keep-norm (normalize (file->title f))))]
      (if (and prune? write?)
        (do (.unlinkSync fs f) (swap! report conj [:pruned f "favorite removed from config"]))
        (swap! report conj [:stale f "not in config (use --prune to delete)"])))))

;; ---------------------------------------------------------------------------
;; Report + main
;; ---------------------------------------------------------------------------

(defn print-report [report write? prune?]
  (println (str "logseq:flashcard-favorite — "
                (if write? "WRITE" "DRY-RUN (no files changed)")
                (when prune? " +PRUNE")))
  (doseq [[status file note] report]
    (println (str "  [" (name status) "] " file (when note (str " — " note)))))
  (println (str "  summary: " (pr-str (frequencies (map first report))))))

(defn -main []
  (let [args (set (drop 2 (vec (.-argv process))))
        write? (contains? args "--write")
        prune? (contains? args "--prune")
        casing (build-casing-index)
        decks (->> (read-favorites)
                   (map #(canonicalize casing %))
                   (remove meta-favorite?)
                   distinct
                   vec)
        report (atom [])]
    (process-aggregate decks write? report)
    (doseq [f decks] (process-subpage f write? report))
    (process-stale decks prune? write? report)
    (print-report @report write? prune?)
    (when-not write?
      (println "  run again with --write to apply"))))

(-main)
