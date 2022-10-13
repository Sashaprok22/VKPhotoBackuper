from vk import VKontakte
from yandex import Yandex
from tqdm import tqdm
from json import dumps

if __name__ == "__main__":
    ya_token = input("Введите Yandex Токен: ")
    if len(ya_token.strip()) == 0: exit("Токен не верен")

    vk_id = input("Введите VK ID: ")
    if not vk_id.isdigit(): exit("Это не число")

    vk = VKontakte()
    ya = Yandex(ya_token)

    photos = vk.get_photos(int(vk_id), 5)

    result_json = []
    busyes_likes = {}
    
    for photo in tqdm(photos.get("items")):
        likes = photo.get("likes").get("count")
        name = str(likes) + ".jpg"

        if busyes_likes.get(likes):
            name = str(photo.get("date")) + ".jpg"
        else:
            busyes_likes[likes] = True

        photo_data = max(photo.get("sizes"), key=lambda a: a.get("width"))
        ya.upload_file_by_url(name, photo_data.get("url"))

        result_json.append({
            "file_name": name,
            "size": photo_data.get("type")
        })

    with open("log.json", "w") as file:
        file.write(dumps(result_json))