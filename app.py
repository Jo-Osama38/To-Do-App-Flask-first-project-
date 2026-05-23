from flask import Flask , render_template, request , url_for

app = Flask(__name__)

projectslist = ["Portfolio", "Todo App", "Blog"] 

@app.route("/" , methods=["GET","POST"])
def home():
    if request.method == "GET":
        username = "Guest"
        userage = None
    elif request.method == "POST":    
        username = request.form.get("username")
        userage = int(request.form.get("userage"))
    return render_template("home.html" , name = username ,age=userage ,language= "pyhton")

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

