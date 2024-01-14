from src.function import *

def test_filter_list():
    assert filter_list([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]
    assert filter_list([{}]) == []

def test_sorted_by_date():
    assert sorted_by_date([{"date": "2019-07-03T18:35:29.512364"},
                           {"date": "2018-06-30T02:08:58.425572"},
                           {"date": "2019-08-26T10:50:58.294041"}]) == [{"date": "2019-08-26T10:50:58.294041"},
                                                                        {"date": "2019-07-03T18:35:29.512364"},
                                                                        {"date": "2018-06-30T02:08:58.425572"}]


