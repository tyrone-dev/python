from unittest import TestCase
from unit_testing import is_prime

__author__ = 'tyronevb'


class TestIs_prime(TestCase):
  def test_is_prime(self):
    self.assertTrue(is_prime(5))
