a = int(input())
English = set(map(int,input().split()))

b = int(input())
French = set(map(int,input().split()))

print(len(English.difference(French)))
