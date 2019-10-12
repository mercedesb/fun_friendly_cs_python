from django.test import TestCase

from django.test import TestCase
from linked_list.models import LinkedListNode
from .models import Stack

class StackTestCase(TestCase):
  def setUp(self):
    self.stack = Stack.objects.create()
  
  def test_head(self):
    """Has a head property"""
    self.assertIsNone(self.stack.head)

  def test_push_when_empty(self):
    """Adds a node as the head of the stack"""
    self.stack.push('3')
    self.assertIsInstance(self.stack.head, LinkedListNode)
    self.assertEqual(self.stack.head.data, '3')

  def test_push_when_not_empty(self):
    """Adds a node as the tail of the stack"""
    self.stack.push('3')
    self.stack.push('7')
    self.assertIsInstance(self.stack.head, LinkedListNode)
    self.assertEqual(self.stack.head.data, '7')
    self.assertIsInstance(self.stack.head.next, LinkedListNode)
    self.assertEqual(self.stack.head.next.data, '3')

  def test_pop_one(self):
    """Updates head to the following node"""
    self.stack.push('3')
    self.stack.push('7')
    self.stack.push('1')
    self.stack.pop()
    self.assertEqual(self.stack.head.data, '7')

  def test_pop_two(self):
    """Returns the correct node"""
    self.stack.push('3')
    self.stack.push('7')
    self.stack.push('1')
    node = self.stack.pop()
    self.assertIsInstance(node, LinkedListNode)
    self.assertEqual(node.data, '1')

  def test_insert_when_index_lt_zero(self):
    """Returns None"""
    self.stack.push('3')
    self.stack.push('7')
    self.stack.push('1')
    node = self.stack.insert('new data', -1)
    self.assertIsNone(node)

  def test_insert_when_index_is_zero_one(self):
    """Updates the head to be the new node"""
    self.stack.push('3')
    self.stack.push('7')
    self.stack.push('1')
    initial_head = self.stack.head
    self.stack.insert('new data', 0)
    self.assertIsInstance(self.stack.head, LinkedListNode)
    self.assertEqual(self.stack.head.data, 'new data')
    self.assertEqual(self.stack.head.next, initial_head)

  def test_insert_when_index_is_zero_two(self):
    """Returns the correct node"""
    self.stack.push('3')
    self.stack.push('7')
    self.stack.push('1')
    node = self.stack.insert('new data', 0)
    self.assertIsInstance(node, LinkedListNode)
    self.assertEqual(node.data, 'new data')

  def test_insert_when_index_gt_zero(self):
    """Raises Exception"""
    self.stack.push('3')
    self.stack.push('7')
    self.stack.push('1')
    with self.assertRaises(Exception):
      self.stack.insert('new data', 1)
