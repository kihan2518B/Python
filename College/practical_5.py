
listOfInput = input().split()
evenList = []
for i in listOfInput:
    userInput = int(i)
    if userInput % 2 == 0:
        evenList.append(userInput)
print(evenList)