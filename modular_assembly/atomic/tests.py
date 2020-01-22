from django.test import TestCase
from django.core.exceptions import ValidationError
from modular_assembly.atomic.models import AtomicComponent


class AtomicComponentCreateTestCase(TestCase):
    def test(self):
        """
        Test AtomicComponent creation
        """
        try:
            a = AtomicComponent()
            a.save()
            self.fail("Violation integrity")
        except ValidationError:
            pass
