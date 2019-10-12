from django.test import TestCase
from .models import LinkedListNode, LinkedList

class LinkedListNodeTestCase(TestCase):
  def setUp(self):
    LinkedListNode.objects.create(data='hi')

  def test_data(self):
    """Has a data property"""
    hi = LinkedListNode.objects.get(data="hi")
    self.assertEqual(hi.data, 'hi')

  def test_next(self):
    """Has a next property"""
    hi = LinkedListNode.objects.get(data="hi")
    self.assertIsNone(hi.next)

class LinkedListTestCase(TestCase):
  def setUp(self):
    self.list = LinkedList.objects.create()
  
  def test_head(self):
    """Has a head property"""
    self.assertIsNone(self.list.head)

  def test_tail(self):
    """Has a tail property"""
    self.assertIsNone(self.list.tail)

  def test_add_when_empty(self):
    """Adds a node as the head and tail of the list"""
    self.list.add('3')
    self.assertIsInstance(self.list.head, LinkedListNode)
    self.assertEqual(self.list.head.data, '3')
    self.assertIsInstance(self.list.tail, LinkedListNode)
    self.assertEqual(self.list.tail.data, '3')
    self.assertEqual(self.list.head, self.list.tail)

  def test_add_when_not_empty_one(self):
    """Adds a node to the end of the list"""
    self.list.add('3')
    self.list.add('7')
    self.assertIsInstance(self.list.tail, LinkedListNode)
    self.assertEqual(self.list.tail.data, '7')
    self.assertNotEqual(self.list.head, self.list.tail)

  def test_remove_head_when_head_not_none_one(self):
    """Updates head to the following node"""
    self.list.add('3')
    self.list.add('6')
    self.list.add('7')
    self.list.add('1')
    self.list.remove_head()
    self.assertEqual(self.list.head.data, '6')

  def test_remove_head_when_head_not_none_two(self):
    """Returns the correct node"""
    self.list.add('3')
    self.list.add('6')
    self.list.add('7')
    self.list.add('1')
    node = self.list.remove_head()
    self.assertIsInstance(node, LinkedListNode)
    self.assertEqual(node.data, '3')

  def test_remove_head_when_head_is_none(self):
    """Returns None"""
    self.assertIsNone(self.list.remove_head())

  def test_remove_tail_when_tail_not_none_one(self):
    """Updates tail to the previous node"""
    self.list.add('3')
    self.list.add('6')
    self.list.add('7')
    self.list.add('1')
    self.list.remove_tail()
    self.assertEqual(self.list.tail.data, '7')

  def test_remove_tail_when_tail_not_none_two(self):
    """Returns the correct node"""
    self.list.add('3')
    self.list.add('6')
    self.list.add('7')
    self.list.add('1')
    node = self.list.remove_tail()
    self.assertIsInstance(node, LinkedListNode)
    self.assertEqual(node.data, '1')

  def test_remove_tail_when_tail_is_none(self):
    """Returns None"""
    self.assertIsNone(self.list.remove_tail())

  def test_insert_when_index_less_than_zero(self):
    """Returns None"""
    self.list.add('3')
    self.list.add('7')
    self.list.add('1')
    node = self.list.insert('new data', -1)
    self.assertIsNone(node)

  def test_insert_when_index_is_zero_one(self):
    """Returns None"""
    self.list.add('3')
    self.list.add('7')
    self.list.add('1')
    initial_head = self.list.head
    self.list.insert('new data', 0)
    self.assertIsInstance(self.list.head, LinkedListNode)
    self.assertEqual(self.list.head.data, 'new data')
    self.assertEqual(self.list.head.next, initial_head)

  def test_insert_when_index_is_zero_two(self):
    """Returns the correct node"""
    self.list.add('3')
    self.list.add('7')
    self.list.add('1')
    node = self.list.insert('new data', 0)
    self.assertIsInstance(node, LinkedListNode)
    self.assertEqual(node.data, 'new data')

  def test_insert_when_index_is_gt_zero_and_in_middle_one(self):
    """Updates the next pointer of the previous node to the inserted node"""
    self.list.add('3')
    self.list.add('7')
    self.list.add('1')
    initial_head = self.list.head
    self.list.insert('new data', 1)
    inserted_node = self.list.head.next
    self.assertEqual(inserted_node.data, 'new data')
    self.assertEqual(initial_head.next, inserted_node)

  def test_insert_when_index_is_gt_zero_and_in_middle_two(self):
    """Sets the next pointer of the inserted node to the node that was at that position"""
    self.list.add('3')
    self.list.add('7')
    self.list.add('1')
    initial_node = self.list.head.next
    self.list.insert('new data', 1)
    inserted_node = self.list.head.next
    self.assertEqual(inserted_node.data, 'new data')
    self.assertEqual(inserted_node.next, initial_node)

  def test_insert_when_index_is_gt_zero_and_at_end_one(self):
    """Updates the next pointer of the previous tail node to the inserted node"""
    self.list.add('3')
    self.list.add('7')
    self.list.add('1')
    initial_tail = self.list.tail
    self.list.insert('new data', 3)
    inserted_node = self.list.head.next.next.next
    self.assertEqual(inserted_node.data, 'new data')
    self.assertEqual(initial_tail.next, inserted_node)

  def test_insert_when_index_is_gt_zero_and_at_end_two(self):
    """Updates the tail node to the inserted node"""
    self.list.add('3')
    self.list.add('7')
    self.list.add('1')
    self.list.insert('new data', 3)
    inserted_node = self.list.head.next.next.next
    self.assertEqual(inserted_node.data, 'new data')
    self.assertEqual(self.list.tail, inserted_node)
