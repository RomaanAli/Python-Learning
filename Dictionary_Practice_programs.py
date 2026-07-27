# creating a dictornaries with multiple data
import copy

"""
student= {
    "name" :"Romaan",
    "age" : 22,
    "roll_no": 105,
    "course" : "Sofwtare Engineering",
    "marks":100,
    "id":1002
}
def display():
    print("-------------------")
    for key,value in student.items():
        print(f"{key}: {value}")


#removing values
print("deleting value with --id-- pop():",student.pop("marks"))
display()
print("deleting value with popitem():",student.popitem())
display()
print("deleting value with - del():")
del student["roll_no"]
display()
print("deleting value with --id-- clear():",student.clear())
display()
#applying loops on dictionary
print("For loop with .items both key and value.")
for key,value in student.items():
    print(f"{key}: {value}")
#for loop with just keys
for key in student.keys():
    print(f"{key}")
#for loop with values:
for value in student.values():
        print(f"{value}:")

#Copy or deep copy
person={
    "name":"Romaan",
    "age":22,
    "siblings":[2,1]
}
person2 = person.copy()
print("Before person:",person)
print("Before person2:",person2)
person2.update({"status":"unemployed"})
person["siblings"].append(5)
print("After person:",person)
print("After person2:",person2)

print("------------------------")

person2=copy.deepcopy(person)
print("Before person:",person)
print("Before person2:",person2)
person2.update({"status":"unemployed"})
person["siblings"].append(5)
person2["siblings"].append(10)
print("After person:",person)
print("After person2:",person2)

#nested dictionaries
students= {
    "101":{
    "name":"Romaan",
    "age":21,
    "marks":90},
    "102":{
    "name":"Hassan",
    "age":22,
    "marks":85},
    "103":{
    "name":"Talha",
    "age":25,
    "marks":70},
}
print("The marks of 102 student:",students["102"]["marks"])
students["101"]["age"]=30
print("The updated age of 101 student:",students["101"]["age"])
students["103"].update({"status":"unemployed"})
print("The updated info 103 student:",students["103"])

#find the student with heighest marks

# find the student with highest marks
max_value = 0
for rol, info in students.items():
    for key, value in info.items():
        if key == "marks":
            if max_value < value:
                max_value = value

print("The heighest marks:",max_value)
print("-----------------------")
#deleting the student 102
del students["102"]
print(students)
"""
students = {
    101: {
        "name": "Romaan",
        "age": "22",
        "roll_no": "105",
    }

}
# taking user input
num =int(input("Enter the number of students: "))
for i in range(num):
    print("----Enter Student details----")

    student_id = int(input("Enter unique student ID(as 101): "))

    na = input("Enter name of student:")
    ag = input("Enter age of student:")
    rol = input("Enter roll no of student:")

    students[student_id]={
        "name":na,
        "age":ag,
        "roll_no":rol,
    }

for x,info in students.items():
    print("-------------------")
    print(x)
    for key, value in info.items():
        print(f"{key}: {value}")


