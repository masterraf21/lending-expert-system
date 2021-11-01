;;; #######################
;;; DEFTEMPLATES & DEFFACTS
;;; #######################

;;; Loan information
(deftemplate loan
    (slot (amount) (type FLOAT))
)

;;; Borrower information
(deftemplate borrower
   (slot name) 
   (slot is_age_over_21) 
   (slot is_ktp)
   (slot is_wni)
   (slot is_domisili_indo)
   (slot is_employed)
   (slot is_comply)

)
