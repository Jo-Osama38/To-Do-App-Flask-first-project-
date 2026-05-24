from flask import Flask , render_template, request , url_for , redirect 

app = Flask(__name__)

tasks = []

@app.route("/" , methods=["GET","POST"])
def home():
    if request.method == "GET":
        task = 'Empty'
    elif request.method == "POST":
        task = request.form.get('task')
        if task.strip():
            tasks.append(task.strip())
    return render_template ('home.html',tasks=tasks)

@app.route("/delete/<int:num>")
def delete(num):
    if num < len(tasks):
        tasks.pop(num)
    return redirect(url_for('home'))


if __name__ == "__main__":    
    app.run(debug=True)

