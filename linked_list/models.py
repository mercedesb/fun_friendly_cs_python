from django.db import models

class LinkedListNode(models.Model):
  data = models.CharField(max_length=10000)
  next = models.ForeignKey('self', models.SET_NULL, blank=True, null=True)

class LinkedList(models.Model):
  head = models.ForeignKey(LinkedListNode, models.SET_NULL, blank=True, null=True, related_name='head')
  tail = models.ForeignKey(LinkedListNode, models.SET_NULL, blank=True, null=True, related_name='tail')
  created_at = models.DateTimeField(auto_now_add=True)

  def add(self, data):
    new_node = LinkedListNode.objects.create(data=data)
    if self.head is None:
      self.head = new_node
    else:
      self.tail.next = new_node
      self.tail.save()

    self.tail = new_node

    self.save()
    return new_node

  def remove(self):
    return self.remove_head()

  def insert(self, data, index):
    if index < 0:
      return None 

    new_node = LinkedListNode.objects.create(data=data)

    if index == 0:
      new_node.next = self.head
      self.head = new_node
      self.save()
    else:
      current = self.head
      previous = None
      i = 0

      while current is not None and i < index:
        previous = current
        current = current.next
        i += 1

      # found where to insert the new node
      if current is not None:
        previous.next = new_node
        new_node.next = current
        previous.save()
        new_node.save()
      elif previous == self.tail:
        self.add(data)

    return new_node

  def remove_head(self):
    if self.head is None:
      return self.head

    removed = self.head
    self.head = self.head.next
    self.save()
    removed.next = None
    removed.save()
    return removed

  def remove_tail(self):
    if self.tail is None:
      return self.tail

    current = self.head
    previous = None

    while current.next is not None:
      previous = current
      current = current.next

    removed = self.tail
    self.tail = previous
    self.save()
    return removed

  def destroy(self):
    current = self.head
    self.head = None
    self.tail = None

    while current is not None:
      previous = current
      current = current.next
      previous.delete()

    self.delete()
