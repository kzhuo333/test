"""Docstring."""
import modules.module1 as m1


def test_f1():
    """Docstring."""
    assert m1.f1(2, 2) == 4


def test_f2():
    """Docstring."""
    assert m1.f2(2, 2) == 4


def test_fixture(some_data, my_fix):
    """Docstring."""
    assert some_data['a'] == 123
    assert some_data['b'] == 456
    assert my_fix.name == 'Jimmy'
