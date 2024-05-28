n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    userInp = input().split()
    if userInp[0].lower() == "pop":
        s.pop()
    elif userInp[0].lower() == "remove":
        s.remove(int(userInp[1]))
    elif userInp[0].lower() == "discard":
        s.discard(int(userInp[1]))

print(sum(s))