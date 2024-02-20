from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, get_item, get_items, save_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    all_items = get_items()
    todos, completed = [], []
    for item in all_items:
        (completed if item['status'] == 'Completed' else todos).append(item)
    return render_template("index.html", todos=todos, completed=completed)

@app.route('/add-todo', methods=['POST'])
def create():
    todo_title = request.form.get('title')
    add_item(todo_title)
    return redirect('/')

@app.route('/mark_complete/<int:id>', methods=["POST"])
def mark_complete(id):
    todo_to_complete = get_item(id)
    todo_to_complete["status"] = "Completed"
    save_item(todo_to_complete)
    return redirect('/')