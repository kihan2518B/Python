# A strict superset has at least one element that does not exist in its subset.

A = set(map(int,input().split()))
res = True
listOfSubset = []
for i in range(int(input())):
    SubSet = set(map(int,input().split()))
    listOfSubset.append(SubSet)

for subset in listOfSubset:
    for i in subset:
        if res:
            if i not in A:
                res = False
                break

    for a in A:
        if res:
            if a not in subset:
                res = True
                break

print(res)

