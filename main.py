from yandex import YandexDisk
from vk_get import VkGetPhotos

YA_TOKEN = ''
vk_token = ''
VK_owner_id = ''

if __name__ == '__main__':
    vk = VkGetPhotos(vk_token)
    ya = YandexDisk(YA_TOKEN)
    ya.vk_backup(vk.get_photos(VK_owner_id))

