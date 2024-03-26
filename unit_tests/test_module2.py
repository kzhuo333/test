"""Docstring."""
import pytest
from modules.module2 import MyClass


def test_exception(my_fix):
    """_summary_
    """
    with pytest.raises(ValueError) as ex:
        my_fix.throw_exception()
    assert str(ex.value) == 'Jimmy loves value errors!'


def test_data_fixture(some_data):
    """_summary_

    Args:
        some_data (_type_): _description_
    """
    assert 'a' in some_data
    assert 'b' in some_data
    assert some_data['a'] + some_data['b'] == 579
    with pytest.raises(KeyError):
        some_data['c']
