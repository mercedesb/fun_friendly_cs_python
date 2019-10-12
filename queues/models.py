from django.db import models
from linked_list.models import LinkedList

class Queue(LinkedList):
  def enqueue(self, data):
    return self.add(data)

  def dequeue(self):
    dequeued = self.head
    self.head = self.head.next
    self.save()
    dequeued.next = None
    dequeued.save()
    return dequeued

  def insert(self, _data, _index):
    raise Exception("Can't insert into the middle of a queue")
