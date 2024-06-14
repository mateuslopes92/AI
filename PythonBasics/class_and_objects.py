# defining a class
class Human:
  def __init__(self, name, occupation):
    self.name = name
    self.occupation = occupation

  def do_work(self):
    if self.occupation == "programer":
      print(self.name, "is a programer")
    elif self.occupation == "actor":
      print(self.name, "shoots a film")

# using a class
mateus = Human("Mateus Lopes", "programer")
mateus.do_work()
