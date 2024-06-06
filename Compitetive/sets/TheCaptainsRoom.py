
k = int(input())
RoomNumbers = list(map(int,input().split()))
RoomDict = {}
for i in RoomNumbers:
    if i in RoomDict:
        RoomDict[i] += 1
    else:
        RoomDict[i] = 1

for i,n in RoomDict.items():
    if n == 1:
        print(i)
        break
