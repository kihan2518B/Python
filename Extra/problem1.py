TemperatureList = []
for i in range(999):
    Temperatures = int(input("Enter temperature: "))
    
    TemperatureList.append(Temperatures)
    
    if (Temperatures == 999):
        break
    

# Average = Sum/len(TemperatureList)
# print(Average)

print(TemperatureList)
Sum = 0
for i in TemperatureList:
    Sum = Sum + i

Average = Sum/len(TemperatureList)
print("Average is: ",Average)
count = 0
for i in TemperatureList:
    if (i >= Average):
        print(i)
        count = count + 1
print(count, "are the number which are above the average of", round(Average,0))