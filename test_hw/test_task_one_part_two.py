import pytest
from hw_test.task_one_funcs import unique_id, ids


@pytest.mark.parametrize("values", [213, 15, 54, 119, 98, 35])
def test_unique_id_one(values):
    res = unique_id(ids)
    assert values in res


@pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5])
def test_unique_id_two(index):
    res = unique_id(ids)
    assert res.count(res[index]) == 1
