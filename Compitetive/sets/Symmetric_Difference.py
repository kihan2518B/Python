
m = int(input())
listInputA = input().split()
newListA = list(map(int, listInputA))
a = set(newListA)

n = int(input())
listInputB = input().split()
newListB = list(map(int, listInputB))
b = set(newListB)

# print(a.difference(b),b.difference(a))
List = list(a.difference(b))
List.extend(b.difference(a))
List.sort()
# print(List)
for i in List:
    print(i)