class Queue:
   def __init__(self):
       self.queue = []

   def is_empty(self):
       return len(self.queue) == 0

   def enqueue(self, item):
       self.queue.append(item)

   def dequeue(self):
       if not self.is_empty():
           return self.queue.pop(0)
       else:
           print("Queue is empty")
           return None

def breadth_first_search_for_file(root, target_file):
    queue = Queue()
    queue.enqueue((root, ""))

    while not queue.is_empty():
        current_node, current_path = queue.dequeue()
        current_path += current_node.name + "/"

        if current_node.name == target_file:
            return current_path

        for child in current_node.children:
            queue.enqueue((child, current_path))

    return None

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

root = TreeNode("C:")
documents = TreeNode("Documents")
root.add_child(documents)
documents.add_child(TreeNode("Homework.docx"))
documents.add_child(TreeNode("Report.docx"))

pictures = TreeNode("Pictures")
root.add_child(pictures)
pictures.add_child(TreeNode("Summer.jpg"))
pictures.add_child(TreeNode("Winter.jpg"))

root.add_child(TreeNode('secret.key'))


file_path = breadth_first_search_for_file(root, 'Report.docx')
if file_path: # Если файл был найден
    print(file_path[:-1])
# C:/Documents/Report.docx