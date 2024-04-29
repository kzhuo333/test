"""Docstring."""

import pytest
import pandas as pd


@pytest.fixture
def some_sub_data():
    retval = pd.DataFrame({'col_a': [1, 2, 3], 'col_b': [4, 5, 6]})
    return retval
