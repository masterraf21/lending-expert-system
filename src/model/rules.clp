;;; #######################
;;; RULES
;;; #######################


(defrule is_prerequisite_passed
    (prerequisite   (has_ktp TRUE) (is_wni TRUE) 
                    (is_domisili_indo TRUE) (is_age_over_21 TRUE))
    =>
    (assert (prerequisite_passed TRUE))
)

(defrule is_job_related_passed
    (job_related    (has_steady_job TRUE) (has_steady_income TRUE)
                    (has_monthly_income TRUE) (has_personal_bank_account TRUE)
    )
    =>
    (assert (job_related_passed TRUE))
)

(defrule is_guarantee_related_passed
    (guarantee_related  (has_valuable_asset TRUE) 
                        (has_reachable_relative TRUE)
    )
    =>
    (assert (guarantee_related_passed TRUE))
)

(defrule is_comply_related_passed
    (comply_related     (is_comply_with_payment_terms TRUE)
                        (is_comply_with_service_terms TRUE)
    )
    =>
    (assert (comply_related_passed TRUE))
)

(defrule is_duration_passed
    (loan_related (duration ?dur) (suggested_duration ?s_dur))
    (test (and (<= ?dur 12) (and (< ?s_dur 12) (>= ?s_dur ?dur))))
    =>
    (assert (duration_passed TRUE))
)

(defrule is_loan_accepted
    (prerequisite_passed TRUE)
    (job_related_passed TRUE)
    (guarantee_related_passed TRUE)
    (comply_related_passed TRUE)
    (duration_passed TRUE)
    =>
    (assert (loan_accepted TRUE))
)
