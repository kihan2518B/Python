
# Learning
'''My_Dict = {
    "name": "Kishan",
    "roll": 6,
    "Address": "Visnagar",
    "marks": {
        "AP1": 45,
        "Maths": 26,
        "PSCT": 30
    }
}

# methods
AllKeys = My_Dict.keys()
print(AllKeys)
AllValues = My_Dict.values()
print(AllValues)
Key_values_pair = My_Dict.items()
print(Key_values_pair)
marks_items = My_Dict["marks"].items()
print(marks_items)

ValueOfKey = My_Dict.get("name")
print(ValueOfKey)

updatedMarksDict = {
    "Maths": 50, #Overwrites if key matches the old key in dict
    "EGD": 55,
    "ECME": 40
}
# Updating maths marks
update = My_Dict["marks"].update(updatedMarksDict) #Returns None
print(update)
print("My_Dict after update", My_Dict)
empty_dict = {}'''

# Practice
# WAP to enter marks of 3 shubjects from the user and store them in dictionary.
# Start with empty dictionary

Marks = {}

for i in range(3):
    subjectName = input("\nEnter Subject Name: ")
    marks = int(input("\nEnter Marks: "))
    Marks.update({subjectName: marks})

print(Marks)
