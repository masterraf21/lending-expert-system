;;; #######################
;;; DEFRULES
;;; #######################

(defrule is_prerequisite_passed
    ()
    =>
    (assert (prerequisite_result TRUE))
)

(defrule is_job_related_passed
    ()
    =>
    (assert (job_related_result TRUE))
)

(defrule is_guarantee_related_passed
    ()
    =>
    (assert (guarantee_related_result TRUE))
)

(defrule is_comply_related_passed
    ()
    =>
    (assert (comply_related_result TRUE))
)

(defrule is_duration_passed
    ()
    =>
    (assert (duration_result TRUE))
)