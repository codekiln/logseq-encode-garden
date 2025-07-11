# `:ref/default-open-blocks-level`
	- ```clojure
	   ;; Configure the default expansion level for linked references.
	   ;; For example, consider the following block hierarchy:
	   ;; - a [[page]] (level 1)
	   ;;   - b        (level 2)
	   ;;     - c      (level 3)
	   ;;       - d    (level 4)
	   ;;
	   ;; With the default value of level 2, block b will be collapsed.
	   ;; If the level's value is set to 3, block c will be collapsed.
	   ;; Default value: 2
	  ```