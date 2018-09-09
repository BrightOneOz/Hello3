import os

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    lines = ["Hello World!"]
    if os.environ.get('MY_ENV_VAR'):
        lines.append(os.environ.get('MY_ENV_VAR'))

    return '\n'.join(lines)


if __name__ == "__main__":
    app.run()
