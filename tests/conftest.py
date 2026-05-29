import pytest


@pytest.fixture
def number():
    return [
        "Visa Platinum 7000792289606361",
        "Visa Classic 6831923482476737658",
        "Visa Classic 6831915151",
        "Visa Classic 6831sdg5151",
        "70007 922896 06361",
        "6831982476737658",
    ]


@pytest.fixture
def sample_data():
    """Фикстура с тестовыми данными"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 3, "state": "PENDING", "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def empty_data():
    """Фикстура с пустым списком"""
    return []


@pytest.fixture
def list_time():
    """Фикстура с датами"""
    return ["2019-07-03", "2018-10-14", "2018-09-12", "2018-06-30"]


@pytest.fixture
def list_time_false():
    """Фикстура с датами"""
    return ["2018-06-30", "2018-09-12", "2018-10-14", "2019-07-03"]
