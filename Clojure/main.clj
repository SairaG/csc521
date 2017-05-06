(defn -main [& args]
  (def quirk (project (clojure.java.io/resource "EBNFgrammer") :auto-whitespace :standard))
  (def quirkParseTree (quirk (slurp *in*)))
   
  (if (.equals "-pt" (first *command-line-args*))
    (def SHOW_PARSE_TREE true))
  (if (= true SHOW_PARSE_TREE)
    (pprint quirkParseTree)
    (interpretQuirk quirkParseTree)))
