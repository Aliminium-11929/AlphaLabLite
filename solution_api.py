from flask import Flask, request
from flask.json import jsonify

from execute import execute
from view import view

app = Flask(__name__)


@app.route("/execute", methods=["POST"])
def execute_runner():
    script: str = request.json.get("script", "")
    output = execute(script=script.splitlines())
    return jsonify(output), 201


@app.route("/view/<id>", methods=["GET"])
def view_runner(id: str):
    varnames = request.args.getlist("items")
    output = view(id=id, varnames=varnames)
    return jsonify(output), 200


if __name__ == "__main__":
    app.run(port=8000, debug=False)
