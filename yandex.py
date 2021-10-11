import requests
import time
from progress.bar import IncrementalBar


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def vk_backup(self, json_vk):
        
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

        headers = self.get_headers()

        _id = json_vk['photos']['id']

        name_list = list()

        requests.put(f'https://cloud-api.yandex.net/v1/disk/resources?path=VK_{_id}', headers=headers)
        bar = IncrementalBar('Загружено', max = len(json_vk['photos']['links']))
        for item in json_vk['photos']['links']:
            name = str(item['likes'])
            if name in name_list:
                name = str(item['likes'])+'_'+str(item['date'])
                file_path = f'VK_{_id}/{name}.jpg'
            else:
                file_path = f'VK_{_id}/{name}.jpg'
                name_list.append(name)
            params = {"path": file_path, 'url': item['url']}
            response = requests.post(upload_url, headers=headers, params=params)
            bar.next()
        bar.finish()
            #response.raise_for_status()
            #if response.status_code == 202:
            #    print("Success")
            #else: print('something wrong')

