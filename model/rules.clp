;;; #######################
;;; RULES
;;; #######################

(defrule is_ktp_exist
    (borrower[is_ktp] TRUE)
    =>
    (LANJUT KE RULE SELANJUTNYA)
)

;;; if loan/bulan < pengeluaran/bulan =? terima
;;; 