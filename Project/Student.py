
Students = [
    {
        "Name": "John Smith",
        "ID": 111,
        "GPA": 71.5
    },
    {
        "Name": "Maria Jordon",
        "ID": 222,
        "GPA": 95.0
    },
    {
        "Name": "Angie Jones",
        "ID": 333,
        "GPA": 87.3
    },
    {
        "Name": "Sam Philips",
        "ID": 342,
        "GPA": 62.3
    }
]


def display_std_header():
    print("===========================================================")
    print("Student Name                 StudentID                  GPA")
    print("===========================================================")


def display_student(index: int, names: list, ids: list, gpas: list):
    display_std_header()
    print(f"{names[index]}                          {ids[index]}                     {round(gpas[index], 1)}")


def list_students(names: list, ids: list, gpas: list):
    if names == []:
        print("Students list has no students")
        exit()
    else:
        display_std_header()
        for idx in range(len(names)):
            print(f"{names[idx]}                          {ids[idx]}                     {round(gpas[idx], 1)}")



def menu():
    fileName = input("Enter the file name to load students information: ")
    if fileName.lower() == "students.txt":
        print("Students Information has been loaded from the file: ")
        print("*******************************************************")
        print("           ***Students Registration system***          ")
        print("Select from the following options\n")
        print("""L - List Students
A - Add Student
E - Edit Student
D - Delete Student
F - Find A Student
G - GPA Average
Q - Quit""")
    else:
        print(f"{fileName} does not exist - Bye")
        exit()
    usersSelection = input()
    if usersSelection.lower() == "l":
        display_student()
    else:
        print("Invalid Input")
        exit()

list_students(["Kishan","Uday","Linax"],[111,222,333],[7.5,8.5,4.56])
# menu()
