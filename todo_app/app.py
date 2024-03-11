from flask import Flask, redirect, render_template, request
import requests
from todo_app.data.session_items import add_item, get_item, get_items, save_item
import os
from todo_app.flask_config import Config
from todo_app.models.task import Task

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    board_id = os.getenv('BOARD_ID')
    cards_path = f"/boards/{board_id}/cards"
    cards = requests.get(full_url(cards_path)).json()
    tasks = [Task.from_trello_card(card) for card in cards]
    todos = [task for task in tasks if task.not_started()]
    in_progress = [task for task in tasks if task.in_progress()]
    complete = [task for task in tasks if task.complete()]
    tasks_without_status = [task for task in tasks if task.statusless()]
    tasks_with_multiple_stati = [task for task in tasks if task.has_multiple_stati()]

    return render_template(
        "index.html",
        todos=todos,
        in_progress=in_progress,
        complete=complete,
        tasks_without_status=tasks_without_status,
        tasks_with_multiple_stati=tasks_with_multiple_stati
    )

@app.route('/add-todo', methods=['POST'])
def create():
    todo_title = request.form.get('title')
    new_card_path = "/cards"
    query = {
        "name": todo_title,
        "idList": os.getenv("LIST_ID"),
    }
    requests.request(
        "POST",
        full_url(new_card_path),
        headers={"Accept": "application/json"},
        params=query,
    )
    return redirect('/')

@app.route('/change-status/<status>/<task_id>', methods=["POST"])
def change_status(task_id, status):
    status_ids = get_status_label_ids()
    status_id = status_ids[status]
    add_status(task_id, status_id)
    return redirect('/')

def full_url(path):
    trello_api_root = "https://api.trello.com/1"
    trello_api_key = os.getenv('TRELLO_API_KEY')
    trello_api_token = os.getenv('TRELLO_API_TOKEN')
    return f"{trello_api_root}{path}?key={trello_api_key}&token={trello_api_token}"

def add_status(task_id, status_id):
    add_label_path = f"/cards/{task_id}/idLabels"
    requests.request("POST", full_url(add_label_path), params={"value": status_id})

@app.route('/remove-status/<task_id>/<status_id>', methods=["POST"])
def remove_status(task_id, status_id):
    remove_label_path = f"/cards/{task_id}/idLabels/{status_id}"
    requests.request("DELETE", full_url(remove_label_path))
    return redirect('/')

def get_status_label_ids():
    status_options = ['Not Started', 'In Progress', 'Complete']
    board_id = os.getenv('BOARD_ID')
    labels_path = f"/boards/{board_id}/labels"
    labels = requests.get(full_url(labels_path)).json()
    return {label["name"]: label["id"] for label in labels if label["name"] in status_options}
