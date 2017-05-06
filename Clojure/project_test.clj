(def quirk
  (insta/parser (slurp "resources/instaparse")))
(println (quirk "print5"))
(if (.equals "-pt" (first *command-line-args*))
    (def SHOW_PARSE_TREE true)
  )
  
