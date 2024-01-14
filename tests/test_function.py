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

def test_modify_date():
    assert modify_date([{"date": "2019-07-03T18:35:29.512364"},
                        {"date": "2018-06-30T02:08:58.425572"},
                        {"date": "2019-08-26T10:50:58.294041"}]) == [{'date': '3.7.2019'},
                                                                     {'date': '30.6.2018'},
                                                                     {'date': '26.8.2019'}]

def test_modify_bill():
    assert modify_bill([{"to": "Счет 11776614605963066702"},
                        {"to": "Счет 41421565395219882431"}]) == [{"to": "Счет **6702"},
                                                                  {"to": "Счет **2431"}]

    assert modify_bill([{"from": "Счет 75106830613657916952",
                         "to": "Счет 35383033474447895560"},
                        {"from": "MasterCard 7158300734726758",
                         "to": "Счет 11776614605963066702"}]) == [{"from": "Счет **6952",
                                                                   "to": "Счет **5560"},
                                                                  {"from": "MasterCard 7158 30** **** 6758",
                                                                   "to": "Счет **6702"}]


