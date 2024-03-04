class Label:
  def __init__(self, id, title):
    self.id = id
    self.title = title

  @classmethod
  def from_trello_label(cls, t_label):
    return cls(t_label['id'], t_label['name'])