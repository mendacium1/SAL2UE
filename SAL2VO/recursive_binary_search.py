#!/usr/bin/python3


def binary_search(lst, low, high, value):
    middle = (low + high) // 2
    if value == lst[middle]:
        return middle
    elif low == high:
        return None
    elif value >  lst[middle]:
        return binary_search(lst, middle + 1, high, value)
    else:
        return binary_search(lst, low, middle - 1, value)

# sorted list of 9 prime numbers for demo
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

last_idx = len(primes) - 1
idx = binary_search(primes, 0, last_idx, 5)
print(f"idx? {idx}")