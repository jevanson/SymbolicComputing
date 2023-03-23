import math
import timeit

@staticmethod
def pritchards_wheel_sieve(N):
    # N >= 5
    p = 3
    length = 2
    S = [1]
    P = [2]

    while p*p <= N or length < N:
        l = min(p*length, N)
        y = length + 1
        delta = 0
        while y <= l:
            S.append(y)
            delta = delta + 1
            y = length + S[delta]

        length = l
        S = [x for x in S if not x % p == 0]
        if p not in P:
            P.append(p)
        
        p = S[1]

    primes = S + P
    primes = [x for x in primes if not x == 1]

    return primes

SETUP_CODE = '''
from __main__ import pritchards_wheel_sieve
'''

TEST_CODE = '''
pritchards_wheel_sieve(1000)
'''

if __name__ == '__main__':
    print(timeit.timeit(setup = SETUP_CODE, stmt=TEST_CODE,number=10000))
    #result = pritchards_wheel_sieve(100)
    #result.sort()
    #print("result: " + str(result))