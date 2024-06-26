class Data:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, tambah):
        self.queue.append(tambah)
    
    def dequeue(self):
        self.queue.pop(0)
    
    def front(self):
        return self.queue[0]
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return "Ya, data kosong"
        else:
            return f"Terdapat {len(self.queue)} data"