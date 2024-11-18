class TreeNode:
   def __init__(self, value):
       self.value = value
       self.children = []

   def add_child(self, child):
       self.children.append(child)

root = TreeNode(1)
child1 = TreeNode(2)
root.add_child(child1)

child2 = TreeNode(3)
root.add_child(child2)

child3 = TreeNode(4)
root.add_child(child3)

child4 = TreeNode(5)
child1.add_child(child4)

