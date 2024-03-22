
StudentsLists = [
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
    if not names:
        print("Students list has no students")
        menu()
    else:
        display_std_header()
        for idx in range(len(names)):
            print(f"{names[idx]}                          {ids[idx]}                     {round(gpas[idx], 1)}")
        menu()


def edit_student(index: int, listOfIDs: list, lisOfNames: list, listOfGPAs: list):
    print(listOfIDs[index])
    print(lisOfNames[index])
    print(listOfGPAs[index])
    newName = input("Enter Name: ")
    newGPA = float(input("Enter GPA: "))
    lisOfNames[index] = newName
    listOfGPAs[index] = newGPA
    print(listOfIDs[index])
    print(lisOfNames[index])
    print(listOfGPAs[index])
    menu()


def delete_student(index: int, listOfIDs: list, listOfNames: list, listOfGPAs: list):
    studentID = listOfIDs[index]
    print(listOfIDs[index])
    print(listOfNames[index])
    print(listOfGPAs[index])
    listOfIDs.pop(index)
    listOfNames.pop(index)
    listOfGPAs.pop(index)
    print(listOfIDs)
    print(f"Student with ID {studentID} is deleted")
    menu()


def menu():
    print("*******************************************************")
    print("           ***Students Registration system***          ")
    print("*******************************************************")
    print("Select from the following options\n")
    print("""L - List Students
A - Add Student
E - Edit Student
D - Delete Student
F - Find A Student
G - GPA Average
Q - Quit""")

    usersSelection = input()
    if usersSelection.lower() == "l":
        listOfNames = []
        listOfGPAs = []
        listOfIDS = []
        for student in StudentsLists:
            listOfIDS.append(student.get("ID"))
            listOfNames.append(student.get("Name"))
            listOfGPAs.append(student.get("GPA"))
        list_students(listOfNames, listOfIDS, listOfGPAs)

    elif usersSelection.lower() == "a":
        add_student(["Kishan", "Uday", "Nilax"], [111, 222, 333], [7.5, 8.5, 4.56])
    elif usersSelection.lower() == "e":
        listOfNames = []
        listOfGPAs = []
        listOfIDS = []
        for student in StudentsLists:
            listOfIDS.append(student.get("ID"))
            listOfNames.append(student.get("Name"))
            listOfGPAs.append(student.get("GPA"))
        inputID = int(input("Enter students ID: "))
        if inputID in listOfIDS:
            index = listOfIDS.index(inputID)
            edit_student(index, listOfIDS, listOfNames, listOfGPAs)
        else:
            print(f"No student with ID {inputID} \n")
            menu()
    elif usersSelection.lower() == "d":
        listOfIDS = []
        listOfNames = []
        listOfGPAs = []
        for student in StudentsLists:
            listOfIDS.append(student.get("ID"))
            listOfNames.append(student.get("Name"))
            listOfGPAs.append(student.get("GPA"))
        inputID = int(input("Enter students ID: "))
        if inputID in listOfIDS:
            index = listOfIDS.index(inputID)
            delete_student(index, listOfIDS, listOfNames, listOfGPAs)
        else:
            print(f"No student with ID {inputID} \n")
            menu()
    else:
        print("Invalid Input")
        exit()


def add_student(names: list, ids: list, gpas: list):
    print("Adding a student ...")
    newStudentId = int(input("Enter student id: "))
    for ID in ids:
        if newStudentId == ID:
            print(f"A student with ID {ID} already exists")
            menu()

    newStudentName = input("Enter student name: ")
    newStudentGPA = float(input("Enter student GPA: "))
    names.append(newStudentName)
    ids.append(newStudentId)
    gpas.append(newStudentGPA)
    print(f"The student with id {newStudentId} is added.")
    menu()


fileName = input("Enter the file name to load students information: ")
if fileName.lower() == "students.txt":
    print("Students Information has been loaded from the file: ")
    menu()
else:
    print(f"{fileName} does not exist - Bye")
