from flask import Flask, render_template
app= Flask("olá, mundo")
@app.route('/alunos')
@app.route('/')
def alunos():
    return render_template("hello.html")
