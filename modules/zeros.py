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


if __name__ == "__main__":
    print('У факториала({}) -  {} нулей в конце!'.format(30, zeros(30)))