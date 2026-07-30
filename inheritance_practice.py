class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    print("-------person class calleed constructor---")

  def printname(self):
    print(self.firstname, self.lastname)

  def shownow(self):
      print("------Person---------")

class Student(Person):
  def __init__(self, fname, lname):
      super().__init__(fname,lname)

  def show(self):
      super().shownow()
      print("-------Student--------")

x = Student("Mike", "Olsen")
x.printname()
x.shownow()
