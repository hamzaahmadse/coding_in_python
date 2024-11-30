def candles(n):
    candles = [True] * n  # All candles are initially lit
    for i in range(1, n + 1):
        if i % 2 == 0:  # For each even i, toggle the state of each i-th candle
            for j in range(i - 1, n, i):
                candles[j] = not candles[j]
    return candles.count(True)  # Count the number of lit candles

# Testing the function with the given test cases
print(candles(1))  # Expected: 1
print(candles(2))  # Expected: 1
print(candles(42))  # Expected: 38
print(candles(0))  # Expected: 0
print(candles(5))  # Expected: 4
