from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Youssef! Welcome to Flask 🚀"

@app.route("/hackclub")
def hackclub():
    return "I love building projects for Hack Club!"

@app.route("/python")
def python_page():
    return "Python is awesome!"



if __name__ == "__main__":    
    app.run(debug=True)

