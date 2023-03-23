import math
import timeit

@staticmethod
def eratosthenes_sieve(N):
	primes = []

	A = [True] * (N+1)

	for i in range(2, int(math.sqrt(N)) + 1):
		if A[i]:
			j = 0
			while i*i+j*i <= N:
				A[i*i+j*i] = False
				j = j + 1

	for i in range(2,N+1):
		if A[i]:
			primes.append(i)

	return primes

SETUP_CODE = '''
from __main__ import eratosthenes_sieve
'''

TEST_CODE = '''
eratosthenes_sieve(1000)
'''

if __name__ == '__main__':
    print(timeit.timeit(setup = SETUP_CODE, stmt=TEST_CODE,number=10000))
    #print(result)