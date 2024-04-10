from todo_app.models.task import Task
from typing import List

class ProgressViewModel:
  _tasks: List[Task]

  def __init__(self, tasks: List[Task]):
    self._tasks = tasks

  @property
  def complete(self):
    return [task for task in self._tasks if task.complete()]

  @property
  def in_progress(self):
    return [task for task in self._tasks if task.in_progress()]

  @property
  def not_started(self):
    return [task for task in self._tasks if task.not_started()]

  @property
  def tasks_without_status(self):
    return [task for task in self._tasks if task.statusless()]

  @property
  def tasks_with_multiple_stati(self):
    return [task for task in self._tasks if task.has_multiple_stati()]
