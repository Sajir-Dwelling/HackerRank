

N,X = list(map(int,input().split()))
marks = []
for _ in range(X):
    row = list(map(float,input().split()))
    marks.append(row)

student_marks = list(zip(*marks))


for student in student_marks:
    average = sum(student)/X
    print("{:.1f}".format(average))