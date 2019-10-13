from django.db import models
from queues.models import Queue
from stack.models import Stack

class TreeNode(models.Model):
  data = models.CharField(max_length=10000)
  parent = models.ForeignKey('self', models.SET_NULL, blank=True, null=True)

  def children(self):
    return TreeNode.objects.filter(parent=self)
  
  def add_child(self, node):
    node.parent = self
    node.save()

class Tree(models.Model):
  root = models.ForeignKey(TreeNode, models.SET_NULL, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def iterative_breadth_first_search(self, root_node, get_search_path, success_criteria):
    # Check that a root node exists.
    if root_node is None:
      return

    # Create our queue and push our root node into it.
    visited_nodes = Queue.objects.create()
    visited_nodes.enqueue(root_node.id)
    found_node = False
    search_path = []

    # Continue searching through as queue as long as it's not empty.
    while visited_nodes.tail is not None and found_node is False:
      node_id = int(visited_nodes.dequeue().data)
      current_node = TreeNode.objects.get(id=node_id)
      search_path.append(get_search_path(current_node))

      found_node = success_criteria(current_node)

      if found_node:
        search_path.append('Success!')

      for child in current_node.children(): 
        if child is not None:
          visited_nodes.enqueue(child.id)

    visited_nodes.destroy()
    return search_path

  def recursive_breadth_first_search(self, root_node, get_search_path, success_criteria):
    visited_nodes = Queue.objects.create()
    visited_nodes.enqueue(root_node.id)
    search_path = self.recursive_bfs_logic(visited_nodes, get_search_path, success_criteria, [])
    return search_path

  def recursive_bfs_logic(self, visited_nodes, get_search_path, success_criteria, search_path):
    if visited_nodes.tail is None:
      return  # if the queue is empty, we're done.
    
    node_id = int(visited_nodes.dequeue().data)
    current_node = TreeNode.objects.get(id=node_id)
    search_path.append(get_search_path(current_node))

    found_node = success_criteria(current_node)
    if found_node:
      search_path.append('Success!')
      visited_nodes.destroy() # if we found a successful path, we're done
      return search_path
    else:
      for child in current_node.children():
        if child is not None:
          visited_nodes.enqueue(child.id)

    return self.recursive_bfs_logic(visited_nodes, get_search_path, success_criteria, search_path)

  def iterative_depth_first_search(self, root_node, get_search_path, success_criteria):
    # Check that a root node exists.
    if root_node is None:
      return

    # Create our stack and push our root node into it.
    visited_nodes = Stack.objects.create()
    visited_nodes.push(root_node.id)
    found_node = False
    search_path = []

    # Continue searching through as stack as long as it's not empty.
    while visited_nodes.head is not None and found_node is False:
      node_id = int(visited_nodes.pop().data)
      current_node = TreeNode.objects.get(id=node_id)
      search_path.append(get_search_path(current_node))

      found_node = success_criteria(current_node)
      
      if found_node:
        search_path.append('Success!')

      for child in current_node.children():
        if child is not None:
          visited_nodes.push(child.id)

    visited_nodes.destroy()
    return search_path

  def recursive_depth_first_search(self, root_node, get_search_path, success_criteria):
    visited_nodes = Stack.objects.create()
    visited_nodes.push(root_node.id)
    search_path = self.recursive_dfs_logic(visited_nodes, get_search_path, success_criteria, [])
    return search_path

  def recursive_dfs_logic(self, visited_nodes, get_search_path, success_criteria, search_path):
    if visited_nodes.head is None:
      return  # if the stack is empty, we're done.

    node_id = int(visited_nodes.pop().data)
    current_node = TreeNode.objects.get(id=node_id)
    search_path.append(get_search_path(current_node))

    found_node = success_criteria(current_node)

    if found_node:
      search_path.append('Success!')
      visited_nodes.destroy() # if we found a successful path, we're done
      return search_path
    else:
      for child in current_node.children():
        if child is not None:
          visited_nodes.push(child.id)

    return self.recursive_dfs_logic(visited_nodes, get_search_path, success_criteria, search_path)
