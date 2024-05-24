# srting validatory function in python
# isalnum(),
# isalpha(),
# isdigit(),
# islower(),
# isupper()


s = input()
isAnum = "False"
isAlpha = "False"
isDigit = "False"
isLower = "False"
isUpper = "False"
for i in s:
    if i.isalnum():
        isAnum = "True"
    if i.isalpha():
        isAlpha = "True"
    if i.isdigit():
        isDigit = "True"
    if i.islower():
        isLower = "True"
    if i.isupper():
        isUpper = "True"

print(isAnum)
print(isAlpha)
print(isDigit)
print(isLower)
print(isUpper)
