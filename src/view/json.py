from util import json_file_to_dict, sanitize_data
from controller import InferenceEngine
import logging


class JsonView():
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.engine = InferenceEngine(log_level=logging.ERROR)

    def print_data(self):
        raw_data = json_file_to_dict(self.file_path)
        data = sanitize_data(raw_data)
        print(data)

    def process_file(self):
        raw_data = json_file_to_dict(self.file_path)
        data = sanitize_data(raw_data)
        self.engine.infer(data)
        result = self.engine.check_result()
        self.engine.reset()
        self.result = result

    def print_result(self):
        if self.result:
            print("Loan Accepted")
        else:
            print("Loan Not Accepted")
