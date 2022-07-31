import requests, os

TOKEN = '2619421814940190'  # константа токена
urls = [
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America',
]  # список адресов


def requests_get(url_all):
    # принимает список адресов
    r = (requests.get(url) for url in url_all)
    return r


def parser():
    # функция парсинга интелекта
    super_man = []
    for item in requests_get(urls):
        intelligence = item.json()
        try:
            for power_stats in intelligence['results']:
                super_man.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })
        except KeyError:
            print(f"Проверте ссылки urls: {urls}")

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_man:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый интелектуальный {name}, интелект: {intelligence_super_hero}")


parser()






class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
         """Метод загружает файлы по списку file_list на яндекс диск"""

         file_path = os.path.normpath(file_path)
         HEADERS = {"Authorization" : f'OAuth {self.token}'}
         FILES = {"file" : open(file_path, 'rb')}

         response_url = requests.get(
         "https://cloud-api.yandex.net/v1/disk/resources/upload",
         params = {"path": file_path} ,
         headers = HEADERS)
         url = response_url.json().get('href')

         response_upload = requests.put(url, files = FILES, headers = {})
         return print(response_upload.status_code)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    uploader = YaUploader(ZZZ)
    result = uploader.upload("file to upload/20211012_093058.jpg")
