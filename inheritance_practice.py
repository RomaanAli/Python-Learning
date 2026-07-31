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
"""
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")
        super().show()


class C(A):

    def show(self):
        print("C")
        super().show()


class D(B, C):

    def show(self):
        print("D")
        super().show()


obj = D()

print(D.mro())

obj.show()
print("----------------------")


def info():
    print("Person")


class Person:

    name="namePerson"
    age=30
    def __init__(self,name="Hammad",age=26):
        self.name = name
        self.age = age

    def set_name(self, newname):
        self.name = newname
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def get_age(self):
        return self.age


class Employee(Person):

    def work(self):
        print("Working")

class Student(Person):

    def study(self):
        print("Studying")


class TeachingAssistant(Employee, Student):
        pass

ta = TeachingAssistant()
ta.work()
ta.study()
print(TeachingAssistant.mro())
ta.set_name("Romaan Ali")
ta.set_age(23)
print("the name access from child to the grandparent person:",ta.get_name())
print("the AGE access from person:",ta.get_age())
