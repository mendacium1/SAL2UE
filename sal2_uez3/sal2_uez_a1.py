from collections import deque

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

def breadth_first_search(rooted_tree, target_node):
    visited = set()
    queue = deque([(0, "")])

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        if node == target_node:
            print(f"Visiting node {node} using breadth_first_search.")
        else:
            print(f"Found target node {node} using breadth_first_search.")

        for child in rooted_tree[node]:
            if child not in visited:
                queue.append((child, path + str(node) + " -> "))

breadth_first_search(rooted_tree, 10)
