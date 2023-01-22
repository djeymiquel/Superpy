from my_lib2 import *


def test_date_today():
    with open("files/current_date.txt", "r") as file:
        current_date_string = file.read().strip()
        assert current_date_string == today.strftime("%Y/%m/%d")

def test_yesterdays():
    assert yesterday == today - timedelta(days=1)

def test_date_string():
    assert my_date.date_string('2023-01') == 'January 2023'
