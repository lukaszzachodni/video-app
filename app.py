import os
from dotenv import load_dotenv
import requests
from src.Json2VideoSDK.src.Movie import Movie
from src.PexelsStockMedia import PexelsStockMedia
from src.Json2VideoSDK.Client import Client as Json2VideoClient
from src.Json2VideoSDK.src.Audio import Audio
from src.Json2VideoSDK.src.Audiogram import Audiogram
from src.Json2VideoSDK.src.Component import Component
from src.Json2VideoSDK.src.HTML import HTML
from src.Json2VideoSDK.src.Image import Image
from src.Json2VideoSDK.src.Scene import Scene
from src.Json2VideoSDK.src.Subtitles import Subtitles
from src.Json2VideoSDK.src.Text import Text
from src.Json2VideoSDK.src.Video import Video
from src.Json2VideoSDK.src.Voice import Voice
from src.GeminiApi import GeminiApi
import yaml
import json


def yaml_do_json(plik_yaml):
    """
    Wczytuje schemat z pliku YAML i zwraca JSON z tym schematem.

    Args:
      plik_yaml: Ścieżka do pliku YAML.

    Returns:
      JSON w formacie {"schema": "zawartość yamla"}
    """
    try:
        with open(plik_yaml, "r") as f:
            schemat_yaml = yaml.safe_load(f)

        # Konwersja YAML na JSON
        schemat_json = json.dumps({"schema": schemat_yaml})
        # print(schemat_json)
        return schemat_json

    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {plik_yaml}")
        return None
    except yaml.YAMLError as e:
        print(f"Błąd parsowania YAML: {e}")
        return None


# Wczytanie zmiennych środowiskowych z pliku .env
load_dotenv()

# Odczytanie kluczy API
JSON2VIDEO_API_KEY = os.getenv("JSON2VIDEO_API_KEY")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

gemini = GeminiApi(GEMINI_API_KEY)
taskName = "Jesteś kreatywnym asystentem AI, który pomaga w tworzeniu filmów."
task1 = {
    "task": taskName,
    "step": {
        "id": "topic and key words",
        "description": "Wymyśl temat krótkiego filmu (60 sekund) i wypisz listę słów kluczowych do przeszukania stocka Pexels. Film powinien być interesujący i angażujący, odpowiedni do wizualnej prezentacji i łatwy do zilustrowania. Słowa kluczowe powinny być zróżnicowane i odzwierciedlać różne aspekty tematu.",
    },
    "response_in_JSON_schema": {
        "topic": "[topic]",
        "picures_key_words": "word1 word2 word3",
        "movies_key_words": "word1 word2 word3",
    },
}

data1 = gemini.send_prompt(prompt=str(task1))

moveScenario = {"topic": data1["topic"], "pictures": [], "movies": []}
stockMedia = PexelsStockMedia(PEXELS_API_KEY)
# print(stockMedia.get_remaining_requests())

# photos = stockMedia.search_photos(data1["picures_key_words"], per_page=10)

# for _photo in photos.photos:
#     moveScenario["pictures"].append(
#         {
#             "url": _photo.src.original,
#             "alt": _photo.alt,
#             "width": _photo.width,
#             "height": _photo.height,
#             "avg_color": _photo.avg_color,
#         }
#     )
task_describe_pexels_video = {
    "task": taskName,
    "step": {
        "id": "Describe video",
        "description": "Describe the content and style of the video, what is happening, camera positon and movement.",
    },
    "response_schema": {"description": "[video description]"},
}


videos = stockMedia.search_videos(data1["movies_key_words"], per_page=1)
for _video in videos.videos:
    video_path = _video.video_files[0].link.split("/")[-1]
    with open(video_path, "wb") as f:
        f.write(requests.get(_video.video_files[0].link).content)
    video_file = gemini.send_file(GEMINI_API_KEY, video_path)
    data_video_description = gemini.send_prompt(
        [video_file, task_describe_pexels_video]
    )
    moveScenario["movies"].append(
        {
            "url": _video.video_files[0].link,
            "width": _video.width,
            "height": _video.height,
            "moviesDescritpion": data_video_description["description"],
        }
    )


print(moveScenario)
exit()


task3 = {
    "task": taskName,
    "step": {
        "id": "Create JSON for json2video API",
        "description": f"Użyj materiałów i opisów ze źródel do stworzenia scenariusza filmu o temacie {moveScenario['topic']}. Pamiętaj aby podać rozmiar dla każdego elementu zgodny z rozmiarem tworzonego filmu, ale nie rozciągaj zdjęć, jeśli trzeba to zrób zooma albo cropa. Przy każdym wykorzystanym źródle dodaj jego alt do danej sceny jako tekst.",
    },
    "sources": {"pictures": moveScenario["pictures"], "movies": moveScenario["movies"]},
    "film_duartion_in_seconds": 60,
    "schema_to_generate_JSON": yaml_do_json("src\Json2VideoSDK\schema.yaml"),
    "response_schema": {
        "schemaVideo": "[generated json]",
        "comments": "comment from AI",
    },
}
data3 = gemini.send_prompt(prompt=str(task3))
if "movie" in data3["schemaVideo"]:
    moveScenario["schemaVideo"] = data3["schemaVideo"]["movie"]
else:
    moveScenario["schemaVideo"] = data3["schemaVideo"]
moveScenario["comments"] = data3["comments"]
print(moveScenario)
json2VideoClient = Json2VideoClient(JSON2VIDEO_API_KEY)


print(json2VideoClient.create_movie(movie=moveScenario["schemaVideo"]))
print(json2VideoClient.get_movies("FQUK9UDCvDttgkQo"))
