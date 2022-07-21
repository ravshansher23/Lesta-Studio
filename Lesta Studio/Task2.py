from collections import deque
from timeit import default_timer as timer
"""Первый класс, реализуемый с помощью модуля deque"""
class Fifo():
    fifo_list = deque(maxlen=10)

    def inserts(self, item):
        self.fifo_list.append(item)

    def past(self):
        return print(self.fifo_list.popleft())

start_time = timer()
r = Fifo()
r.inserts(4)
r.inserts('123')
r.inserts(111)
end_time = timer()
print(end_time - start_time)
print(r.fifo_list)
r.past()
print(r.fifo_list)
print()

"""Второй и третий класс, реализуемый с помощью методов списка(скорость их обработки меньше, при большом колличестве елементов списка)"""
class SimplePop:
    fifo_list = []
    def inserts(self, item):
        self.fifo_list.append(item)
        if len(self.fifo_list) > 10:
            self.fifo_list.pop(0)
    def past(self):
        return print(self.fifo_list.pop(0))
start_time = timer()
w = SimplePop()
w.inserts('1')
w.inserts('2')
w.inserts('3')
end_time = timer()
print(end_time - start_time)
print(w.fifo_list)
w.past()
print(w.fifo_list)
print()
class SimplePopTwo:
    fifo_list = []
    def inserts(self, item):
        self.fifo_list.append(item)
        if len(self.fifo_list) > 10:
            self.fifo_list.reverse()
            self.fifo_list.pop()
            self.fifo_list.reverse()
    def past(self):
        self.fifo_list.reverse()
        r = self.fifo_list.pop()
        self.fifo_list.reverse()
        return print(r)
start_time = timer()
s = SimplePopTwo()
s.inserts('1')
for i in range(15):
    s.inserts(i)
end_time = timer()
print(end_time - start_time)
print(s.fifo_list)
s.past()
print(s.fifo_list)