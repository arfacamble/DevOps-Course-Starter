class ProgressViewModel:
  def __init__(self, tasks):
    self._tasks = tasks
    self.complete = [task for task in tasks if task.complete()]

  @property
  def complete(self):
    return self._complete

  @complete.setter
  def complete(self, complete_tasks):
    if not isinstance(complete_tasks, list):
      raise TypeError("Complete Tasks must be a list")
    self._complete = complete_tasks
