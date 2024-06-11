from queue import LifoQueue

# inisialisasi stack

stack = LifoQueue(maxsize=5)

stack.put("Gacoan")
stack.put("Nasi Kuning")
stack.put("Lengko")
stack.put("Ketoprak")
stack.put("Mie Ayam Sultan")

#panggil stack
print(stack.queue)

# stack.get()
# print(stack.queue)



print(stack.empty())
print(stack.full())