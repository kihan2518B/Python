
# else if conditonal statement example
# Traffic light

trafficLight = "GreeN"

if(trafficLight.lower() == "red"):
    print("You have to stop")
elif(trafficLight.lower() == "yellow"):
    print("Your wait is near to be over")
elif(trafficLight.lower() == "green"):
    print("You may go now")
else:
    print("light is broken")

#Another example
print("**************Gues the Output ******************")
# A = int(input("A: "))
# G = input("Choose M/F: ")
A = 2
G = "M"
if((A == 1 or A == 2) and G == "M"):
    print("100")
elif(A == 3 or A == 4 or G=="F"):
    print("200")
elif(A == 5 and G == "M"):
    print("300")
else:
    print("no fee")

#Ternary operator
print('*************** Ternary operator ***************')

n = 2
print("true") if n != 2 else print("false")

print("********* Clever if/ternary operator ********")

age = int(input("Enter Age"))
value = ("yes","no") [age < 18]
print(value)

# other example
sal = int(input("Enter salary"))
tax = sal*(0.1,0.2) [sal >= 50000]
print(tax)