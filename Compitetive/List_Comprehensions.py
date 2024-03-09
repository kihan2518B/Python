#List comprehensions offers shorter syntax to make
# new list based on old list
# Syntax
# NewList = [expression for item in iterable if condition == true]

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
#
# newList = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1)  if(i+j+k != n)]
# print(newList)

SecondList = [i if i%2 == 1 else 0 for i in range(0,5) ]
print(SecondList)
