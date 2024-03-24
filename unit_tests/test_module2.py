"""Docstring."""
import pytest
from modules.module2 import MyClass


def test_exception():
    """_summary_
    """
    cc = MyClass('Jimmy')
    with pytest.raises(ValueError):
        cc.throw_exception()
