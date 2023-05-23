from collections import deque
# used for popleft (receiving node from the front of the queue - not possible with lists)

rooted_tree = [
        [1, 2, 3],      #0
        [4, 5],         #1
        [6],            #2
        [7, 8],         #3
        [],             #4
        [9, 10],        #5
        [11],           #6
        [],             #7
        [12],           #8
        [],             #9
        [],             #10
        [],             #11
        [],             #12
]

# 1 a.) breadth_first_search
def breadth_first_search(rooted_tree, target_node):
    """
    Perform breadth-first search on a rooted tree and print every visited node, highlighting the target node.

    Args:
        rooted_tree (list): A list representing the rooted tree structure.
            Each element of the list represents a node, and the value of each element is a list of its neighbors.
            The index of each element corresponds to the node's unique identifier.
        target_node (int): The identifier of the target node to be highlighted in the printed output.

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
            print(f"[{current_node}]")  # Highlight the target node by enclosing it in square brackets
        else:
            print(current_node)

        neighbors = rooted_tree[current_node]  # Get the neighbors of the current node
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)  # Add the unvisited neighbor nodes to the queue for further traversal


breadth_first_search(rooted_tree, 10)
