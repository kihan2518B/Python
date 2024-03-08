#You are given a positive integer . Print a numerical triangle of height N-1
# like the one below:
# 1
# 22
# 333
# ....
# You have to complete task in just two lines

for i in range(1,int(input())):
    print((10**i // 9) * i)