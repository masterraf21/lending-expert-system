;;; #######################
;;; DEFTEMPLATES & DEFFACTS
;;; #######################

;;; Loan information
(deftemplate loan
    (slot amount (type FLOAT))
    (slot duration (type INTEGER))
)

;;; Borrower information
(deftemplate borrower
    (slot name (type STRING)) 
    ;; prerequisite facts
    (slot has_ktp (type SYMBOL))
    (slot is_wni (type SYMBOL))
    (slot is_domisili_indo (type SYMBOL))
    (slot is_age_over_21 (type SYMBOL))
    ;; more advanced facts
    (slot has_steady_job (type SYMBOL))
    (slot has_steady_income (type SYMBOL))
    (slot has_monthly_income (type SYMBOL))
    (slot has_personal_bank_account (type SYMBOL))
    ;; loan related facts
    (slot monthly_allowance (type FLOAT))
    (slot monthly_spending (type FLOAT))
    (slot suggested_loan_duration (type INTEGER))
    ;; risk related facts
    (slot has_valuable_asset (type SYMBOl))
    (slot has_reachable_relative (type SYMBOL))
    ;; terms and conditions facts
    (slot is_comply_with_payment_terms (type SYMBOL))
    (slot is_comply_with_service_terms (type SYMBOL))
)
