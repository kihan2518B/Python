

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

marks = student_marks.get(query_name)
Sum = sum(marks)
a = Sum/len(marks)
print(format(a, '.2f'))