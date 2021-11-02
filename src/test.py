import unittest
import os
import logging
from util import sanitize_data
from controller import InferenceEngine


class TestEngine(unittest.TestCase):
    def test_engine_with_dummy(self):
        dummy_data = {
            'has_ktp': 'y',
            'is_wni': 'y',
            'is_domisili_indo': 'y',
            'is_age_over_21': 'y',
            'has_steady_job': 'y',
            'has_steady_income': 'y',
            'has_monthly_income': 'y',
            'has_personal_bank_account': 'y',
            'monthly_income': 20000000,
            'monthly_spending': 10000000,
            'suggested_duration': 9,
            'loan_amount': 3000000,
            'has_valuable_asset': 'y',
            'has_reachable_relative': 'y',
            'is_comply_with_payment_terms': 'y',
            'is_comply_with_service_terms': 'y'
        }
        data = sanitize_data(dummy_data)

        engine = InferenceEngine(log_level=logging.INFO)
        engine.infer(data)
        result = engine.check_result()
        engine.reset()

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
