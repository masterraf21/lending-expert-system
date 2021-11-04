import flask
from controller import InferenceEngine
from util import init_logger
import logging
import json

from util.io import sanitize_data

LOG_LEVEL = logging.ERROR


class WebView():
    def __init__(self, debug: bool = False, log_level=LOG_LEVEL) -> None:
        self.engine = InferenceEngine(log_level=log_level)
        self.debug = debug
        self.logger = init_logger(log_level)

    def run(self):
        app = flask.Flask(__name__)
        # if self.debug:
        #     app.config["DEBUG"] = self.debug

        @app.route('/', methods=['GET'])
        def home():
            res = app.response_class(
                mimetype="application/json",
                response=json.dumps({
                    "data": "Hello Stranger"
                })
            )
            return res

        @app.route('/pinjam', methods=['POST'])
        def handle_pinjam():
            raw_data = dict(flask.request.json)
            data = sanitize_data(raw_data)
            self.logger.debug(json.dumps(data, indent=4))

            self.engine.reset()
            self.engine.infer(data)
            accepted = self.engine.check_result()
            result = ""
            if accepted:
                result = "Pinjaman Diterima"
            else:
                result = "Pinjaman Tidak Diterima"

            res = app.response_class(
                mimetype="application/json",
                response=json.dumps({
                    "hasil": result
                })
            )
            return res

        app.run(debug=self.debug, port=5000)
