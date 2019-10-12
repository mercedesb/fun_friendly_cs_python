from django.shortcuts import render
from .models import Cupcakes
import random

# Create your views here.
def index(request):
  batches = random.randint(1,11)
  context = {'progress': "You haven't started baking yet :(", 'batches': batches }
  return render(request, 'big_o_notation/index.html', context)

def preheat_oven(request, batches):
  context = {'progress': Cupcakes().preheat_oven(batches), 'batches': batches}
  return render(request, 'big_o_notation/index.html', context)

def combine_butter_and_sugar(request, batches):
  context = {'progress': Cupcakes().combine_butter_and_sugar(batches), 'batches': batches}
  return render(request, 'big_o_notation/index.html', context)

def add_eggs(request, batches):
  context = {'progress': Cupcakes().add_eggs(batches), 'batches': batches}
  return render(request, 'big_o_notation/index.html', context)

def combine_flour_and_baking_powder(request, batches):
  context = {'progress': Cupcakes().combine_flour_and_baking_powder(batches), 'batches': batches}
  return render(request, 'big_o_notation/index.html', context)

def combine_milk_flour_and_butter_mixture(request, batches):
  context = {'progress': Cupcakes().combine_flour_mixture_and_milk_and_butter_mixture(batches), 'batches': batches}
  return render(request, 'big_o_notation/index.html', context)

def bake(request, batches):
  context = {'progress': Cupcakes().bake(), 'batches': batches}
  return render(request, 'big_o_notation/index.html', context)

def frost(request, batches):
  context = {'progress': Cupcakes().fibonacci_frosting(batches), 'batches': batches}
  return render(request, 'big_o_notation/index.html', context)