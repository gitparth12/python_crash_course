def sum_natural_num(n: int):
    # base case
    if n <= 1:
        return n
    # recursive case
    else:
        return n + sum_natural_num(n - 1)
