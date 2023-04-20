import pytest
from hw_test.task_one_funcs import biggest_volume_channel, stats


def test_biggest_volume_channel():
    res = biggest_volume_channel(stats)
    assert '120' in res
    assert 'yandex' in res

