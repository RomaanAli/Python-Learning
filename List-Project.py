#-------Student Mangement System----------
students = []


def display_menu():
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Sort by Marks")
    print("7. Total Students")
    print("8. Exit")


def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = int(input("Enter Marks: "))

    student = [name, age, marks]
    students.append(student)

    print("Student Added Successfully!")


def display_students():
    if len(students) == 0:
        print("No Students Found.")
        return

    print("\nName\tAge\tMarks")
    print("-" * 30)

    for student in students:
        print(student[0], "\t", student[1], "\t", student[2])


def search_student():
    name = input("Enter Student Name: ")

    for student in students:
        if student[0].lower() == name.lower():
            print("\nStudent Found")
            print("Name :", student[0])
            print("Age :", student[1])
            print("Marks :", student[2])
            return

    print("Student Not Found.")


def update_marks():
    name = input("Enter Student Name: ")

    for student in students:
        if student[0].lower() == name.lower():
            marks = int(input("Enter New Marks: "))
            student[2] = marks
            print("Marks Updated Successfully!")
            return

    print("Student Not Found.")


def delete_student():
    name = input("Enter Student Name: ")

    for student in students:
        if student[0].lower() == name.lower():
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found.")


def sort_students():
    students.sort(key=lambda student: student[2], reverse=True)
    print("Students Sorted by Marks.")


def total_students():
    print("Total Students :", len(students))


while True:

    display_menu()

    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_marks()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        sort_students()

    elif choice == 7:
        total_students()

    elif choice == 8:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")