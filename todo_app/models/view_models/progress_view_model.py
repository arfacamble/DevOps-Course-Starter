from todo_app.models.task import Task
from typing import List

class ProgressViewModel:
  _tasks: List[Task]
  _complete: List[Task]
  _in_progress: List[Task]
  _not_started: List[Task]
  _tasks_without_status: List[Task]
  _tasks_with_multiple_stati: List[Task]

  def __init__(self, tasks: List[Task]):
    self._tasks = tasks
    self._complete = [task for task in tasks if task.complete()]
    self._in_progress = [task for task in tasks if task.in_progress()]
    self._not_started = [task for task in tasks if task.not_started()]
    self.tasks_without_status = [task for task in tasks if task.statusless()]
    self.tasks_with_multiple_stati = [task for task in tasks if task.has_multiple_stati()]

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

  @property
  def tasks_without_status(self):
    return self._tasks_without_status

  @tasks_without_status.setter
  def tasks_without_status(self, tasks_without_status):
    if not isinstance(tasks_without_status, list):
      raise TypeError("Not started tasks must be a list")
    self._tasks_without_status = tasks_without_status

  @property
  def tasks_with_multiple_stati(self):
    return self._tasks_with_multiple_stati

  @tasks_with_multiple_stati.setter
  def tasks_with_multiple_stati(self, tasks_with_multiple_stati):
    if not isinstance(tasks_with_multiple_stati, list):
      raise TypeError("Not started tasks must be a list")
    self._tasks_with_multiple_stati = tasks_with_multiple_stati
