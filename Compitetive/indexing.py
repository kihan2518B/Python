# take input of a phrase or sentence
# store the number of time each word comes in that sentence
# and then print it
# hint use dictionary

arr = input().split()
print(arr)
dict = {}
setOfArr = set(arr)
for i in setOfArr:
    count = 0
    for j in arr:
        if i == j:
            count+=1
        dict.update({i:count})

print(dict)