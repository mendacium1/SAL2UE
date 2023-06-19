print("Termin 6")

class BinaryTree(object):
    def __init__(self, key):
        self.key = key # Wert
        self.left = None # for BinaryTree
        self.right = None # for BinaryTree

    def preorder(self):
        print(self.key)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


class BinarySearchTree(BinaryTree):
    def search(self, key):
        if key == self.key:
            return self
        elif key < self.key:
            if self.left:
                return self.left.search(key)
        else:
            # key > slf.key
            if self.right:
                return self.right.search(key)
        return None


n13 = BinarySearchTree(13)
n5 = BinarySearchTree(5)
n19 = BinarySearchTree(19)
n2 = BinarySearchTree(2)
n11 = BinarySearchTree(11)
n17 = BinarySearchTree(17)
n23 = BinarySearchTree(23)
n3 = BinarySearchTree(3)
n7 = BinarySearchTree(7)

n13.left = n5
n13.right = n19
n5.left = n2
n5.right = n11
n19.left = n17
n19.right = n23
n2.right = n3
n11.left = n7

n13.preorder()

node = n13.search(667)
print(node.key, "gefunden")