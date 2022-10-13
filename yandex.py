from time import sleep
import requests

class Yandex():
    folder = "vk_photos/"

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": token
        }
        requests.delete("https://cloud-api.yandex.net/v1/disk/resources", headers=self.headers, params={"path": self.folder, "permanently": 1})
        requests.put("https://cloud-api.yandex.net/v1/disk/resources", headers=self.headers, params={"path": self.folder})


    def upload_file_by_url(self, file_name, file_url):
        path = self.folder + file_name
        params = {
            "path": path,
            "url": file_url,
        }
        res_url = requests.post("https://cloud-api.yandex.net/v1/disk/resources/upload", headers=self.headers, params=params).json().get("href")

        if isinstance(res_url, str):
            result = requests.get(res_url, headers=self.headers).json()
            while result.get("status") == "in-progress":
                sleep(0.1)
                result = requests.get(res_url, headers=self.headers).json()

if __name__ == "__main__":
    ya = Yandex("YANDEX_TOKEN")
    ya.upload_file_by_url("img.jpg", "https://sun9-32.userapi.com/c5654/u02943/107531621/s_f15991c2.jpg")