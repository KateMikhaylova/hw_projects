import requests
import os


class YaDisk:
    def __init__(self, token):
        self.token = token

    def _get_upload_link(self, yadisk_path):
        get_url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {"path": yadisk_path, "overwrite": "true"}
        resp = requests.get(get_url, headers=headers, params=params)
        upload_url = resp.json().get('href', '')
        return upload_url

    def upload_file(self, file_path):
        upload_url = self._get_upload_link(os.path.basename(file_path))
        response = requests.put(upload_url, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Файл успешно загружен на ЯндексДиск")


if __name__ == '__main__':
    token = input('Введите Ваш токен: ')
    ya = YaDisk(token)
    path_to_file = input('Введите путь к файлу на Вашем локальном компьютере для сохранения на ЯндексДиск: ')
    ya.upload_file(path_to_file)






