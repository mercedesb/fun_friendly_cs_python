from django.shortcuts import render
import datetime
from .models import Stack

def index(request):
  if Stack.objects.count() == 0:
    progress = "No candy yet :("
  else:
    progress = render_stack(Stack.objects.all().order_by('created_at').last())

  context = {'progress': progress }
  return render(request, 'stack/index.html', context)
  
def create(request):
  pez_dispenser = Stack.objects.create() if Stack.objects.count() == 0 else Stack.objects.all().order_by('created_at').last()
  pez_dispenser.push(f"PEZ {datetime.datetime.now()}")
  progress = render_stack(pez_dispenser)
  context = {'progress': progress }
  return render(request, 'stack/index.html', context)

def delete(request):
  pez_dispenser = Stack.objects.all().order_by('created_at').last()

  if pez_dispenser is None or pez_dispenser.head is None:
    error_message = '⚠️ Oops! Nothing to delete'
  else:
    pez_dispenser.pop()
    error_message = None

  progress = render_stack(pez_dispenser)
  context = {'progress': progress, 'error_message': error_message }
  return render(request, 'stack/index.html', context)

def render_stack(stack):
  template = '<ul>'

  node = stack.head
  while node is not None:
    template += f"<li>{node.data}</li>"
    node = node.next

  template += '</ul>'

  return template
