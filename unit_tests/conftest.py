"""Docstring."""
import pytest
from modules.module2 import MyClass


@pytest.fixture
def my_fix():
    """_summary_

    Returns:
        _type_: _description_
    """
    print('Making a Jimmy')
    return MyClass('Jimmy')


@pytest.fixture
def some_data():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {'a': 123, 'b': 456}
