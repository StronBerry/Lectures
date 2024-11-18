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


queue = Queue()
queue.enqueue(['FleurBurger 5000', 'Golden Opulence Sundae', 'Zillion Dollar Lobster Frittata'])
queue.enqueue(['Golden Opulence Sundae', 'Sushi Del Oriente'])
queue.enqueue(['Pizza Louis XIII', 'Macaroons Haute Couture'])

print(queue.dequeue())  # ['FleurBurger 5000', 'Golden Opulence Sundae', 'Zillion Dollar Lobster Frittata']
print(queue.dequeue())  # ['Golden Opulence Sundae', 'Sushi Del Oriente']
print(queue.dequeue())  # ['Pizza Louis XIII', 'Macaroons Haute Couture']
# Queue is empty
print(queue.dequeue())  # None