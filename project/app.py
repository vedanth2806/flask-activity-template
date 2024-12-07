# TODO Build the app.py file along with the template.html file to create a simple To-Do List app
# The app should have routes for adding a task, and should show a list of tasks
# Everything you have learned above will be useful for this task

from flask import Flask, render_template;

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/task')
def task():
    tasks= ['play football','prepare','study']
    return render_template('tasks.html', tasks=tasks )

if __name__ == '__main__':
    app.run(port=8000)