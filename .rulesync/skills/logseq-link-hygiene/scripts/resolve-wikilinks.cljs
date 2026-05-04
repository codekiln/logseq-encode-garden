(ns resolve-wikilinks
  (:require ["fs" :as fs]
            ["path" :as path]
            ["process" :as process]
            [clojure.string :as str]))

(defn exists? [p]
  (.existsSync fs p))

(defn read-file [p]
  (.readFileSync fs p "utf8"))

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
  (try
    (js/decodeURIComponent s)
    (catch :default _ s)))

(defn file->title [p]
  (-> p
      (str/replace #"^pages/" "")
      (str/replace #"\.md$" "")
      (str/replace #"___" "/")
      safe-decode))

(defn normalize [s]
  (-> s
      str/lower-case
      (str/replace #"[^a-z0-9]+" "")
      str/trim))

(defn date-link? [s]
  (boolean (re-matches #"\d{4}/\d{2}/\d{2}" s)))

(defn bracket-links [s]
  (map second (re-seq #"\[\[([^\]]+)\]\]" s)))

(defn alias-values [line]
  (when (str/starts-with? line "alias::")
    (let [raw (str/trim (subs line (count "alias::")))]
      (if (str/includes? raw "[[")
        (bracket-links raw)
        (map str/trim (str/split raw #","))))))

(defn aliases-for-file [p]
  (->> (str/split-lines (read-file p))
       (take-while #(not (str/starts-with? % "- ")))
       (mapcat #(or (alias-values %) []))
       (remove str/blank?)))

(defn page-index []
  (let [files (walk-md "pages")]
    (reduce
     (fn [idx p]
       (let [title (file->title p)
             aliases (aliases-for-file p)]
         (-> idx
             (update :titles assoc title title)
             (update :normalized update (normalize title) (fnil conj #{}) title)
             (update :aliases into (map (fn [a] [a title]) aliases))
             (update :normalized
                     (fn [m]
                       (reduce
                        (fn [acc a] (update acc (normalize a) (fnil conj #{}) title))
                        m aliases))))))
     {:titles {} :aliases {} :normalized {}}
     files)))

(defn classify [idx link]
  (let [titles (:titles idx)
        aliases (:aliases idx)
        normalized (:normalized idx)
        norm-candidates (get normalized (normalize link))]
    (cond
      (date-link? link)
      {:status "date-link" :canonical link :candidates [link]}

      (contains? titles link)
      {:status "canonical" :canonical link :candidates [link]}

      (contains? aliases link)
      {:status "alias-match" :canonical (get aliases link) :candidates [(get aliases link)]}

      (= 1 (count norm-candidates))
      {:status "normalized-match" :canonical (first norm-candidates) :candidates (vec norm-candidates)}

      (> (count norm-candidates) 1)
      {:status "ambiguous" :canonical nil :candidates (vec norm-candidates)}

      :else
      {:status "unresolved" :canonical nil :candidates []})))

(defn changed-files [args]
  (let [idx (.indexOf args "--changed")]
    (if (neg? idx)
      []
      (drop (inc idx) args))))

(defn emit [m]
  (js/console.log (js/JSON.stringify (clj->js m))))

(defn -main []
  (let [args (vec (seq (.-argv process)))
        files (changed-files (drop 2 args))
        idx (page-index)]
    (doseq [file files
            :when (exists? file)
            link (distinct (bracket-links (read-file file)))]
      (emit (merge {:file file :link link} (classify idx link))))))

(-main)
