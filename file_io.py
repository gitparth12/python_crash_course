
# # Better way
# for line in open('data.csv'):
#     nums = line.split(',')[2: -2]
#     nums = list(map(int, nums))
#     print(f"{sum(nums)}: ", end='')
#     print(*nums)

# # packing lists
# def my_sum(*args):
#     return sum(args)

if __name__ == "__main__":
    # naïve way
    f = open('data.csv', 'r')
    # f.read()
    # f.readline()
    # f.readlines()
    for line in f.readlines():
        # improvement: slicing
        nums = line.split(',') # .strip()

        total = 0
        for num in nums:
            try:
                total += int(num)
            except ValueError:
                continue

        print("{}: {}".format(total, ' '.join(nums)))