from django.test import TestCase

from app.app import calc


class CalcTest(TestCase):
    def test_add(self):
        r = calc.add(1, 2)
        valor_esperado = 3
        self.assertEquals(r, valor_esperado)
