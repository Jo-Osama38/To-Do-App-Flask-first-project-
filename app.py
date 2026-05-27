from flask import Flask , render_template, request , url_for , redirect 
import sqlite3

app = Flask(__name__)

def db_connection ():
    conn = sqlite3.connect("task.db")
    return conn
def db_init():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS tasks (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   task TEXT NOT NULL ,
                   completed INTEGER DEFAULT 0 )
                   """)
    conn.commit()
    conn.close()
    

@app.route("/" , methods=["GET","POST"])
def home():
    if request.method == "GET":
        task = 'Empty'
    elif request.method == "POST":
        task = request.form.get('task')
        if task.strip():
            conn = db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
            conn.commit()

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.commit()
    conn.close()
    return render_template ('home.html',tasks=tasks)

@app.route("/delete/<int:num>")
def delete(num):

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = (?)', (num,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route("/complete/<int:num>")
def complete(num):
    conn = db_connection()
    cursor =  conn.cursor()
    cursor.execute('UPDATE tasks SET completed = 1 WHERE id = (?)' , (num,) )
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route("/uncomplete/<int:num>")
def uncomplete(num):
    conn = db_connection()
    cursor =  conn.cursor()
    cursor.execute('UPDATE tasks SET completed = 0 WHERE id = (?)' , (num,) )
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route("/edit/<int:num>", methods=["GET","POST"])
def edit(num):
    if request.method == "GET":
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT task FROM tasks WHERE id =(?)',(num,))
        task = cursor.fetchone()
        conn.commit()
        conn.close()
        return render_template('edit.html' ,task = task)
    elif request.method == "POST":
        editTask = request.form.get('editTask')
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET task = ?  WHERE id =(?)',(editTask , num,))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))

db_init()
if __name__ == "__main__":    
    app.run(debug=True)

