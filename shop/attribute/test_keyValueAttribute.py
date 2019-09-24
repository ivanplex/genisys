from unittest import TestCase
from .models import KeyValueAttribute


class TestKeyValueAttribute(TestCase):


    def test_get_key(self):
        kv = KeyValueAttribute.objects.create()
        kv.key = "Test"
        self.assertEqual(kv.get_key())
        self.fail()

    def test_set_key(self):
        self.fail()

    def test_get_value(self):
        self.fail()

    def test_set_value(self):
        self.fail()
