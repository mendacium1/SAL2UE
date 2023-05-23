from collections import deque

# used for popleft (receiving node from the front of the queue - not possible with lists)

rooted_example_tree = [
    [1, 2, 3],  # 0
    [4, 5],  # 1
    [6],  # 2
    [7, 8],  # 3
    [],  # 4
    [9, 10],  # 5
    [11],  # 6
    [],  # 7
    [12],  # 8
    [],  # 9
    [],  # 10
    [],  # 11
    [],  # 12
]


# 1 a.) breadth_first_search
def breadth_first_search(rooted_tree, target_node):
    """
    Perform breadth-first search on a rooted tree and print every visited node, highlighting the
    target node.

    Args:
        rooted_tree (list): A list representing the rooted tree structure.
            Each element of the list represents a node, and the value of each element is a list of
            its neighbors.
            The index of each element corresponds to the node's unique identifier.
        target_node (int): The identifier of the target node to be highlighted in the printed
        output.

    Returns:
        None

    """
    visited = set()  # Set to keep track of visited nodes
    queue = deque()  # Queue to store nodes for breadth-first traversal
    queue.append(0)  # Starting from the root node (index 0)

    while queue:
        current_node = queue.popleft()  # Retrieve the node from the front of the queue
        visited.add(current_node)  # Mark the current node as visited

        if current_node == target_node:
            print(f"Found target node {current_node} using breadth-first search.")
        else:
            print(f"Visiting node {current_node} using breadth-first search.")

        neighbors = rooted_tree[current_node]
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)


print("\nbreadth_first_search:")
breadth_first_search(rooted_example_tree, 10)


# 1 b.) depth_first_search
def depth_first_search(rooted_tree, target_node):
    """
    Perform depth-first search (DFS) on a rooted tree and print visited nodes,
    highlighting the target node.

    Args:
        rooted_tree (list): A list representing the rooted tree structure.
                            Each index corresponds to a node, and the value at
                            that index is a list of its neighboring nodes.
                            The root node is assumed to be at index 0.
        target_node (int): The node to search for within the tree.

    Returns:
        None: The function does not return a value. It prints the visited nodes.
    """

    def dfs_helper(node, visited):
        """
        Recursive helper function for depth-first search.

        Args:
            node (int): The current node being visited.
            visited (set): A set containing the visited nodes.

        Returns:
            None: The function does not return a value. It modifies the visited set.
        """
        visited.add(node)
        if node == target_node:
            print(f"Found target node {node} using depth-first search.")
        else:
            print(f"Visiting node {node} using depth-first search.")

        for neighbor in rooted_tree[node]:
            if neighbor not in visited:
                dfs_helper(neighbor, visited)

    visited_nodes = set()
    dfs_helper(0, visited_nodes)  # Start DFS from the root (node 0)


print("\ndepth_first_search:")
depth_first_search(rooted_example_tree, 10)


# 1 c.) File I/O
def read_rooted_tree(filepath):
    rooted_tree = []
    with open(filepath, 'r') as file:
        for line in file:
            nodes = line.replace(',', '').split()
            if len(nodes) == 0:
                rooted_tree.append([])
            else:
                rooted_tree.append([int(node) for node in nodes])
    return rooted_tree


filename = "rooted_tree.txt"
rooted_tree_from_file = read_rooted_tree(filename)
print("\nrooted_tree_from_file - breadth_first_search:")
breadth_first_search(rooted_tree_from_file, 30)
print("\nrooted_tree_from_file - depth_first_search:")
depth_first_search(rooted_tree_from_file, 30)
