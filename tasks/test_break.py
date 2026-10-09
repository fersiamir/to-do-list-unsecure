from django.test import TestCase


class BreakTest(TestCase):
    def test_always_fails(self):
        self.assertEqual(1, 2)
