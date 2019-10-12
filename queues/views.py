from django.shortcuts import render
import datetime
from .models import Queue

def index(request):
  if Queue.objects.count() == 0:
    progress = "Nobody wants to speak yet :("
  else:
    progress = render_queue(Queue.objects.all().order_by('created_at').last())

  context = {'progress': progress }
  return render(request, 'queues/index.html', context)
  

def create(request):
  bof_line = Queue.objects.create() if Queue.objects.count() == 0 else Queue.objects.all().order_by('created_at').last()
  bof_line.enqueue(f"Person {datetime.datetime.now()}")
  progress = render_queue(bof_line)
  context = {'progress': progress }
  return render(request, 'queues/index.html', context)

def delete(request):
  bof_line = Queue.objects.all().order_by('created_at').last()

  if bof_line is None or bof_line.head is None:
    error_message = '⚠️ Oops! Nothing to delete'
  else:
    bof_line.dequeue()
    error_message = None

  progress = render_queue(bof_line)
  context = {'progress': progress, 'error_message': error_message }
  return render(request, 'queues/index.html', context)

def render_queue(queue):
  template = '<ul>'

  node = queue.head
  while node is not None:
    template += f"<li>{node.data}</li>"
    node = node.next

  template += '</ul>'

  return template
