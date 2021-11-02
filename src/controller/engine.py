from clips import *
from model import load_clp
from util import count_loan_duration, parse_single_facts
import logging
from colorlog import ColoredFormatter
import json


class InferenceEngine():
    def __init__(self, log_level=0) -> None:
        # Setup logging facilitator
        self.log_level = log_level
        LOGFORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
        logging.root.setLevel(self.log_level)
        formatter = ColoredFormatter(LOGFORMAT)
        stream = logging.StreamHandler()
        stream.setLevel(self.log_level)
        stream.setFormatter(formatter)
        log = logging.getLogger('pythonConfig')
        log.setLevel(self.log_level)
        log.addHandler(stream)
        self.logger = log
        # Setup CLIPS Environment
        log.info("Initiating Inference Engine....")
        self.env = Environment()
        for clp in load_clp():
            self.env.build(clp)
        self.result_facts = {}

        # debugging
        log.debug("Printing Loaded Rules....")
        for rule in self.env._agenda.rules():
            log.debug(rule)
        log.debug("Printing Loaded Templates...")
        for template in self.env._facts.templates():
            log.debug(template)

    def reset(self):
        self.logger.info("Resetting CLIPS state.....")
        self.env.reset()
        self.result_facts = {}

    def check_result(self) -> bool:
        return ('loan_accepted' in self.result_facts)

    def infer(self, data: dict):
        self.logger.debug("Printing Sanitized data...")
        self.logger.debug(data)
        # input data with templates
        prereq_template = self.env._facts.find_template('prerequisite')
        prereq_facts = prereq_template.assert_fact(
            has_ktp=data['has_ktp'],
            is_wni=data['is_wni'],
            is_domisili_indo=data['is_domisili_indo'],
            is_age_over_21=data['is_age_over_21']
        )

        job_template = self.env._facts.find_template('job_related')
        job_facts = job_template.assert_fact(
            has_steady_job=data['has_steady_job'],
            has_steady_income=data['has_steady_income'],
            has_monthly_income=data['has_monthly_income'],
            has_personal_bank_account=data['has_personal_bank_account']
        )

        income_template = self.env._facts.find_template('income_related')
        income_facts = income_template.assert_fact(
            monthly_income=data['monthly_income'],
            monthly_spending=data['monthly_spending']
        )

        # loan duration count with ffunction from util
        loan_duration = count_loan_duration(
            loan_amount=data['loan_amount'],
            income=data['monthly_income'],
            spending=data['monthly_spending']
        )
        self.logger.debug("Printing Loan Duration....")
        self.logger.debug(f"Duration: {loan_duration}")

        loan_template = self.env._facts.find_template('loan_related')
        loan_facts = loan_template.assert_fact(
            duration=loan_duration,
            suggested_duration=data['suggested_duration']
        )

        guarantee_template = self.env._facts.find_template('guarantee_related')
        guarantee_facts = guarantee_template.assert_fact(
            has_valuable_asset=data['has_valuable_asset'],
            has_reachable_relative=data['has_reachable_relative']
        )

        comply_template = self.env._facts.find_template('comply_related')
        comply_fact = comply_template.assert_fact(
            is_comply_with_payment_terms=data['is_comply_with_payment_terms'],
            is_comply_with_service_terms=data['is_comply_with_service_terms']
        )

        self.env._agenda.run(200)
        self.logger.debug("Printing Activated Rules")
        for rule in self.env._agenda.activations():
            self.logger.debug(rule)

        implied_facts = []
        self.logger.debug("Printing Implied Facts.....")
        for fact in self.env._facts.facts():
            if isinstance(fact, ImpliedFact):
                self.logger.debug(fact)
                implied_facts.append(str(fact))

        result_facts = parse_single_facts(implied_facts)
        self.logger.debug("Printing Result Facts Dicitonary......")
        self.logger.debug(result_facts)

        self.result_facts = result_facts
