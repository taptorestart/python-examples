
def factorial(n):
    print(n)
    if n - 1 > 1:
        return n * factorial(n - 1)
    else:
        return n * 1


if __name__ == '__main__':
    factorial_result = factorial(5)
    print(factorial_result)


'''
# Result
5
4
3
2
120
'''
