"""
3 a) Reverse sentence

This function takes a sentence as an input, reverses the order of the words in
the sentence, and returns the result as a string with the first letter
capitalized and a period at the end.

The function first converts the input sentence to lowercase using the lower
method, removes any periods using the replace method, and then splits the
sentence into words using the split method. The words are then reversed using
the slicing notation [::-1], and joined together with spaces using the join
method.

The resulting reversed sentence is then capitalized using string slicing,
with the first letter converted to uppercase, and the rest of the string
concatenated using the + operator. Finally, a period is added to the end of the
sentence string, and the result is returned.
"""
def reverse_sentence(sentence):
    reversed_sentence = " ".join(sentence.lower().replace('.', '') \
        .split()[::-1])
    return reversed_sentence[0].upper() + reversed_sentence[1:] + '.'

# print(reverse_sentence("Never gonna give you up."))
"""
3 b) Character swapping

This function manipulates an input string by modifying the order of its
characters according to certain rules.

The function begins by initializing an empty list called
output_character_chains, which will store the modified character chains.

The function then iterates over each substring in the input string, which are
delimited by spaces, using the split method.

For each substring, the function checks its length. If the length is greater
than 1, the function applies a manipulation rule to the substring. If the length
is 1, the substring is added to the output list unchanged.

The manipulation rule depends on whether the length of the substring is odd or
even. If the length is odd, the function reverses the order of the characters
in the substring, except for the first and last characters, which are swapped.
If the length is even, the function splits the substring in half and inserts a
space in the middle.

Finally, the function joins the modified substrings back into a single string
using the join method and returns the result.
"""
def manipulate_string(string):
    output_character_chains = []
    for character_chain in string.split():
        if len(character_chain) > 1:
            if len(character_chain) % 2:
                output_character_chains.append(character_chain[-1] + \
                    character_chain[1:-1] + character_chain[0])
            else:
                output_character_chains.append(character_chain[ \
                    :len(character_chain) // 2] + ' ' + character_chain[ \
                    len(character_chain) // 2:])
        else:
            output_character_chains.append(character_chain)
    return ' '.join(output_character_chains)


# print(manipulate_string("1 12 123 1234 12345 123456 1234567 12345678" + \
#   "123456789"))