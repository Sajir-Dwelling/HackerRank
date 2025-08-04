
import numpy

n, m = list(map(int,input().split()))

A = []
for _ in range(n):
    row = list(map(int,input().split()))
    A.append(row)

B = []
for _ in range(n):
    row = list(map(int,input().split()))
    B.append(row)

A = numpy.array(A)
B = numpy.array(B)

print(A+B)
print(A-B)
print(A*B)
#print(A//B)
C = numpy.divide(A,B)
C = numpy.array((C),int)
print(C)
print(A%B)
print(A**B)
