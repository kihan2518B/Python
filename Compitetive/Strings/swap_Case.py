# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters
# and vice versa.

def swap_case(s):
    stringList = list(s)
    StringOfList = ''
    for i in stringList:
        String = str(i)
        Upper = String.upper()
        Lower = String.lower()
        if String == Upper:
            StringOfList += String.lower()
            # print(StringOfList)
        else:
            StringOfList += String.upper()
            # print(StringOfList)
    return StringOfList

a = swap_case(input())
print(a)