def sieve_of_eratosthenes(number):
    prime_numbers = [True for _ in range(number + 1)]
    square_root = int(number**0.5)
    print(f"square_root: {square_root}")

    for i in range(2, square_root + 1):
        print()
        print(f"i: {i}")
        if prime_numbers[i]:
            for j in range(i + i, number + 1, i):
                print(f"j: {j}")
                prime_numbers[j] = False
    result = []
    for i in range(2, number + 1):
        if prime_numbers[i]:
            result.append(i)
    return result


if __name__ == "__main__":
    prime_number_list = sieve_of_eratosthenes(10)
    print(prime_number_list)


"""
# Result
square_root: 3

i: 2
j: 4
j: 6
j: 8
j: 10

i: 3
j: 6
j: 9
[2, 3, 5, 7]
"""
