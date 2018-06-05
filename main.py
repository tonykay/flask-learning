from flask import Flask, send_file
app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World from Flask"

if __name__ == '__main__':
    app.run(debug=True)
