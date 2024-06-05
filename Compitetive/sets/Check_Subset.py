T = int(input())

res = []
for i in range(T):
    nA = int(input())
    A = set(map(int,input().split()))

    nB = int(input())
    B = set(map(int,input().split()))
    res.append(str(A.issubset(B)))

print("\n".join(res))
