"""Docstring."""
import pytest
from modules.module2 import MyClass


@pytest.fixture
def my_fix():
    """_summary_

    Returns:
        _type_: _description_
    """
    return MyClass('Jimmy')
