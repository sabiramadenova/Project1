def memoize(func):
    memo = {}

    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]

    return wrapper

# annotation
@memoize
def fibonacci(n):
    # print(f"for fib({n})")
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(10)
print("Fibonacci(10) with memoization:", result)
