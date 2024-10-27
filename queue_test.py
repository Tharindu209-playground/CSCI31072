class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None
    
    def print_queue(self):
        return self.items

def ticketing_system(customers):
    queue = Queue()
    for customer in customers:
        queue.enqueue(customer)
    
    print("Serving customers in order:")
    while not queue.is_empty():
        print(f"Serving: {queue.dequeue()}")
        print("Queue after serving:", queue.print_queue())

# Sample Usage
customers = ["Alice", "Bob", "Charlie"]
ticketing_system(customers)
