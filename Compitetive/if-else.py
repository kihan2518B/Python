n = int(input("Enter value of n: "))
# if(n % 2 ==1 ):
#     print("Weird")
# elif(n%2 == 0 and 2<= n >=5):
#     print("Not Weird")
# elif(n%2 == 0 and 6<=n>=20):
#     print("Weird")
# elif(n%2 == 0 and n>20):
#     print("Not Weird")

if(n%2 == 1): #n is odd
    print("Weird")
else:
    if (n >= 2 and n <= 5):
        print("Not Weird")
    elif (n >= 6 and n <= 20):
        print("Weird")
    elif (n > 20):
        print("Not Weird")