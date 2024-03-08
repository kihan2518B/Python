# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following: 123...n

n = int(input())


def printNums(n):
    listOfNum = ""
    for i in range(1, n + 1):
        listOfNum += str(i)
    return listOfNum


# calling printNums function
print(printNums(n))
