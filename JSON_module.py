import json

user = {
    "name": "Ali",
    "age": 22
}

json_data = json.dumps(user)

print(json_data)
user.update({"department": "Software Engineer","gender":"male"})
json_data=json.dumps(user)
print("after adding new entries:",json_data)

print("access by loop--:",json_data[1])
for i in json_data:
    print(i,end="")

data='{"company": "Graphite"}'

"""json_data = json.loads(data)
print("\n\ncompany added:",json_data)
json_data = json.loads('{"programming": "python"}')
print("\n\n",json_data)
"""


with (open("./test.json","w")) as json_file:
    json.dump(json_data,json_file,indent=4)

with open("./test.json","r") as json_file:
    json_data = json.load(json_file)

print("\n\njson file data:",json_data)


students = [
    {
        "id": 1,
        "name": "Ali",
        "marks": 85
    },
    {
        "id": 2,
        "name": "Ahmed",
        "marks": 90
    }
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    student_data = json.load(file)

print("Student data:",student_data)

new_student =[
    {
        "id": 3,
        "name": "Hassan",
        "marks": 70
    },
    {
        "id": 4,
        "name": "Romaan",
        "marks": 95
    }
]
with open("students.json", "w") as file:
    json.dump(new_student, file, indent=4)

for student in student_data:
    print(student["name"], student["marks"])


FILE_NAME = "users.json"

def load_users():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)

users = load_users()
users.append({
    "id": 1,
    "name": "Ali",
    "age": 22
})

save_users(users)
