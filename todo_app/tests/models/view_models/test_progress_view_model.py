from todo_app.models.label import Label
from todo_app.models.task import Task
from todo_app.models.view_models.progress_view_model import ProgressViewModel

def test_progress_view_model_sorts_tasks_correctly_that_are_complete():
  complete_label = Label("id1", "Complete")
  in_progress_label = Label("id2", "In Progress")
  complete_task = Task("id1", "done task", [complete_label])
  tasks = [
    complete_task,
    Task("id2", "ongoing job", [in_progress_label]),
  ]
  view_model = ProgressViewModel(tasks)
  assert len(view_model.complete) is 1
  assert view_model.complete[0] is complete_task

def test_progress_view_model_sorts_tasks_correctly_that_are_in_progress():
  complete_label = Label("id1", "Complete")
  in_progress_label = Label("id2", "In Progress")
  in_progress_task = Task("id1", "in progress task", [in_progress_label])
  tasks = [
    in_progress_task,
    Task("id2", "complete job", [complete_label]),
  ]
  view_model = ProgressViewModel(tasks)
  assert len(view_model.in_progress) is 1
  assert view_model.in_progress[0] is in_progress_task
