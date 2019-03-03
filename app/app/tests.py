from django.test import TestCase

from .calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)


    def test_subtrack_number(self):
        self.assertEqual(subtract(5, 11), 6)
