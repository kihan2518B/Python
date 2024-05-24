# from 1 to n print Decimal Octal Hexadecimal (capitalized) Binary
number = int(input())


def print_formatted(n):
    width = len(bin(n)) - 2  # -2 to remove the '0b' prefix
    for i in range(1,n+1):
        print(str(i).rjust(width), oct(i).split('o')[1].rjust(width), hex(i).split("x")[1].upper().rjust(width), bin(i).split('b')[1].rjust(width))


print_formatted(number)