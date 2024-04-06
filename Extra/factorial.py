
n = int(input())


def fact(k: int):
    ans = 1
    if k == 0:
        return 1
    else:
        for i in range(1, k+1):
            ans *= i
        return ans


print(fact(n))


# USD to INR
def USD_to_INR(usd):
    return usd * 83.59

print(USD_to_INR(2))