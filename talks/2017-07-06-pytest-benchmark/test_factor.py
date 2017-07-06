import math

def factor(n):
    return [x for x in range(2, n) if n % x == 0]

def factor_sqrt(n):
    factors = set()
    for x in range(2, int(math.sqrt(n) + 1)):
         if n % x == 0:
             factors.add(x)
             factors.add(n // x)
    return list(sorted(factors))

def test_factor(benchmark):
    result = benchmark(factor, 1001)
    assert result == [7, 11, 13, 77, 91, 143]
