def fibonacci(n: int):
    # base case
    if n == 0 or n == 1:
        return n
    # recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for i in range(5):
        print(fibonacci(i))
