# Binary Tree

class Tree(object):

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        ret = ""
        return str(self.data)

def Depth(node):
    if node is None:
        return 0

    lDepth = Depth(node.left)
    rDepth = Depth(node.right)

    if lDepth > rDepth:
        return lDepth + 1
    else:
        return rDepth + 1

def Height(node):
    if node is None:
        return 0
    q = []

    q.append(node)
    height = 0

    while(True):
        nodeCount = len(q)
        if nodeCount == 0:
            return height

        height += 1

        while(nodeCount > 0):
            node = q[0]
            q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

            nodeCount -= 1

def countnodes(node):
    if node is None:
        return 0
    return (1 + countnodes(node.left) + countnodes(node.right))

def is_complete(node, index, node_nos):
    if node is None:
        return True

    if index >= node_nos:
        return False

    return (is_complete(node.left, 2*index+1, node_nos)
        and is_complete(node.right, 2*index+1, node_nos)
          )


root = Tree(3)


root.left = Tree(4)
root.right = Tree(5)

root.left.left = Tree(6)
root.right.right = Tree(7)
root.left.left.left = Tree(8)

node_count = countnodes(root)
index = 0

print("Depth is %s" % Depth(root))
print("Height is %s" % Height(root))

if is_complete(root, index, node_count):
    print("Complete Binary tree")
else:
    print("Not a Complete Binary tree")
