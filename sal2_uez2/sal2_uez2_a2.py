"""
2 a) File I/O

This function takes a file path as an input and reads the contents of the file
using the open function. It then removes any newline characters and spaces from
the text using the replace method, and returns the resulting string.

In short, the read_text_file function reads a text file and returns its
contents as a single, continuous string without any newline characters or
spaces.
"""
def read_text_file(path):
    with open(path) as input_file:
        return input_file.read().replace('\n', '').replace(' ', '')

"""
2 b) frequency analysis

This function takes a text string as input and analyzes it by counting the
occurrences of each character in the string.

The function initializes an empty dictionary called occurrences to store the
character counts. It then iterates over each character in the input string,
converting it to lowercase for case-insensitive analysis.

For each character, the function checks if it already exists in the occurrences
dictionary. If it does, the function increments the count of the character in
the dictionary. If not, the function adds the character to the dictionary with
a count of 1.

Finally, the function returns the occurrences dictionary containing the counts
of each character in the input text string.
"""
def anaylze_text(text):
    occurences = {}
    for character in text.lower():
        if character in occurences:
            occurences[character] += 1
        else:
            occurences[character] = 1
    return occurences

# print(anaylze_text("..bbAA..aaaa..ÖöÖö..ÖÖÖÖ..ccCC..BBBBcccc..AAaaAA.."))


"""
2 c) analysis of text-file

This code section reads the contents of a text file using the read_text_file
function, and then analyzes the text using the anaylze_text function.

The analyzed_text variable is assigned a dictionary containing the character
counts of the input text.

The analyzed_text_sorted variable is assigned a list of tuples containing the
character counts sorted in ascending order, using the sorted function and a
lambda function that sorts by the second element of each tuple.

The code then prints the five most common characters in the input text, by
iterating over the last five elements of the sorted list in reverse order and
printing each character and its count in a formatted string.
"""
text_file_string = read_text_file("text_to_analyze.txt")
analyzed_text = anaylze_text(text_file_string)
analyzed_text_sorted = sorted(analyzed_text.items(), key=lambda x:x[1])

print("The five most common characters are:")
for i in analyzed_text_sorted[:-5:-1]:
    print(f"'{i[0]}' ({i[1]})")

"""
2 d) Big-O-Analyze - Memory Complexity

The memory complexity of "analyze_text(text)" is O(k), where k is the number of
unique characters in the input text.
This is because the size of the dictionary is directly proportional to the size
of unique characters in the input text.
"""

