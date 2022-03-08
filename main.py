from flask import Flask
import flask

app = Flask(__name__)

@app.route('/')
def magic_ball():
    return "<center><h1> Welcome to Magic 8 Ball!!</h1></center>"

if __name__ == "__main__":
    app.run(debug=True)
