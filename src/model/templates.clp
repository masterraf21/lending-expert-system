;;; #######################
;;; DEFTEMPLATES & DEFFACTS
;;; #######################

;;; Prerequisite facts
(deftemplate prerequisite
    (slot has_ktp)
    (slot is_wni)
    (slot is_domisili_indo)
    (slot is_age_over_21)
)

;;; Job related facts
(deftemplate job_related
    (slot has_steady_job)
    (slot has_steady_income)
    (slot has_monthly_income)
    (slot has_personal_bank_account)
)

;; Income related facts
(deftemplate income_related
    (slot monthly_income (type FLOAT))
    (slot monthly_spending (type FLOAT))
)

;;; Income related facts
(deftemplate loan_related
    (slot loan_amount (type FLOAT))
    (slot loan_duration (type INTEGER))
    (slot suggested_loan_duration (type INTEGER))
)

;;; Guarantee related facts
(deftemplate guarantee_related
    (slot has_valuable_asset)
    (slot has_reachable_relative)
)

;;; Compliance related facts
(deftemplate comply_related
    (slot is_comply_with_payment_terms)
    (slot is_comply_with_service_terms)
)