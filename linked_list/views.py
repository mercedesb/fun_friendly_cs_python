from django.shortcuts import render
from .models import LinkedList

def index(request):
  if LinkedList.objects.count() == 0:
    progress = "No clues yet :("
  else:
    progress = render_list(LinkedList.objects.all().order_by('created_at').last())

  context = {'progress': progress }
  return render(request, 'linked_list/index.html', context)
  

def create(request):
  current_list = LinkedList.objects.create() if LinkedList.objects.count() == 0 else LinkedList.objects.all().order_by('created_at').last()
  current_list.add(request.POST['add'])
  progress = render_list(current_list)
  context = {'progress': progress }
  return render(request, 'linked_list/index.html', context)

def delete(request):
  current_list = LinkedList.objects.all().order_by('created_at').last()

  if current_list is None or current_list.head is None:
    error_message = '⚠️ Oops! Nothing to delete'
  else:
    current_list.remove()
    error_message = None

  progress = render_list(current_list)
  context = {'progress': progress, 'error_message': error_message }
  return render(request, 'linked_list/index.html', context)

def render_list(list_to_render):
  template = '<ul>'

  clue = list_to_render.head
  while clue is not None:
    template += f"<li>{clue.data}</li>"
    clue = clue.next

  template += '</ul>'

  return template

