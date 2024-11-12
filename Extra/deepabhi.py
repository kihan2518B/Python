# class Student:
#     def init(self, name, age, gender, hobbies, roll_no, course):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.hobbies = hobbies
#         self.roll_no = roll_no
#         self.course = course
#         self.marks = {}
#         self.calculate_percentage()
#         self.calculate_result()
#
#     def calculate_percentage(self):
#         if self.marks:
#             total_marks = sum(self.marks.values())
#             self.percentage = (total_marks / (len(self.marks) * 100)) * 100
#         else:
#             self.percentage = 0
#
#     def calculate_result(self):
#         if self.marks:
#             self.result = "Pass" if all(mark >= 40 for mark in self.marks.values()) else "Fail"
#         else:
#             self.result = "N/A"
#
#     def add_mark(self, subject, mark):
#         self.marks[subject] = mark
#         self.calculate_percentage()
#         self.calculate_result()
#
#
# class StudentManagementSystem:
#     def init(self):
#         self.students = {}
#
#     def add_student(self, name, age, gender, hobbies, roll_no, course):
#         student = Student(name, age, gender, hobbies, roll_no, course)
#         self.get_student_marks(student)
#         self.students[roll_no] = student
#         print(f"Student {name} added successfully!")
#
#     def get_student_marks(self, student):
#         print("\nEnter subject-wise marks:")
#         subjects = ["EEEE", "ME-2", "PP", "CS", "ES"]
#         for subject in subjects:
#             mark = int(input(f"Enter {subject} marks for {student.name}: "))
#             student.add_mark(subject, mark)
#
#     def remove_student(self, roll_no):
#         if roll_no in self.students:
#             del self.students[roll_no]
#             print(f"Student with Roll No. {roll_no} removed successfully!")
#         else:
#             print("Student not found.")
#
#     def update_student_details(self, roll_no, **kwargs):
#         if roll_no in self.students:
#             student = self.students[roll_no]
#             for key, value in kwargs.items():
#                 setattr(student, key, value)
#             print(f"Student details updated successfully!")
#         else:
#             print("Student not found.")
#
#     def view_student_details(self, roll_no):
#         if roll_no in self.students:
#             student = self.students[roll_no]
#             print(f"\n===== Student Details =====")
#             print(f"Name: {student.name}")
#             print(f"Age: {student.age}")
#             print(f"Gender: {student.gender}")
#             print(f"Hobbies: {', '.join(student.hobbies)}")
#             print(f"Roll No: {student.roll_no}")
#             print(f"Course: {student.course}")
#             print("\nAcademic Details:")
#             print("Subject-wise Marks:")
#             for subject, mark in student.marks.items():
#                 print(f"  {subject}: {mark} {'(Pass)' if mark >= 40 else '(Fail)'}")
#             print(f"\nOverall Percentage: {student.percentage:.2f}%")
#             print(f"Overall Result: {student.result}")
#         else:
#             print("Student not found.")
#
#
# # Interactive menu for the student management system
# def main():
#     sms = StudentManagementSystem()
#
#     while True:
#         print("\n===== Student Management System =====")
#         print("1. Add Student")
#         print("2. Remove Student")
#         print("3. Update Student Details")
#         print("4. View Student Details")
#         print("5. Exit")
#
#         choice = input("Enter your choice (1-5): ")
#
#         if choice == "1":
#             name = input("Enter student's name: ")
#             age = int(input("Enter student's age: "))
#             gender = input("Enter student's gender: ")
#             hobbies = input("Enter student's hobbies (comma-separated): ").split(',')
#             roll_no = int(input("Enter student's roll number: "))
#             course = input("Enter student's course: ")
#             sms.add_student(name, age, gender, hobbies, roll_no, course)
#
#         elif choice == "2":
#             roll_no = int(input("Enter roll number of student to remove: "))
#             sms.remove_student(roll_no)
#
#         elif choice == "3":
#             roll_no = int(input("Enter roll number of student to update: "))
#             attribute = input("Enter attribute to update (name/age/gender/hobbies/course): ")
#             value = input(f"Enter new value for {attribute}: ")
#             sms.update_student_details(roll_no, **{attribute: value})
#
#         elif choice == "4":
#             roll_no = int(input("Enter roll number of student to view details: "))
#             sms.view_student_details(roll_no)
#
#         elif choice == "5":
#             print("Exiting Student Management System. Goodbye!")
#             break
#
#         else:
#             print("Invalid choice. Please enter a valid option (1-5).")
#
#
# if name == "main":
#     main()
#
# class Student:
#     def init(self, name, age, gender, hobbies, roll_no, course):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.hobbies = hobbies
#         self.roll_no = roll_no
#         self.course = course
#         self.marks = {}
#         self.calculate_percentage()
#         self.calculate_result()
#
#     def calculate_percentage(self):
#         if self.marks:
#             total_marks = sum(self.marks.values())
#             self.percentage = (total_marks / (len(self.marks) * 100)) * 100
#         else:
#             self.percentage = 0
#
#     def calculate_result(self):
#         if self.marks:
#             self.result = "Pass" if all(mark >= 40 for mark in self.marks.values()) else "Fail"
#         else:
#             self.result = "N/A"
#
#     def add_mark(self, subject, mark):
#         self.marks[subject] = mark
#         self.calculate_percentage()
#         self.calculate_result()
#
#
# class StudentManagementSystem:
#     def init(self):
#         self.students = {}
#
#     def add_student(self, name, age, gender, hobbies, roll_no, course):
#         student = Student(name, age, gender, hobbies, roll_no, course)
#         self.get_student_marks(student)
#         self.students[roll_no] = student
#         print(f"Student {name} added successfully!")
#
#     def get_student_marks(self, student):
#         print("\nEnter subject-wise marks:")
#         subjects = ["EEEE", "ME-2", "PP", "CS", "ES"]
#         for subject in subjects:
#             mark = int(input(f"Enter {subject} marks for {student.name}: "))
#             student.add_mark(subject, mark)
#
#     def remove_student(self, roll_no):
#         if roll_no in self.students:
#             del self.students[roll_no]
#             print(f"Student with Roll No. {roll_no} removed successfully!")
#         else:
#             print("Student not found.")
#
#     def update_student_details(self, roll_no, **kwargs):
#         if roll_no in self.students:
#             student = self.students[roll_no]
#             for key, value in kwargs.items():
#                 setattr(student, key, value)
#             print(f"Student details updated successfully!")
#         else:
#             print("Student not found.")
#
#     def view_student_details(self, roll_no):
#         if roll_no in self.students:
#             student = self.students[roll_no]
#             print(f"\n===== Student Details =====")
#             print(f"Name: {student.name}")
#             print(f"Age: {student.age}")
#             print(f"Gender: {student.gender}")
#             print(f"Hobbies: {', '.join(student.hobbies)}")
#             print(f"Roll No: {student.roll_no}")
#             print(f"Course: {student.course}")
#             print("\nAcademic Details:")
#             print("Subject-wise Marks:")
#             for subject, mark in student.marks.items():
#                 print(f"  {subject}: {mark} {'(Pass)' if mark >= 40 else '(Fail)'}")
#             print(f"\nOverall Percentage: {student.percentage:.2f}%")
#             print(f"Overall Result: {student.result}")
#         else:
#             print("Student not found.")
#
#
# # Interactive menu for the student management system
# def main():
#     sms = StudentManagementSystem()
#
#     while True:
#         print("\n===== Student Management System =====")
#         print("1. Add Student")
#         print("2. Remove Student")
#         print("3. Update Student Details")
#         print("4. View Student Details")
#         print("5. Exit")
#
#         choice = input("Enter your choice (1-5): ")
#
#         if choice == "1":
#             name = input("Enter student's name: ")
#             age = int(input("Enter student's age: "))
#             gender = input("Enter student's gender: ")
#             hobbies = input("Enter student's hobbies (comma-separated): ").split(',')
#             roll_no = int(input("Enter student's roll number: "))
#             course = input("Enter student's course: ")
#             sms.add_student(name, age, gender, hobbies, roll_no, course)
#
#         elif choice == "2":
#             roll_no = int(input("Enter roll number of student to remove: "))
#             sms.remove_student(roll_no)



class Student:
    def __init__(self, name, age, gender, hobbies, roll_no, course):
        self.name = name
        self.age = age
        self.gender = gender
        self.hobbies = hobbies
        self.roll_no = roll_no
        self.course = course
        self.marks = {}
        self.calculate_percentage()
        self.calculate_result()

    def calculate_percentage(self):
        if self.marks:
            total_marks = sum(self.marks.values())
            self.percentage = (total_marks / (len(self.marks) * 100)) * 100
        else:
            self.percentage = 0

    def calculate_result(self):
        if self.marks:
            self.result = "Pass" if all(mark >= 40 for mark in self.marks.values()) else "Fail"
        else:
            self.result = "N/A"

    def add_mark(self, subject, mark):
        self.marks[subject] = mark
        self.calculate_percentage()
        self.calculate_result()


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, age, gender, hobbies, roll_no, course):
        student = Student(name, age, gender, hobbies, roll_no, course)
        self.get_student_marks(student)
        self.students[roll_no] = student
        print(f"Student {name} added successfully!")

    def get_student_marks(self, student):
        print("\nEnter subject-wise marks:")
        subjects = ["EEEE", "ME-2", "PP", "CS", "ES"]
        for subject in subjects:
            mark = int(input(f"Enter {subject} marks for {student.name}: "))
            student.add_mark(subject, mark)

    def remove_student(self, roll_no):
        if roll_no in self.students:
            del self.students[roll_no]
            print(f"Student with Roll No. {roll_no} removed successfully!")
        else:
            print("Student not found.")

    def update_student_details(self, roll_no, **kwargs):
        if roll_no in self.students:
            student = self.students[roll_no]
            for key, value in kwargs.items():
                setattr(student, key, value)
            print(f"Student details updated successfully!")
        else:
            print("Student not found.")

    def view_student_details(self, roll_no):
        if roll_no in self.students:
            student = self.students[roll_no]
            print(f"\n===== Student Details =====")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Gender: {student.gender}")
            print(f"Hobbies: {', '.join(student.hobbies)}")
            print(f"Roll No: {student.roll_no}")
            print(f"Course: {student.course}")
            print("\nAcademic Details:")
            print("Subject-wise Marks:")
            for subject, mark in student.marks.items():
                print(f"  {subject}: {mark} {'(Pass)' if mark >= 40 else '(Fail)'}")
            print(f"\nOverall Percentage: {student.percentage:.2f}%")
            print(f"Overall Result: {student.result}")
        else:
            print("Student not found.")


# Interactive menu for the student management system
def main():
    sms = StudentManagementSystem()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student Details")
        print("4. View Student Details")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            gender = input("Enter student's gender: ")
            hobbies = input("Enter student's hobbies (comma-separated): ").split(',')
            roll_no = int(input("Enter student's roll number: "))
            course = input("Enter student's course: ")
            sms.add_student(name, age, gender, hobbies, roll_no, course)

        elif choice == "2":
            roll_no = int(input("Enter roll number of student to remove: "))
            sms.remove_student(roll_no)

        elif choice == "3":
            roll_no = int(input("Enter roll number of student to update: "))
            attribute = input("Enter attribute to update (name/age/gender/hobbies/course): ")
            value = input(f"Enter new value for {attribute}: ")
            sms.update_student_details(roll_no, **{attribute: value})

        elif choice == "4":
            roll_no = int(input("Enter roll number of student to view details: "))
            sms.view_student_details(roll_no)

        elif choice == "5":
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-5).")


if __name__ == "__main__":
    main()
