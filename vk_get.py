import requests


class VkGetPhotos:
    def __init__(self, token):
        self.token = token
        self.url = 'https://api.vk.com/method/photos.get'
        self.param = {
            'album_id': 'profile',
            'photo_sizes': '1',
            'access_token': self.token,
            'v': '5.131',
            'extended': '1'
        }

    def get_photos(self, id, count = 5):
        self.param['owner_id'] = id
        counter = 0
        res = requests.get(self.url, params=self.param)
        res_dict = {'photos': {'id': id, 'links': []}}
        for item in res.json()['response']['items']:
            if counter < count:
                temp_dict = dict()
                temp_dict['url'] = item['sizes'][-1]['url']
                temp_dict['likes'] = item['likes']['count']
                temp_dict['date'] = item['date']
                res_dict['photos']['links'].append(temp_dict)
                counter += 1

        return res_dict






