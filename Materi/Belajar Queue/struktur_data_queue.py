queue = []

# menambah data
def enqueue(item):
    queue.append(item)

# menghapus data
def dequeue():
    queue.pop(0)

# mengecek data pertama
def front():
    if len(queue) < 1:
        return "Data kosong"
    else:
        return queue[0]
        
# mengecek data akhir        
def tail():
    return queue[-1]

# mengecek data
def isEmpty():
    if len(queue) == 0:
        return "Queue Kosong"
    else:
        return "ada Queue"

# menghitung data
def size():
    return len(queue)

enqueue("Dimas")
enqueue("Dandi")
enqueue("Djarot")
enqueue("Denis")

# pemanggilan fungsi
dequeue()

print("Data pertama: ", front())
print("Data terakhir: ", tail())
print("Apakah datanya ada?: ", isEmpty())
print(queue)