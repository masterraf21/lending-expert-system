from clips import *


class InferenceEngine():
    def __init__(self, clp_files=[]) -> None:
        self.env = Environment()
        for clp_file in clp_files:
            self.env.load(clp_file)

    def init_agent(self):
        pass

    def run(self):
        pass

    def reset(self):
        self.env.reset()

    def eval(self):
        self.env.eval()

    def process_data(self, data: dict):
        pass
