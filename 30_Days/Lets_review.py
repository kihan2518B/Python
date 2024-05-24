# print even index of sting and odd index of string in
# one line saperated with space
# The first line contains an integer, T (the number of test cases).
# Each line i of the  subsequent lines contain a string, S.
# Example: S = adbecf
# Output: abc def

T = int(input())


def odd_even(s):
    odd = ""
    even = ""
    for i in range(len(s)):
        if i%2 == 0:
            even += s[i]
        else:
            odd += s[i]
    print(even, odd)


listOfInputs = [input() for i in range(T)]

for i in listOfInputs:
    odd_even(i)

