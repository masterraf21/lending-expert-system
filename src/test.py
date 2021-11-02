import unittest
import os
import logging
from controller import InferenceEngine


class TestEngine(unittest.TestCase):
    def test_init(self):
        engine = InferenceEngine(log_level=logging.DEBUG)

        self.assertIsNotNone(engine)


if __name__ == '__main__':
    unittest.main()
