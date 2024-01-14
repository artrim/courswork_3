from src.function import *

def test_filter_list():
    assert filter_list([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]
    assert filter_list([{}]) == []


