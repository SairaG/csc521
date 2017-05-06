;instparser
(ns clojure.core (:require [instaparse.core :as insta])(:require [clojure.java.io :as io]))

(def parse
  (insta/parser
  (slurp(clojure.java.io/resource "quirk.txt")) :auto-whitespace :standard)
  )
(println (parse "print 1 + 4 -3"))



;Interpreter
(ns clojure.core
  (:gen-class)
  (:require [instaparse.core :as insta]))

(defn third [aList] (nth aList 2))
(defn fourth [aList] (nth aList 3))

(defn 0 [aList] (nth aList 0))

(0 subtree)

(defn CallByLabel (first (second subtree)) (second subtree) scope)
   (println "Call by label done")
  )


    (CallByLabel (stSecond subtree) (second subtree) scope)
(defn stFirst [subtree] (first (first subtree)))
(defn stSecond [subtree] (second (first subtree)))


(defn Expression [subtree scope]
	(println "Expression")
	(println first( second subtree))

	(cond
   (= 2 (count subtree))
   (CallByLabel (first (second subtree)) (second subtree) scope)
   (= :Term (first (second subtree)))
		((if (.equals :ADD (first (third subtree)))
			(+ (CallByLabel (first (second subtree))(second subtree) scope)
			(CallByLabel (first (fourth subtree))(fourth subtree) scope)))
		(if (.equals :SUB (first (third subtree)))
			(- (CallByLabel (first (second subtree))(second subtree) scope)
			(CallByLabel (first (fourth subtree))(fourth subtree) scope))))

      :else
      		(CallByLabel (first (second subtree)) (second subtree) scope))
)


(def VarBindLoop [paramList valueList]
  (if (= 1 (count paramList))
    (assoc {} (first paramList)  (fist valueList))
    (merge (assoc {} (first paramList)  (first valueList))
      (VarBindLoop
        (rest paramList)
        (rest valueList)
        )

      )
   )
 )


(defn Program [subtree scope]
 (println "PROGRAM")

 (cond
   (= :Program (first (third subtree)))
   ((CallByLabel (first (second subtree)) (second subtree) scope)
     (CallByLabel (first (third subtree)) (third subtree) scope))
   :else
   (CallByLabel (first (second subtree)) (second subtree) scope)
  )
 )

(defn Statement [subtree scope]
 (println "STATEMENT")
 (defn Assignment [subtree scope]
	(println "Done Assignment")

	(cond ( = :SingleAssignment (first (second subtree)))
		(def newScope (CallByLabel (first (second subtree))(second subtree) scope)
	 ( = :MultipleAssignment (first (second subtree)))
		(CallByLabel (first (second subtree))(second subtree) scope))
)
(defn SingleAssignment [subtree scope]
	(println "Single Assignment Done")

	(def newScope (assoc scope (second (CallByLabel (first (third subtree))(third subtree) scope))
					(CallByLabel (first (fifth subtree))(fifth subtree) scope)))

))

(defn interpret-quirk [subtree scope] (CallByLabel (first subtree) subtree {}))
  (ns.clojure.core
    (require [clojure.core :as insta]))


(defn -main [& args]
  ;(println (first *command-line-args*))
  (if (.equals "-pt" (first *command-line-args*))
    (def SHOW_PARSE_TREE true)
  )
  (def quirk-parser (insta/parser (slurp "resources/quirk-grammar-ebnf") :auto-whitespace :standard))
  (def parse-tree (quirk-parser "function foo (x, y) { return 3 + 4 + 2 / x ^ y} print foo(12, 12)"))
  (if (= true SHOW_PARSE_TREE)
    (println parse-tree)
    (interpret-quirk parse-tree {}))
  (println "done!")
 )

(-main)
