from django.shortcuts import render
import json
from .models import TreeNode, Tree

def index(request):
  progress = "You haven't chosen anyone to go through the maze yet :("
  context = {'progress': progress }
  return render(request, 'tree/index.html', context)

def harry_worst_iterative(request):
  triwizard_maze = initialize_triwizard_maze()
  route = triwizard_maze.iterative_breadth_first_search(harrys_entry_point(triwizard_maze), search_path_name, found_the_triwizard_cup)
  progress = render_route(route)
  context = {'progress': progress }
  return render(request, 'tree/index.html', context)

def harry_worst_recursive(request):
  triwizard_maze = initialize_triwizard_maze()
  route = triwizard_maze.recursive_breadth_first_search(harrys_entry_point(triwizard_maze), search_path_name, found_the_triwizard_cup)
  progress = render_route(route)
  context = {'progress': progress }
  return render(request, 'tree/index.html', context)

def harry_best_iterative(request):
  triwizard_maze = initialize_triwizard_maze()
  route = triwizard_maze.iterative_depth_first_search(harrys_entry_point(triwizard_maze), search_path_name, found_the_triwizard_cup)
  progress = render_route(route)
  context = {'progress': progress }
  return render(request, 'tree/index.html', context)

def harry_best_recursive(request):
  triwizard_maze = initialize_triwizard_maze()
  route = triwizard_maze.recursive_depth_first_search(harrys_entry_point(triwizard_maze), search_path_name, found_the_triwizard_cup)
  progress = render_route(route)
  context = {'progress': progress }
  return render(request, 'tree/index.html', context)

def cedric_worst_iterative(request):
  triwizard_maze = initialize_triwizard_maze()
  route = triwizard_maze.iterative_breadth_first_search(cedrics_entry_point(triwizard_maze), search_path_name, found_the_triwizard_cup)
  progress = render_route(route)
  context = {'progress': progress }
  return render(request, 'tree/index.html', context)

def cedric_worst_recursive(request):
  triwizard_maze = initialize_triwizard_maze()
  route = triwizard_maze.recursive_breadth_first_search(cedrics_entry_point(triwizard_maze), search_path_name, found_the_triwizard_cup)
  progress = render_route(route)
  context = {'progress': progress }
  return render(request, 'tree/index.html', context)

def cedric_best_iterative(request):
  triwizard_maze = initialize_triwizard_maze()
  route = triwizard_maze.iterative_depth_first_search(cedrics_entry_point(triwizard_maze), search_path_name, found_the_triwizard_cup)
  progress = render_route(route)
  context = {'progress': progress }
  return render(request, 'tree/index.html', context)

def cedric_best_recursive(request):
  triwizard_maze = initialize_triwizard_maze()
  route = triwizard_maze.recursive_depth_first_search(cedrics_entry_point(triwizard_maze), search_path_name, found_the_triwizard_cup)
  progress = render_route(route)
  context = {'progress': progress }
  return render(request, 'tree/index.html', context)

def initialize_triwizard_maze():
  if Tree.objects.count() > 0:
    return Tree.objects.first()
  else:
    root = TreeNode.objects.create(data=json.dumps({ 'name': 'start' }))
    one = TreeNode.objects.create(data=json.dumps({ 'name': '1', 'who': 'Harry' }))
    two = TreeNode.objects.create(data=json.dumps({ 'name': '2', 'who': 'Cedric' }))
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
    nine = TreeNode.objects.create(data=json.dumps({ 'name': '9' }))
    ten = TreeNode.objects.create(data=json.dumps({ 'name': '10' }))
    three.add_child(seven)
    three.add_child(eight)
    six.add_child(nine)
    six.add_child(ten)

    eleven = TreeNode.objects.create(data=json.dumps({ 'name': '11' }))
    twelve = TreeNode.objects.create(data=json.dumps({ 'name': '12' }))
    thirteen = TreeNode.objects.create(data=json.dumps({ 'name': '13' }))
    fourteen = TreeNode.objects.create(data=json.dumps({ 'name': '14' }))
    fifteen = TreeNode.objects.create(data=json.dumps({ 'name': '15' }))
    eight.add_child(eleven)
    eight.add_child(twelve)
    ten.add_child(thirteen)
    ten.add_child(fourteen)
    ten.add_child(fifteen)

    sixteen = TreeNode.objects.create(data=json.dumps({ 'name': '16', 'triwizard_cup': True }))
    seventeen = TreeNode.objects.create(data=json.dumps({ 'name': '17' }))
    eighteen = TreeNode.objects.create(data=json.dumps({ 'name': '18' }))
    nineteen = TreeNode.objects.create(data=json.dumps({ 'name': '19' }))
    eleven.add_child(sixteen)
    eleven.add_child(seventeen)
    fourteen.add_child(eighteen)
    fourteen.add_child(nineteen)

    twenty = TreeNode.objects.create(data=json.dumps({ 'name': '20' }))
    twentyone = TreeNode.objects.create(data=json.dumps({ 'name': '21' }))
    twentytwo = TreeNode.objects.create(data=json.dumps({ 'name': '22' }))
    nineteen.add_child(twenty)
    nineteen.add_child(twentyone)
    nineteen.add_child(twentytwo)

    twentythree = TreeNode.objects.create(data=json.dumps({ 'name': '23' }))
    twentyfour = TreeNode.objects.create(data=json.dumps({ 'name': '24', 'triwizard_cup': True }))
    twenty.add_child(twentythree)
    twenty.add_child(twentyfour)

    return Tree.objects.create(root=root)

def found_the_triwizard_cup(node):
  return json.loads(node.data).get("triwizard_cup", False)

def search_path_name(node):
  return json.loads(node.data)['name']

def harrys_entry_point(maze):
  return maze.root.children().filter(data__contains='Harry').first()

def cedrics_entry_point(maze):
  return maze.root.children().filter(data__contains='Cedric').first()

def render_route(route):
  return ' -> '.join(route)
