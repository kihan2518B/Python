def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        newString = ""
        for j in range(len(sub_string)):
            newString += string[i+j]
        print(newString)
        if sub_string == newString:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)