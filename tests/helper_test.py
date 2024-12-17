from datetime import datetime
from core.helper.datetime import formatDateTime


def test_datetime_converter():
    datetimeTest = datetime(2024, 6, 13, 15, 8, 39)

    converted = formatDateTime(datetimeTest)

    assert converted == "13-06-2024 15:08:39"
