@staticmethod
def bengallouns_inc_sieve(N):
	leastprimes = [0] * (N + 1)
	primes = []

	for i in range(2,N+1):
		if leastprimes[i] == 0:
			leastprimes[i] = i
			primes.append(i)

		j = 0
		while i*primes[j] <= N:
			leastprimes[i*primes[j]] = primes[j]

			if primes[j] == leastprimes[i]:
				break

			j = j + 1

	return primes

if __name__ == '__main__':
	result = bengallouns_inc_sieve(100)
	print(result)