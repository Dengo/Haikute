from gevent import queue
import json


class Haiqueue(object):

    def __init__(self):
        self.users = set()
        self.haiku = []

    def backlog(self, size=5):
        return self.haiku[:(-size-1):-1]

    def add(self, haiku):
        for user in self.users:
            print(user)
            user.queue.put_nowait(haiku)
        self.messages.append(haiku)


class User(object):

    def __init__(self):
        self.queue = queue.Queue()




