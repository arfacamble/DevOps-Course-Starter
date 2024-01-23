from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, get_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    todos = get_items()
    return render_template("index.html", todos=todos)

@app.route('/add-todo', methods=['POST'])
def create():
    todo_title = request.form.get('title')
    add_item(todo_title)
    return redirect('/')