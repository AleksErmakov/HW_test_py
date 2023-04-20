import requests


class YandexFolder:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, name_folder):
        url_yandex = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": name_folder, "overwrite": "true"}
        response = requests.put(url_yandex, headers=headers, params=params)
        if response.status_code == 201:
            return f'Папка успешно создана, код: {response.status_code}'
        if response.status_code != 201:
            return f'ошибка, код: {response.status_code}'


# if __name__ == '__main__':
#     token = ''  # добавить токен на Полигоне
#     new_folder = YandexFolder(token=token)
#     print(new_folder.create_folder('new_folder'))
