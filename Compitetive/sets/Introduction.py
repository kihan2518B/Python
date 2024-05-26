def average(array):
    setOfArray = set(array)
    Average = sum(setOfArray)/len(setOfArray)
    return format(Average,".3f")


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)