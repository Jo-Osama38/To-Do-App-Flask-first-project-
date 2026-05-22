from flask import Flask , render_template, request

app = Flask(__name__)

projectslist = ["Portfolio", "Todo App", "Blog"]

@app.route("/" , methods=["GET","POST"])
def home():
    username = request.form.get("username")
    return render_template("home.html" , name = username ,age= 2 ,language= "pyhton")

@app.route("/about")
def about():
    return render_template ("about.html")

@app.route("/projects")
def projects ():
    return render_template("projects.html", projects = projectslist)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":    
    app.run(debug=True)

