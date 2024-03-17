#Applying list methods as per user
N = int(input())    #Number of commands in input
list = []
Inputs = []
for i in range(N):
    Input= input().split()
    Inputs.append(Input) #Creating an array of inputs

# applying all functions as per inputs
for j in Inputs:
    lowerInput = j[0].lower()
    if lowerInput == 'insert':
        list.insert(int(j[1]),int(j[2]))
    elif lowerInput == 'print':
        print(list)
    elif lowerInput == 'remove':
        list.remove(int(j[1]))
    elif lowerInput == 'append':
        list.append(int(j[1]))
    elif lowerInput == 'sort':
        list.sort()
    elif lowerInput == 'pop':
        list.pop(len(list) - 1)
    elif lowerInput == 'reverse':
        list.reverse()