def merge_the_tools(string, k):
    listOft = []
    for i in range(0,len(string),k):
        # print(string[i:i+k])
        listOft.append(string[i:i+k])
    # print(listOft)
    for i in listOft:
        u = ""
        for j in i:
            if j not in u:
                u += j
        print(u)

string, k = input(), int(input())
merge_the_tools(string, k)
