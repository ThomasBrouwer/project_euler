# Greedy algorithm, using nCr = (n-1)C(r-1) + (n-1)Cr, with nCn=nC0=1
import numpy
n_max, million = 100, 1000000
C = numpy.zeros((n_max+1, n_max+1))
for n in range(0,n_max+1):
	C[n,0], C[n,n] = 1, 1
for n in range(1,n_max+1):
	for r in range(1,n+1):
		C[n,r] = C[n-1,r-1] + C[n-1,r]
print len(C[numpy.where(C >= million)].flatten())