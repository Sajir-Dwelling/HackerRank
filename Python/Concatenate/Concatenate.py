import numpy


n,m,p = map(int,input().split())

N = numpy.array([input().split() for _ in range(n)],int)
M = numpy.array([input().split() for _ in range(m)],int)

print(numpy.concatenate((N, M), axis=0))