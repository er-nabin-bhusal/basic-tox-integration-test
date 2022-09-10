from unittest import TestCase
from app import demo_func


class TestWith(TestCase):

    def test_demo_func(self):
        res = demo_func()
        self.assertEqual(res, True)
