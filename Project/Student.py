
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
        print("L")
    else:
        print("Invalid Input")
        exit()

menu()
