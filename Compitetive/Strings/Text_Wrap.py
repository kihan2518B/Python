import textwrap

def wrap(string, max_width):
    finalString = ""
    for i in range(len(string)):
        if i != 0 and i % max_width ==0:
            finalString += "\n"
        finalString += string[i]
    return finalString

    # Using textwrap
    # wrapper = "\n".join(textwrap.wrap(string, max_width))
    # return wrapper

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)