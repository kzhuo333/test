def test_more1():
    """_summary_
    """
    assert 'a' in ['a', 'b']


def test_more2(some_data):
    """_summary_

    Args:
        some_data (_type_): _description_
    """
    assert some_data['a'] == 123
    assert some_data['b'] == 456


def test_more3(some_sub_data):
    """

    Args:
        some_sub_data (_type_): _description_
    """
    assert some_sub_data['col_a'].to_list() == [1, 2, 3]
