#loop practice in tuple
from turtledemo.penrose import start
"""
subjects = ("Math", "Physics", "English", "Programming")

for subject in subjects:
    print(subject)

i=0
while i < len(subjects):
    print(subjects[i])
    i+=1

#counting the numbers appear in the tuple
numbers = (10, 20, 30, 40, 20, 50, 20)
t = input("Enter the values in tuple separated by space:")
my_tuple = tuple(map(int,t.split()))
cout=0
c=0
li=[]
for i,number in enumerate(numbers,start=0):
    if number == 20:
        cout+=1
        li.append(i)
print(li)
for i,n in enumerate(my_tuple,start=0):
    if n == 20:
        c+=1

print("The number of time 20 appear in tuple:",cout)
print("The number of time 20 appear in tuple:",c)
"""

#packing and unpacking in tuple
intern = ("Romaan", 25, "Backend-itern", "Raiwind" , "Grayphite")
name, age, role, location, company = intern

print("The name is: ",name)
print("The age is: ",age)
print("The role is: ",role)
print("The location is: ",location)
print("The company is: ",company)

name,age,*info= intern
print("The name is: ",name)
print("The age is: ",age)
print("The Role , location adn Company is: ",info)

