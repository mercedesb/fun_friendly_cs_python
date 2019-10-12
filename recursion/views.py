from django.shortcuts import render
from .models import NestingDollCollection
import random

# Create your views here.
def index(request):
  context = {'progress': "We haven't counted yet :(" }
  return render(request, 'recursion/index.html', context)

def count(request):
  random_number = random.randint(1,11)
  nesting_dolls = NestingDollCollection(random_number)
  count = nesting_dolls.count()
  context = {'progress': f"There are {count} nested dolls" }
  return render(request, 'recursion/index.html', context)