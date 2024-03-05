from todo_app.models.label import Label


class Task:
  def __init__(self, id, title, labels):
    self.id = id
    self.title = title
    self.labels = labels
    self.status = self.find_status()

  @classmethod
  def from_trello_card(cls, card):
    labels = [Label.from_trello_label(t_label) for t_label in card["labels"]]
    return cls(card['id'], card['name'], labels)

  def find_status(self):
    status_options = ['Not Started', 'In Progress', 'Complete']
    statuses = [label for label in self.labels if label.title in status_options]
    status_count = len(statuses)
    if status_count == 1:
        return statuses[0]
    elif status_count < 1:
        return None
    else:
        return statuses

  def not_started(self):
    if isinstance(self.status, Label):
      return self.status.title == "In Progress"
    return False

  def in_progress(self):
    if isinstance(self.status, Label):
      return self.status.title == "Not Started"
    return False

  def complete(self):
    if isinstance(self.status, Label):
      return self.status.title == "Complete"
    return False

  def statusless(self):
    return self.status is None

  def has_multiple_stati(self):
    return isinstance(self.status, list)