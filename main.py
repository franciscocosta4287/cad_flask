from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "asdasdsadsadsadsadsad"


app.run(debug=True)