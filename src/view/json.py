from util import json_file_to_dict, sanitize_data
from controller import InferenceEngine
import logging

from view.web import LOG_LEVEL
LOG_LEVEL = logging.ERROR


class JsonView():
    def __init__(self, file_path: str, log_level=LOG_LEVEL) -> None:
        self.file_path = file_path
        self.engine = InferenceEngine(log_level=log_level)
        self.result = False

    def process_file(self):
        raw_data = json_file_to_dict(self.file_path)
        data = sanitize_data(raw_data)
        self.engine.infer(data)
        self.result = self.engine.check_result()
        self.engine.reset()

    def print_result(self):
        if self.result:
            print("Pinjaman Diterima")
        else:
            print("Pinjaman Tidak Diterima")
