n = int(input())
myDict = {}

for i in range(n):
    userInput = input()
    myDict[userInput.split(" ")[0]] = userInput.split(" ")[1]

names = [input() for i in range(n)]
for i in names:
    value = myDict.get(i)
    if value is not None:
        print(f"{i}={value}")
    else:
        print("Not found")
