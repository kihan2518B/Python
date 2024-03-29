# Palindrome are those who reads same whether from start or end
A = input()
a = list(A)
B = a.copy()
B.reverse()
if a == B:
    print("Palindrome")
else:
    print("Not palindrome")
