"""
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
"""
class father:
    def show(self):
        print("--------FATHER----------")
class mother:
    def show(self):
        print("--------MOTHER----------")
class child(father,mother):
    pass

c=child()
c.show()
print(child.mro())
print(child.__mro__)