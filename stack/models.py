from django.db import models
from linked_list.models import LinkedList, LinkedListNode

class Stack(LinkedList):
  def push(self, data):
    new_node = LinkedListNode.objects.create(data=data)

    if self.head is not None:
      new_node.next = self.head
      new_node.save()

    self.head = new_node
    self.save()
    return new_node

  def pop(self):
    popped = self.head
    self.head = self.head.next
    self.save()
    popped.next = None
    popped.save()
    return popped

  # override default add behavior
  def add(self, data):
    self.push(data)

  def insert(self, data, index):
    if index > 0:
      raise Exception("Can't insert into the middle of a stack")

    return super().insert(data, index)
