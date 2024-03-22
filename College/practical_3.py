
n = float(input("Enter any number: "))

if n > 3.7:
    grade = "A+"
elif 3.4 < n <= 3.7:
    grade = "A"
elif 3.0 < n <= 3.4:
    grade = "A-"
elif 2.7 < n <= 3.0:
    grade = "B+"
elif 2.4 < n <= 2.7:
    grade = "B"
elif 2.0 < n <= 2.4:
    grade = "B-"
elif 1.7 < n <= 2.0:
    grade = "C+"
elif 1.4 < n <= 1.7:
    grade = "C"
elif n == 1.4:
    grade = "C-"
else:
    grade = "F"
print(grade)