# Given an integer,n,and n space-separated integers as
# input, create a tuple,t, of those n integers.
# Then compute and print the result of hash(t).

n = int(input())
List = list(map(int, input().split()))

if len(List) == n:
    print(hash(tuple(List)))
else:
    print("Wrong Input")
