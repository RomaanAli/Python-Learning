#creating a dictornaries with multiple data
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

"""
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
"""
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
