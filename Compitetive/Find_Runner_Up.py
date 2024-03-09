# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given N scores.
# Store them in a list and find the score of the runner-up.
# Sample input or array 2,5,5,6,9,2,3
# output: 6 =>   ( cuz 9 is max and 6 is second max)

n = int(input())
arr = map(int, input().split())

sortedArr = sorted(set(arr))
print(sortedArr[-2])
