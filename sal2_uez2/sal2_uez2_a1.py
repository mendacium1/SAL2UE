"""
1 a) Cocktail Shaker Sort

The cocktail_shaker_sort function takes an unsorted list as input, and returns
the list sorted in ascending order using the cocktail shaker sort algorithm.
The algorithm works by repeatedly iterating through the list in both forward
and backward directions, swapping adjacent elements that are in the wrong order
until no more swaps are needed.

The function initializes a flag variable to True, indicating that swaps may be
necessary, and enters a while loop that continues until no more swaps are made.

In each iteration of the loop, the function first iterates through the list
from left to right, swapping adjacent elements that are in the wrong order, and
then iterates through the list from right to left, swapping adjacent elements
that are in the wrong order.

If no swaps are made in either direction, the function returns the sorted list.
"""

def cocktail_shaker_sort(a_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(a_list) - 1):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                swapped = True
        if not swapped:
            break
        else:
            swapped = False
        for i in range(len(a_list) - 2, 0, -1):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i] 
                swapped = True
    return a_list

"""
1 b) File I/O

This code section reads an unsorted list of numbers from a file called
"unsorted_list.txt" using the open function and stores it as a list of integers
called unsorted_number_list.

Then, the cocktail_shaker_sort function is called to sort the
unsorted_number_list, and the sorted list is stored as sorted_number_list.

Finally, the sorted list is written to a new file called "sorted_list.txt"
using the open function with the "w" flag to indicate that the file should be
opened for writing, and the write method is used to write the sorted list to
the file as a comma-separated string, with each number on a new line. The map
function is used to convert each integer in the sorted list to a string, and
the join method is used to join the list of strings with commas and newlines.
"""
with open("unsorted_list.txt") as input_file:
    unsorted_number_list = [int(x) for x in input_file.read().replace(',',"") \
        .replace("\n"," ").split()]
sorted_number_list = cocktail_shaker_sort(unsorted_number_list)

with open("sorted_list.txt", "w") as output_file:
    output_file.write(",\n".join(map(str, sorted_number_list)))


"""
1 c) time complexity

The worst-case time complexity of the cocktail_shaker_sort algorithm is O(n^2),
where "n" is the number of elements in the input list. This is because in the
worst case, the algorithm will have to make n-1 passes through the list in each
direction, and in each pass it may have to compare and swap up to n-1 adjacent
elements. Therefore, the total number of comparisons and swaps will be
proportional to n^2.
"""

