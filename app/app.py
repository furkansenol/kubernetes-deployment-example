from flask import Flask
from structlog import get_logger

logger = get_logger()

app = Flask(__name__)


@app.route("/", methods=["POST"])
def handle_post():
    logger.info(event="POST endpoint called")

    return "Hello from POST endpoint"


@app.route("/", methods=["PATCH"])
def handle_patch():
    logger.info(event="PATCH endpoint called")

    return "Hello from PATCH endpoint"


@app.route("/", methods=["GET"])
def handle_get():
    logger.info(event="GET endpoint called")

    return "Hello World!"


@app.route("/", methods=["DELETE"])
def handle_delete():
    logger.info(event="DELETE endpoint called")

    return "Hello from DELETE endpoint"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
