from controller import InferenceEngine
import flask
from controller import InferenceEngine
from util import init_logger
import json
from flask_cors import CORS
from waitress import serve
from util.io import sanitize_data
engine = InferenceEngine()

app = flask.Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    res = app.response_class(
        mimetype="application/json",
        response=json.dumps({
            "data": "Hello Stranger"
        })
    )
    return res


@app.route('/api', methods=['POST'])
def handle_pinjam():
    raw_data = dict(flask.request.json)
    data = sanitize_data(raw_data)

    engine.reset()
    engine.infer(data)
    accepted = engine.check_result()
    result = ""
    message = ""
    if accepted:
        result = "y"
        message = "Pinjaman Diterima"
    else:
        result = "n"
        message = "Pinjaman Tidak Diterima"

    res = app.response_class(
        mimetype="application/json",
        response=json.dumps({
            "data": result,
            "message": message
        })
    )
    return res


if __name__ == "__main__":
    app.run(port=5000, threaded=True, host='0.0.0.0')
