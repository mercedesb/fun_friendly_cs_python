from django.test import TestCase
from linked_list.models import LinkedListNode
from .models import Queue

class QueueTestCase(TestCase):
  def setUp(self):
    self.queue = Queue.objects.create()
  
  def test_head(self):
    """Has a head property"""
    self.assertIsNone(self.queue.head)

  def test_tail(self):
    """Has a tail property"""
    self.assertIsNone(self.queue.tail)

  def test_enqueue_when_empty(self):
    """Adds a node as the head and tail of the queue"""
    self.queue.enqueue('3')
    self.assertIsInstance(self.queue.head, LinkedListNode)
    self.assertEqual(self.queue.head.data, '3')
    self.assertIsInstance(self.queue.tail, LinkedListNode)
    self.assertEqual(self.queue.tail.data, '3')
    self.assertEqual(self.queue.head, self.queue.tail)

  def test_enqueue_when_not_empty(self):
    """Adds a node as the tail of the queue"""
    self.queue.enqueue('3')
    self.queue.enqueue('7')
    self.assertIsInstance(self.queue.head, LinkedListNode)
    self.assertEqual(self.queue.head.data, '3')
    self.assertIsInstance(self.queue.head.next, LinkedListNode)
    self.assertEqual(self.queue.head.next.data, '7')
    self.assertIsInstance(self.queue.tail, LinkedListNode)
    self.assertEqual(self.queue.tail.data, '7')
    self.assertNotEqual(self.queue.head, self.queue.tail)

  def test_dequeue_one(self):
    """Updates head to the following node"""
    self.queue.enqueue('3')
    self.queue.enqueue('7')
    self.queue.enqueue('1')
    self.queue.dequeue()
    self.assertEqual(self.queue.head.data, '7')

  def test_dequeue_two(self):
    """Returns the correct node"""
    self.queue.enqueue('3')
    self.queue.enqueue('7')
    self.queue.enqueue('1')
    node = self.queue.dequeue()
    self.assertIsInstance(node, LinkedListNode)
    self.assertEqual(node.data, '3')

  def test_insert(self):
    """Raises exception"""
    self.queue.enqueue('3')
    self.queue.enqueue('7')
    self.queue.enqueue('1')
    with self.assertRaises(Exception):
      self.queue.insert('new data', 1)