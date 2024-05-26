# There is array of n integers and two disjoint sets of m integers.
# for a value i in array if it is in A then add 1 to happiness and
# if it is in B then add -1 to happiness and else perform no action.
# Initially happiness = 0

m,n = map(int,input().split())

Array = input().split()
# print(Array)
ArrA = input().split()
ArrB = input().split()
A = {int(num) for num in ArrA}
B = {int(num) for num in ArrB}

# print(A)
happiness = 0
for i in Array:
    if int(i) in A:
        happiness += 1
    elif int(i) in B:
        happiness -= 1
print(happiness)
