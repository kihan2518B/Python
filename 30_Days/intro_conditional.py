
n = int(input("Enter value of n: "))

if(n%2 == 1): #n is odd
    print("Weird")
else:
    if (n >= 2 and n <= 5):
        print("Not Weird")
    elif (n >= 6 and n <= 20):
        print("Weird")
    elif (n > 20):
        print("Not Weird")