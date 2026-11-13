logseq-entity:: [[Logseq/Entity/Podcast]]

- # Ghost in the Patch - Alpha podcast
	- GitHub repo: [[Person/codekiln/GitHub/gitpa]]
	- Web Address: https://codekiln.github.io/gitpa
	- RSS address: TBD
	- query-table:: false
	  query-properties:: [:page]
	  #+BEGIN_QUERY
	  {:title [:h2 "Episodes"]
	   :query [:find (pull ?p [*])
	           :where
	           [?p :block/name]
	           [?p :block/properties ?props]
	           [(get ?props :logseq-entity) ?entities]
	           [(contains? ?entities "Logseq/Entity/Podcast/Episode")]
	           [(get ?props :public) ?public]
	           [(= ?public true)]]
	   :result-transform (fn [rows] (sort-by :block/name (fn [a b] (compare b a)) rows))
	   :view (fn [rows]
	           (into ["ul"]
	                 (map (fn [row]
	                        ["li" ["a" {:href (str "#/page/" (clojure.string/replace (:block/name row) "/" "%2F"))}
	                               (:block/original-name row)]]) rows)))
	   :table-view? false
	  }
	  #+END_QUERY
