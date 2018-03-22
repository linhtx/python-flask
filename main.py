from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "home"

if __name__ == '__main__':
    app.run(port = 80, debug = True)
    

