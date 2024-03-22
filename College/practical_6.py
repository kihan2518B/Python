
# abcabca

stringOfInput = input()
halfLength = int(len(stringOfInput)/2)
status = ""
for i in range(halfLength):
    if stringOfInput[i] == stringOfInput[i+3]:
        status = "happy"
    else:
        status = "unhappy"
print("status",status)