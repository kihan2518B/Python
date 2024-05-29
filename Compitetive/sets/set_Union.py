a = int(input())
French = set(map(int,input().split()))

b = int(input())
English = set(map(int,input().split()))

print(len(English|French))