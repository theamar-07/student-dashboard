from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

study_tasks = []

@app.route('/')
def home():
    current_time = datetime.now().strftime("%I:%M %p")
    return render_template('index.html', python_time=current_time, tasks=study_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form.get('task_input')
    if new_task:
        study_tasks.append(new_task)
    return redirect(url_for('home')) # Refresh the page to show the new task

@app.route('/delete/<int:task_index>')
def delete_task(task_index):
    
    if 0 <= task_index < len(study_tasks):
        study_tasks.pop(task_index)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
