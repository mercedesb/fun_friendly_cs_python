from django.shortcuts import render
from .models import InstagramAccount

def index(request):
  if InstagramAccount.objects.count() == 0:
    progress = "You haven't created anything yet :("
  else:
     progress = f"{dogs_text()}{cats_text()}"

  context = {'progress': progress }
  return render(request, 'set_theory/index.html', context)

def intersection(request):
  header = 'Cute accounts that have both cats and dogs!'
  intersection = InstagramAccount.objects.filter(dog=True, cat=True)
  return render_set(request, header, intersection)

def union(request):
  header = 'All the cute accounts!'
  union = InstagramAccount.objects.all()
  return render_set(request, header, union)

def difference(request):
  header = 'Cute accounts that have only dogs (no cats allowed)!'
  difference = InstagramAccount.objects.filter(dog=True, cat=False)
  return render_set(request, header, difference)

def relative_complement(request):
  header = 'Cute accounts that have only cats (no dogs allowed)!'
  complement = InstagramAccount.objects.filter(dog=False, cat=True)
  return render_set(request, header, complement)

def symmetric_difference(request):
  header = 'Cute accounts that have only one type of animal (no cross-species friendships here)!'
  symmetric_difference = InstagramAccount.objects.filter(dog=True, cat=False) | InstagramAccount.objects.filter(dog=False, cat=True)
  return render_set(request, header, symmetric_difference)

def render_set(request, header, calculated_set):
  if InstagramAccount.objects.count() == 0:
    progress = "You haven't created anything yet :("
  else:
    progress = f"{dogs_text()}{cats_text()}{set_text(header, calculated_set)}"

  context = {'progress': progress }
  return render(request, 'set_theory/index.html', context)

def dogs_text():
  dogs = InstagramAccount.objects.filter(dog=True)
  return set_text('Cute Instagram Dogs', dogs)

def cats_text():
  cats = InstagramAccount.objects.filter(cat=True)
  return set_text('Cute Instagram Cats', cats)

def set_text(header, calculated_set):
  template = f"<div class='Set'><h3>{header}</h3><ul>"
  accounts_text = [ f"<li>{a.account_handle}</li>" for a in calculated_set ]
  template += "".join(accounts_text)
  template += '</ul></div>'
  return template