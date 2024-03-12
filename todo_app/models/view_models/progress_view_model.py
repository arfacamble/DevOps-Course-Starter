from todo_app.models.task import Task
from typing import List

class ProgressViewModel:
  _tasks: List[Task]
  _complete: List[Task]
  _in_progress: List[Task]
  _not_started: List[Task]

  def __init__(self, tasks: List[Task]):
    self._tasks = tasks
    self._complete = [task for task in tasks if task.complete()]
    self._in_progress = [task for task in tasks if task.in_progress()]
    self._not_started = [task for task in tasks if task.not_started()]

  @property
  def complete(self):
    return self._complete

  @complete.setter
  def complete(self, complete_tasks):
    if not isinstance(complete_tasks, list):
      raise TypeError("Complete Tasks must be a list")
    self._complete = complete_tasks

  @property
  def in_progress(self):
    return self._in_progress

  @in_progress.setter
  def in_progress(self, in_progress_tasks):
    if not isinstance(in_progress_tasks, list):
      raise TypeError("In progress tasks must be a list")
    self._in_progress = in_progress_tasks

  @property
  def not_started(self):
    return self._not_started

  @not_started.setter
  def not_started(self, not_started_tasks):
    if not isinstance(not_started_tasks, list):
      raise TypeError("Not started tasks must be a list")
    self._not_started = not_started_tasks
