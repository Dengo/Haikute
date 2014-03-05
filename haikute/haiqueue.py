from gevent import queue
from collections import deque

class Haistorage(object):

    def __init__(self):
        self.haiku = deque(maxlen=5)

    def backlog(self):
        return self.haiku

    def add(self, haiku):
        self.haiku.appendleft(haiku)

# stores haikus
haistorage = Haistorage()

#contains command queue
haiqueue = queue.Queue()

#when generated, haikus are added to command queue to be added to all ajax
while True:
    if haiqueue.empty():
        break
    haistorage.add(haiqueue.get())
