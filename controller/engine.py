from clips import *


class InferenceEngine():
    def __init__(self, clp_files=[]) -> None:
        self.env = Environment()
        for clp_file in clp_files:
            self.env.load(clp_file)

    def init_agent(self):
        pass

    def reset(self):
        pass
