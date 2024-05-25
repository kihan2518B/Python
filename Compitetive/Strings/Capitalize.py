# Capitalize initials of fName and lName
# Complete the solve function below.

def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))


s = input()

result = solve(s)
print(result)
