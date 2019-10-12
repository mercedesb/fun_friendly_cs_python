from django.test import TestCase
from .models import NestingDollCollection

class NestingDollCollectionTestCase(TestCase):
  def test_count(self):
    """Accurately counts the number of nested dolls"""
    seven = NestingDollCollection(7)
    three = NestingDollCollection(3)
    ten = NestingDollCollection(10)
    self.assertEqual(seven.count(), 7)
    self.assertEqual(three.count(), 3)
    self.assertEqual(ten.count(), 10)