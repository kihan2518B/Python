# The first line contains an integer, N (the size of our array)
# The second line contains N space-separated integers
# that describe array A's elements.
# Output: Print the elements of array A in reverse order as
# a single line of space-separated numbers.


n = int(input())
a = list(map(int, input().split()))
print(a)
revA = a[::-1]
print(revA)
String = " ".join(map(str, revA))
print(String)
