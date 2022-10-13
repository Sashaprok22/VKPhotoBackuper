import requests

class VKontakte():
    token = "VK_TOKEN"

    def get_photos(self, owner_id=-1, count=5):
        params = {
            "access_token": self.token,
            "v": 5.131,
            "count": count,
            "owner_id": owner_id,
            "album_id": "profile",
            "extended": 1,
            "rev": 1,
        }
        vk_reponse = requests.get("https://api.vk.com/method/photos.get", params)
        vk_reponse.raise_for_status()
        return vk_reponse.json().get("response")

if __name__ == "__main__":
    vk = VKontakte()
    print(vk.get_photos(472289571))