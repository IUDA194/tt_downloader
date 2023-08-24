import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


class TikTok_video:

    link = None
    name = None
    path = None

    def __init__(self, link, name) -> None:
        self.link = link
        self.name = name


    def download(self):
        cookies = {
            '__cflb': '0H28v8EEysMCvTTqtuFFMWyYEmbm6aBgFbGgf6QNXTT',
        }

        headers = {
            'authority': 'ssstik.io',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '__cflb=0H28v8EEysMCvTTqtuFFMWyYEmbm6aBgFbGgf6QNXTT',
            'hx-current-url': 'https://ssstik.io/ru',
            'hx-request': 'true',
            'hx-target': 'target',
            'hx-trigger': '_gcaptcha_pt',
            'origin': 'https://ssstik.io',
            'referer': 'https://ssstik.io/ru',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        }

        params = {
            'url': 'dl',
        }

        data = {
            'id': self.link,
            'locale': 'ru',
            'tt': 'dFRZRFI5',
        }

        response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
        downloadSoup = BeautifulSoup(response.text, "html.parser")

        downloadLink = downloadSoup.a['href']

        mp4_file = urlopen(downloadLink)
        with open(f"tiktok/{self.name}.mp4", "wb") as file:
            self.path = f"tiktok/{self.name}.mp4"
            while True:
                data = mp4_file.read(4096)
                if data: file.write(data)
                else: break

