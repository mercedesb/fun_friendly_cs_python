from django.db import models

class NestingDollCollection:
  def __init__(self, number):
    self.big_doll = NestingDoll(True)
    self.nest_dolls(number - 1, self.big_doll)

  def count(self):
    return self.count_nested_dolls(self.big_doll)

  def count_nested_dolls(self, doll):
    child = doll.open()

    # base case
    if child is None:
      return 1

    return self.count_nested_dolls(child) + 1

  def nest_dolls(self, number, doll):
    # base case
    if number <= 1:
      doll.add_child(False)
    else:
      doll.add_child(True)
      self.nest_dolls(number - 1, doll.child)

class NestingDoll:
  def __init__(self, opens):
    self.opens = opens
    self.child = None

  def add_child(self, child_opens):
    self.child = NestingDoll(child_opens)

  def open(self):
    if (self.opens):
      return self.child