def minion_game(string):
    # allSubstrings = []
    StuartScore = 0
    KevinScore = 0
    for index, char in enumerate(string):
        if char in "AEIOU":
            KevinScore += len(string) - index
        else:
            StuartScore += len(string) - index

    if StuartScore > KevinScore:
        print("Stuart",StuartScore)
    elif StuartScore == KevinScore:
        print("Draw")
    else:
        print("Kevin",KevinScore)

s = input()
minion_game(s)



