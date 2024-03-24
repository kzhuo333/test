"""Docstring."""
import pytest
from modules.module2 import MyClass


def test_exception(my_fix):
    """_summary_
    """
    with pytest.raises(ValueError) as ex:
        my_fix.throw_exception()
    assert str(ex.value) == 'Jimmy loves value errors!'
