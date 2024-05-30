

records = list()

AllScores = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])
    AllScores.add(score)

AllScores = list(AllScores)
AllScores.sort()

# print(AllScores[1])
# print(records)
sol = list()
for i in records:
    if AllScores[1] in i:
        sol.append(i[0])
sol.sort()
print("\n".join(sol))