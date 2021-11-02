from controller import InferenceEngine
from util import prompt_question, sanitize_data
import logging

yn = "y/n"
acc = ["y", "n"]


class CLIView():
    def __init__(self) -> None:
        self.engine = InferenceEngine(log_level=logging.ERROR)
        self.clean_data = {}
        self.result = False

    def process_data(self):
        self.get_data()
        self.engine.infer(self.clean_data)
        self.result = self.engine.check_result()
        self.engine.reset()

    def print_result(self):
        print("\n")
        if self.result:
            print("Pinjaman Diterima")
        else:
            print("Pinjaman Tidak Diterima")

    def get_data(self):
        input_data = {}

        amount = prompt_question(
            question="Berapa uang yang ingin anda pinjam",
            type="float",
            example_answer="20000"
        )
        input_data["loan_amount"] = amount

        suggested_duration = prompt_question(
            question="Berapa lama anda akan berencana mengembalikan",
            type="int",
            example_answer="6"
        )
        input_data["suggested_duration"] = suggested_duration

        age_over_21 = prompt_question(
            question="Apakah anda berumur diatas 21",
            accepted_anwers=acc,
            example_answer=yn
        )
        input_data["is_age_over_21"] = age_over_21

        has_ktp = prompt_question(
            question="Apakah anda mempunyai KTP",
            accepted_anwers=acc,
            example_answer=yn
        )
        input_data["has_ktp"] = has_ktp

        is_wni = prompt_question(
            question="Apakah anda berstatus WNI",
            accepted_anwers=acc,
            example_answer=yn
        )
        input_data["is_wni"] = is_wni

        domisili_indo = prompt_question(
            question="Apakah anda berdomisili di Indonesia",
            accepted_anwers=acc,
            example_answer=yn
        )
        input_data["is_domisili_indo"] = domisili_indo

        steady_job = prompt_question(
            question="Apakah anda memiliki pekerjaan tetap",
            accepted_anwers=acc,
            example_answer=yn
        )
        input_data["has_steady_job"] = steady_job

        steady_income = prompt_question(
            question="Apakah anda memiliki pendapatan tetap",
            accepted_anwers=acc,
            example_answer=yn
        )
        input_data["has_steady_income"] = steady_income

        monthly_income = prompt_question(
            question="Apakah anda memiliki pendapatan bulanan",
            accepted_anwers=acc,
            example_answer=yn
        )
        input_data["has_monthly_income"] = monthly_income

        personal_bank = prompt_question(
            question="Apakah anda memiliki rekening bank pribadi",
            accepted_anwers=acc,
            example_answer=yn
        )
        input_data["has_personal_bank_account"] = personal_bank

        monthly_income_amount = prompt_question(
            question="Berapa pendapatan bulanan anda",
            type="float",
            example_answer="5000000"
        )
        input_data["monthly_income"] = monthly_income_amount

        monthly_spending_amount = prompt_question(
            question="Berapa pengeluaran bulanan anda",
            type="float",
            example_answer="100000"
        )
        input_data["monthly_spending"] = monthly_spending_amount

        valuable_asset = prompt_question(
            question="Apakah anda punya aset berharga sebagai jaminan",
            accepted_anwers=acc,
            example_answer=yn
        )
        input_data["has_valuable_asset"] = valuable_asset

        reachable_relative = prompt_question(
            question="Apakah anda memiliki kerabat yang bisa dihubungi",
            accepted_anwers=acc,
            example_answer=yn
        )
        input_data["has_reachable_relative"] = reachable_relative

        payment_terms = prompt_question(
            question="Apakah bersedia memenuhi ketentuan syarat pembayaran dan jaminan",
            accepted_anwers=acc,
            example_answer=yn
        )
        input_data['is_comply_with_payment_terms'] = payment_terms

        service_terms = prompt_question(
            question="Apakah bersedia dengan ketentuan dan syarat layanan",
            accepted_anwers=acc,
            example_answer=yn
        )
        input_data['is_comply_with_service_terms'] = service_terms

        self.clean_data = sanitize_data(input_data)
