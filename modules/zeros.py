import time


def zeros(n):
    """calculate the number of trailing zeros
    in a factorial of a given number"""
    factorial = count_zero = 1
    while n > 1:
        factorial *= n
        n -= 1
    while factorial % 10 ** count_zero == 0:
        count_zero += 1
    return count_zero - 1


# Algorithm for Counting trailing zeros in factorial of a number.
# So in general, if you want to count trailing zero in factorial of a number,
# you have to,
#
# 1. Divide the number by 5, to find out how much 5 factors are present, then,
# 2. Divide the number by 25 to find out how many times 25 are present
# in a number as it will add extra 5 to number then,
# 3. Divide the number by 125 to find out how many times 125 are present
# in a number as it will add extra 5 to number and so on.


def zeros_optimized(n):
    '''Optimized calculate the number of trailing zeros
    in a factorial of a given number'''
    i = 1
    count_zero = 0
    while n >= i:
        i *= 5
        count_zero += int(n / i)
    return count_zero


if __name__ == "__main__":
    n = 50
    t1 = t2 = 0
    for i in range(n):
        start1 = time.perf_counter()
        z = zeros(1000)
        end1 = time.perf_counter()
        t1 += end1 - start1

    for i in range(n):
        start2 = time.perf_counter()
        z = zeros_optimized(1000)
        end2 = time.perf_counter()
        t2 += end2 - start2

    print('У факториала({}) -  {} нулей в конце!'.format(1000, z))
    print('Среднее ремя выполнения: ')
    print('\tzeros function = ', t1 / n)
    print('\tzeros_optimized function = ', t2 / n)
    print('time gain:', t1 - t2)
