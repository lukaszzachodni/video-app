from Pexels import Client as PexelsApi
import requests
import datetime


class PexelsStockMedia:
    def __init__(self, apiKey: str):
        self.apiKey = apiKey
        self.pexels = PexelsApi(token=apiKey)

    def search_photos(self, query: str, page: int = 1, per_page: int = 15):
        photos = self.pexels.search_photos(query, page=page, results_per_page=per_page)
        return photos

    def get_photo(self, photo_id: int):
        photo = self.pexels.get_photo(photo_id)
        return photo

    def search_videos(self, query: str, page: int = 1, per_page: int = 15):
        videos = self.pexels.search_videos(query, page=page, per_page=per_page)
        return videos

    def get_video(self, video_id: int):
        video = self.pexels.get_video(video_id)
        return video

    def get_remaining_requests(self):

        try:
            response = requests.get(
                "https://api.pexels.com/v1/",
                headers={"Authorization": self.apiKey},
            )
            response.raise_for_status()

            limit = int(response.headers["X-Ratelimit-Limit"])
            remaining = int(response.headers["X-Ratelimit-Remaining"])
            limit_reset = datetime.datetime.fromtimestamp(
                int(response.headers["X-Ratelimit-Reset"])
            ).strftime("%Y-%m-%d %H:%M:%S")

            return limit, remaining, limit_reset

        except requests.exceptions.RequestException as e:
            print(f"Error checking request limits: {e}")
