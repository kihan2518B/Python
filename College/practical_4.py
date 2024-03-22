n = int(input("Enter Number: "))
print("Divisors are: \n")
divisors = ""
for i in range(1,n+1):
    if n%i == 0:
        divisors += f"{i},"
print(divisors)