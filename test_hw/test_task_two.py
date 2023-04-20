import pytest
from hw_test.task_two_func import YandexFolder


def test_yandex_folder():

    new_folder = YandexFolder(token='') #добавить токен с полигона
    res = new_folder.create_folder('folder_one')
    assert 'Папка успешно создана, код: 201' == res


