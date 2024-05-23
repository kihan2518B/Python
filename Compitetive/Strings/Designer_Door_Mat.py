

Input = input().split()
m,n = int(Input[0]),int(Input[1])
p = ".|."
# Upper Triangle
for i in range(int(m / 2)):
    print((p*((i * 2) + 1)).center(n,"-"))

# Middle Line
print("WELLCOME".center(n,"-"))

# Lower Triangle
for i in range(int((m / 2)-1), -1, -1):
    print((p*((i * 2) + 1)).center(n,"-"))
