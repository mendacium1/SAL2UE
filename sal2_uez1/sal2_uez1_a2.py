from timeit import timeit
from random import sample, randint

def linear_search(list_of_numbers, number):
    """Checks if the given number is in the given list by iterating over all list-elements

    Args:
        list_of_numbers: the list of numbers
        number: the number to search for
    Returns:
        True/False if number is in list
    """
    for num in list_of_numbers:
        if num == number:
            return True
    return False

def search_using_in(list_of_numbers, number):
    """Checks if the given number is in the given list by using the "in" keyword in python

    Args:
        list_of_numbers: the list of numbers
        number: the number to search for
    Returns:
        True/False if number is in list
    """
    return number in list_of_numbers

def binary_search(sorted_list_of_numbers, number):
    """Checks if the given number is in the given list by doing a binary search

    Args:
        list_of_numbers: the list of numbers
        number: the number to search for
    Returns:
        True/False if number is in list
    """
    low = 0
    high = len(sorted_list_of_numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list_of_numbers[mid] == number:
            return True 
        elif sorted_list_of_numbers[mid] < number:
            low = mid + 1
        else:
            high = mid - 1

    return False

# generate a list of 5,000 random integers between 0 and 9,999
rand_list = sample(range(0,10000), 5000)
# sort the randomized list using python's native 'sorted()' function
sorted_list = sorted(rand_list)
# generate a random integer between 0 and 9,999
num = randint(0, 10000)
# number of times the statement is run by timeit
iterations = 20000


print(f"Searching for number '{num}' in a list of 5,000 random integers")
print(f"{timeit(lambda: linear_search(sorted_list, num), number=iterations):,.4f}" +
    f" seconds were needed to run {iterations} search iterations using linear search.")
print(f"{timeit(lambda: search_using_in(sorted_list, num), number=iterations):,.4f}" +
    f" seconds were needed to run {iterations} search iterations using Python's 'in' keyword")
print(f"{timeit(lambda: binary_search(sorted_list, num), number=iterations):,.4f}" +
    f" seconds were needed to run {iterations} search iterations using binary search.")

"""
e.)
Die Laufzeitkomplexität von linear_search beträgt O(n) (im worst case), da über jedes Element
iteriert wird.
Die Laufzeitkomplexität von search_using_in beträgt O(n), da über jedes Element iteriert wird.
-> https://wiki.python.org/moin/TimeComplexity
Die Laufzeitkomplexität von binary_search beträgt O(log n), da bei jedem Durchlauf die Liste in
zwei Hälften geteilt wird.

Die Laufzeit schwankt so stark, da die Zahlen zufällig gewählt werden und so die Zahl früh, spät
oder garnicht gefunden werden kann.
"""
