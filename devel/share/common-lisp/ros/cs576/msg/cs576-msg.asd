
(cl:in-package :asdf)

(defsystem "cs576-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "FloatArray" :depends-on ("_package_FloatArray"))
    (:file "_package_FloatArray" :depends-on ("_package"))
  ))