
nA = int(input())
A = set(map(int, input().split()))

for i in range(int(input())):
    Choice = input().split()
    otherSet = set(map(int, input().split()))

    operation = Choice[0].lower()

    if operation == "intersection_update":
        A.intersection_update(otherSet)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(otherSet)
    elif operation == "difference_update":
        A.difference_update(otherSet)
    elif operation == "update":
        A.update(otherSet)

print(sum(A))
