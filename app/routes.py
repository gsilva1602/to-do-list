from flask import render_template, request, redirect, url_for
from app import app

tasks = []

@app.route('/teste')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/remove/<int:index>')
def remove_task(index):
    try:
        task = tasks.pop(index)
    except IndexError:
        pass
    return redirect(url_for('index'))