import pytest
from hw_test.task_one_funcs import geo_logs_visit, geo_logs


@pytest.mark.parametrize("num_index, num_visit", [
    (0, 'visit1'),
    (1, 'visit3'),
    (2, 'visit7'),
    (3, 'visit8'),
    (4, 'visit9'),
    (5, 'visit10'),
])
def test_geo_logs_city(num_index, num_visit):
    res = geo_logs_visit(geo_logs)
    assert 'Россия' in res[num_index][num_visit]


def test_geo_logs_city_two():
    res = geo_logs_visit(geo_logs)
    assert type(res) == list
