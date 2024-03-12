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

def test_progress_view_model_sorts_tasks_correctly_that_are_not_started():
  complete_label = Label("id1", "Complete")
  not_started_label = Label("id2", "Not Started")
  not_started_task = Task("id1", "task to do", [not_started_label])
  tasks = [
    not_started_task,
    Task("id2", "complete job", [complete_label]),
  ]
  view_model = ProgressViewModel(tasks)
  assert len(view_model.not_started) is 1
  assert view_model.not_started[0] is not_started_task

def test_progress_view_model_sorts_multiple_tasks_correctly():
  complete_label = Label("id1", "Complete")
  in_progress_label = Label("id2", "In Progress")
  not_started_label = Label("id2", "Not Started")
  complete_titles = ["All done", "meets minimum requirements"]
  in_progress_titles = ["bit of a slog", "nearly there", "get it over the line"]
  not_started_titles = ["tax return", "water bill"]
  tasks = []
  for i, title in enumerate(complete_titles):
    tasks.append(Task(f"id{i}", title, [complete_label]))
  for i, title in enumerate(in_progress_titles):
    tasks.append(Task(f"id{i}", title, [in_progress_label]))
  for i, title in enumerate(not_started_titles):
    tasks.append(Task(f"id{i}", title, [not_started_label]))
  view_model = ProgressViewModel(tasks)
  assert len(view_model.not_started) is len(not_started_titles)
  assert [task.title for task in view_model.not_started].sort() == not_started_titles.sort()
  assert len(view_model.in_progress) is len(in_progress_titles)
  assert [task.title for task in view_model.in_progress].sort() == in_progress_titles.sort()
  assert len(view_model.complete) is len(complete_titles)
  assert [task.title for task in view_model.complete].sort() == complete_titles.sort()
