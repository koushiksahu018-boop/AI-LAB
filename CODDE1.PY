# WAP TO PRINT DFS OF A TREE USING PYTHON

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def dfs(node):
    if node is None:
        return
    print(node.data, end=" ")
    dfs(node.left)
    dfs(node.right)
    