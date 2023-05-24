from queue import PriorityQueue


# 2 a.) Adapted frequency analysis
def read_text_file(path):
    """
    Reads the content of a text file.

    Args:
        path (str): The path to the text file.

    Returns:
        str: The content of the text file.
    """
    with open(path, "r", encoding="utf-8") as input_file:
        return input_file.read()


print("\033[96mTest output for 2 a.):\033[0m\n" + read_text_file("text_to_analyze.txt"))


def analyze_text(text):
    """
    Analyzes the given text and returns the occurrences of each character.

    Args:
        text (str): The text to be analyzed.

    Returns:
        dict: A dictionary containing each character as key and its occurrence count as value.
    """
    occurrences = {}
    for character in text:
        if character in occurrences:
            occurrences[character] += 1
        else:
            occurrences[character] = 1
    return occurrences


test_text = read_text_file("text_to_analyze.txt")
print("\033[96mTest output for 2 a.):\033[0m\n" + str(analyze_text(test_text)))


# 2 b.) Huffman Tree
class TreeNode:
    """
    Simple class to represent a node in a huffman tree. (Binary Tree)
    __lt__ and __gt__ are overriden to make objects of the class comparable to other
    objects.
    Attributes:
    left: A child TreeNode object to the left
    right: A child TreeNode object to the right
    """

    def __init__(self, left, right):
        self.left = left  # left child
        self.right = right  # right child

    def __lt__(self, any_object):
        """
        This method overrides the < operation. If two entries in a priority queue
        (tuple) have the same priority, the implementation tries to compare the
        second two values. Since the implementation does not know how to compare a string
        object with a TreeNode object, it raises an exception. This function returns the
        value 0 when a Treenode object is compared with any other object in a "lesser than"
        operation.
        """
        return 0

    def __gt__(self, any_object):
        """
        This method overrides the > operation. If two entries in a priority queue
        (tuple) have the same priority, the implementation tries to compare the
        second two values. Since the implementation does not know how to compare a string
        object with a TreeNode object, it raises an exception. This function returns the
        value 0 when a Treenode object is compared with any other object in a "greater
        than" operation.
        """
        return 0


def create_huffman_tree(char_freq):
    """
    Creates a Huffman tree based on character frequencies.

    Args:
        char_freq (dict): A dictionary containing characters as keys and their frequencies as
        values.

    Returns:
        TreeNode: The root node of the created Huffman tree.
    """
    my_priority_queue = PriorityQueue()
    for key, value in char_freq.items():
        my_priority_queue.put((value, TreeNode(key, None)))
    while my_priority_queue.qsize() > 1:
        priority1, node1 = my_priority_queue.get()
        priority2, node2 = my_priority_queue.get()
        combined_priority = priority1 + priority2
        combined_node = TreeNode(node1, node2)
        my_priority_queue.put((combined_priority, combined_node))

    return my_priority_queue.get()


test_freq_analysis = analyze_text(test_text)
test_root_node = create_huffman_tree(test_freq_analysis)
print("\033[96mTest output for 2 b.):\033[0m\n" + str(test_root_node))


# 2 c.) Huffman Code
def create_huffman_code(node, huffman_code, prefix=''):
    """
    Creates Huffman codes for each character in the Huffman tree.

    Args:
        node (TreeNode): The current node being traversed in the Huffman tree.
        huffman_code (dict): A dictionary to store the Huffman codes.
        prefix (str): The prefix code generated during traversal.

    Returns:
        None
    """
    if node is None:
        return

    if isinstance(node, str):
        huffman_code[node] = prefix
        return

    create_huffman_code(node.left, huffman_code, prefix + '0')
    create_huffman_code(node.right, huffman_code, prefix + '1')


test_huffman_code = {}
create_huffman_code(test_root_node[1], test_huffman_code, '')
print("\033[96mTest output for 2 c.):\033[0m\n" + str(test_huffman_code))


# 2 d.) Text encoding
def encode_text(huffman_code, text):
    """
    Encodes the given text using Huffman codes.

    Args:
        huffman_code (dict): A dictionary containing Huffman codes for each character.
        text (str): The text to be encoded.

    Returns:
        str: The encoded text.
    """
    output = ""
    for character in text:
        if character in huffman_code:
            output += huffman_code[character]
        else:
            output += character
    return output


print("\033[96mTest output for 2 d.):\033[0m\n" + str(encode_text(test_huffman_code,
                                                                  test_text)))

# 2 e.) Functiontest
print("\033[92mFunctiontest\033[0m")
# read in "text_to_analyze.txt"
functiontest_content_text = read_text_file("text_to_analyze.txt")
# create frequency analysis of input text
functiontest_freq_analysis = analyze_text(functiontest_content_text)
# create a huffman tree with the frequency analysis
functiontest_huffman_tree = create_huffman_tree(functiontest_freq_analysis)
# create a huffman code with the huffman tree
functiontest_huffman_code = {}
create_huffman_code(functiontest_huffman_tree[1], functiontest_huffman_code)
# encode the text from "text_to_analyze.txt" with the functiontest_huffman_code and print it
functiontest_encoded_text = encode_text(functiontest_huffman_code, functiontest_content_text)
print(functiontest_encoded_text)


# 2 f.) Text decoding
def decode_text(huffman_code, encoded_text):
    """
    Decodes the given encoded text using Huffman codes.

    Args:
        huffman_code (dict): A dictionary containing Huffman codes for each character.
        encoded_text (str): The text to be decoded.

    Returns:
        str: The decoded text.
    """
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        for character, code in huffman_code.items():
            if current_code == code:
                decoded_text += character
                current_code = ""
                break
    return decoded_text


test_decoded_text = decode_text(functiontest_huffman_code, functiontest_encoded_text)
print("\033[96mTest output for 2 f.):\033[0m\n" + test_decoded_text)
