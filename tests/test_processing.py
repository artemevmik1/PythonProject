import pytest
from src.processing import *


def test_filter_by_state_success(sample_data: List[Dict[str, Any]]) -> None:
    result = filter_by_state(sample_data)
    expected = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
        {"id": 3, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"}
    ]
    assert result == expected
    assert len(result) == 3