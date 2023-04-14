from primes.primality_tests import isPrime, isPrime1


def bruteForcePrimesUpToN(n):
    result = []

    for i in range(2, n+1):
        if isPrime1(i):
            result.append(i)
    return result


def eratosfenSieve(n):
    arr = [True for i in range(n+1)]
    result = []
    for i in range(2, n+1):
        if not arr[i]:
            continue
        # if isPrime1(i):
        for j in range(i*2, n+1, i):
            arr[j] = False
    for i in range(n+1):
        if arr[i]:
            if not isPrime1(i):
                print(i)
            result.append(i)
    return result[2:]
