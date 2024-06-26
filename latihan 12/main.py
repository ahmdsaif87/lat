from stack import Data

nambah = Data()
nambah.enqueue("Vario")
nambah.enqueue("Mio Mirza")
nambah.enqueue("Supra X")
nambah.dequeue()
print(f"data yang ada = {nambah.queue}")
print(f"data yang pertama ditambahkan = {nambah.front()}")
print(nambah.isEmpty())
