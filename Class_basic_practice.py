class Car:
    def __init__(self,wheels,brand,price):
        self.wheels = wheels
        self.brand = brand
        self.price = price
    def show(self):
        print("The brand of car is:",self.brand)
        print("The wheels of car is:",self.wheels)
        print("The price of car is:",self.price)
        print("---------------------------------")

c1 = Car(4,"Alto",2000)
c2 = Car(6,"BMW",1000)
c1.show()
c2.show()
