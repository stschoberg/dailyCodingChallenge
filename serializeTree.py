# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.
#
# For example, given the following Node class:

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Pre-oder traversal
def serialize(node):
    return serializeHelper(node, [])


def serializeHelper(node,lst):
    if(node.left == None):
        lst.append(None)
    else:
        serializeHelper(node.left, lst.append(node.val))
    if(node.left == None):
        lst.append(None)
    else:
        serializeHelper(node.right, lst.append(node.val))
