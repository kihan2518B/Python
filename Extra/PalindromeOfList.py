# Palindrome are those who reads same whether from start or end
A = [1,"Apple",3,"Apple",1]
B = A.copy()
B.reverse()
print(B)
if A == B:
    print("Palindrome")
else:
    print("Not palindrome")