from django.test import TestCase
import json
from queues.models import Queue
from stack.models import Stack
from .models import TreeNode, Tree

class TreeBreadthFirstTestCase(TestCase):
  def setUp(self):
    self.tree = Tree.objects.create()
    root = TreeNode.objects.create(data=json.dumps({ 'name': 'root' }))
    one = TreeNode.objects.create(data=json.dumps({ 'name': '1' }))
    two = TreeNode.objects.create(data=json.dumps({ 'name': '2' }))
    root.add_child(one)
    root.add_child(two)

    three = TreeNode.objects.create(data=json.dumps({ 'name': '3' }))
    four = TreeNode.objects.create(data=json.dumps({ 'name': '4' }))
    five = TreeNode.objects.create(data=json.dumps({ 'name': '5' }))
    six = TreeNode.objects.create(data=json.dumps({ 'name': '6' }))
    one.add_child(three)
    one.add_child(four)
    two.add_child(five)
    two.add_child(six)

    seven = TreeNode.objects.create(data=json.dumps({ 'name': '7' }))
    eight = TreeNode.objects.create(data=json.dumps({ 'name': '8' }))
    nine = TreeNode.objects.create(data=json.dumps({ 'name': '9', 'success': True }))
    ten = TreeNode.objects.create(data=json.dumps({ 'name': '10' }))
    eleven = TreeNode.objects.create(data=json.dumps({ 'name': '11' }))
    twelve = TreeNode.objects.create(data=json.dumps({ 'name': '12' }))
    thirteen = TreeNode.objects.create(data=json.dumps({ 'name': '13' }))
    fourteen = TreeNode.objects.create(data=json.dumps({ 'name': '14' }))
    three.add_child(seven)
    three.add_child(eight)
    four.add_child(nine)
    four.add_child(ten)
    five.add_child(eleven)
    five.add_child(twelve)
    six.add_child(thirteen)
    six.add_child(fourteen)
    self.tree.root = root
    self.tree.save()
    self.expected_path = ['root','1','2','3','4','5','6','7','8','9','Success!']
  
  def success_criteria(self, node):
    return json.loads(node.data).get("success", False)
  
  def get_search_path(self, node):
    return json.loads(node.data)['name']

  def test_iterative_breadth_first_search_one(self):
    """Finds and returns the correct node"""
    search_path = self.tree.iterative_breadth_first_search(
      self.tree.root,
      self.get_search_path,
      self.success_criteria
    )
    self.assertEqual(search_path.pop(), 'Success!')
    self.assertEqual(search_path.pop(), '9')
    self.assertEqual(Queue.objects.count(), 0)

  def test_iterative_breadth_first_search_two(self):
    """searches breadth first"""
    search_path = self.tree.iterative_breadth_first_search(
      self.tree.root,
      self.get_search_path,
      self.success_criteria
    )
    self.assertEqual(len(search_path), len(self.expected_path))
    for i in range(len(search_path)):
      self.assertEqual(search_path[i], self.expected_path[i])

    self.assertEqual(Queue.objects.count(), 0)
  
  def test_recursive_breadth_first_search_one(self):
    """Finds and returns the correct node"""
    search_path = self.tree.recursive_breadth_first_search(
      self.tree.root,
      self.get_search_path,
      self.success_criteria
    )
    self.assertEqual(search_path.pop(), 'Success!')
    self.assertEqual(search_path.pop(), '9')
    self.assertEqual(Queue.objects.count(), 0)
  
  def test_recursive_breadth_first_search_two(self):
    """searches breadth first"""
    search_path = self.tree.recursive_breadth_first_search(
      self.tree.root,
      self.get_search_path,
      self.success_criteria
    )
    self.assertEqual(len(search_path), len(self.expected_path))
    for i in range(len(search_path)):
      self.assertEqual(search_path[i], self.expected_path[i])

    self.assertEqual(Queue.objects.count(), 0)
  
class TreeDepthFirstTestCase(TestCase):
  def setUp(self):
    self.tree = Tree.objects.create()
    root = TreeNode.objects.create(data=json.dumps({ 'name': 'root' }))
    one = TreeNode.objects.create(data=json.dumps({ 'name': '1' }))
    two = TreeNode.objects.create(data=json.dumps({ 'name': '2' }))
    root.add_child(one)
    root.add_child(two)

    three = TreeNode.objects.create(data=json.dumps({ 'name': '3' }))
    four = TreeNode.objects.create(data=json.dumps({ 'name': '4' }))
    five = TreeNode.objects.create(data=json.dumps({ 'name': '5' }))
    six = TreeNode.objects.create(data=json.dumps({ 'name': '6' }))
    one.add_child(three)
    one.add_child(four)
    two.add_child(five)
    two.add_child(six)

    seven = TreeNode.objects.create(data=json.dumps({ 'name': '7' }))
    eight = TreeNode.objects.create(data=json.dumps({ 'name': '8' }))
    nine = TreeNode.objects.create(data=json.dumps({ 'name': '9', 'success': True }))
    ten = TreeNode.objects.create(data=json.dumps({ 'name': '10' }))
    eleven = TreeNode.objects.create(data=json.dumps({ 'name': '11' }))
    twelve = TreeNode.objects.create(data=json.dumps({ 'name': '12' }))
    thirteen = TreeNode.objects.create(data=json.dumps({ 'name': '13' }))
    fourteen = TreeNode.objects.create(data=json.dumps({ 'name': '14' }))
    three.add_child(seven)
    three.add_child(eight)
    four.add_child(nine)
    four.add_child(ten)
    five.add_child(eleven)
    five.add_child(twelve)
    six.add_child(thirteen)
    six.add_child(fourteen)
    self.tree.root = root
    self.tree.save()
    self.expected_path = ['root','2','6','14','13','5','12','11','1','4','10','9','Success!']
  
  def success_criteria(self, node):
    return json.loads(node.data).get("success", False)
  
  def get_search_path(self, node):
    return json.loads(node.data)['name']

  def test_iterative_depth_first_search_one(self):
    """Finds and returns the correct node"""
    search_path = self.tree.iterative_depth_first_search(
      self.tree.root,
      self.get_search_path,
      self.success_criteria
    )

    self.assertEqual(search_path.pop(), 'Success!')
    self.assertEqual(search_path.pop(), '9')
    self.assertEqual(Stack.objects.count(), 0)
    
  def test_iterative_depth_first_search_two(self):
    """searches depth first"""
    search_path = self.tree.iterative_depth_first_search(
      self.tree.root,
      self.get_search_path,
      self.success_criteria
    )
    self.assertEqual(len(search_path), len(self.expected_path))
    for i in range(len(search_path)):
      self.assertEqual(search_path[i], self.expected_path[i])
    
    self.assertEqual(Stack.objects.count(), 0)

  def test_recursive_depth_first_search_one(self):
    """Finds and returns the correct node"""
    search_path = self.tree.recursive_depth_first_search(
      self.tree.root,
      self.get_search_path,
      self.success_criteria
    )
    self.assertEqual(search_path.pop(), 'Success!')
    self.assertEqual(search_path.pop(), '9')
    self.assertEqual(Stack.objects.count(), 0)
    
  def test_recursive_depth_first_search_two(self):
    """searches depth first"""
    search_path = self.tree.recursive_depth_first_search(
      self.tree.root,
      self.get_search_path,
      self.success_criteria
    )
    self.assertEqual(len(search_path), len(self.expected_path))
    for i in range(len(search_path)):
      self.assertEqual(search_path[i], self.expected_path[i])

    self.assertEqual(Stack.objects.count(), 0)

