import google.generativeai as genai
import json

import time


class GeminiApi:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def send_prompt(self, prompt) -> str:
        response = self.model.generate_content(prompt).text
        # print(response)
        return json.loads(response.replace("`", "").replace("json", ""))

    def send_file(self, api_key, file_path: str) -> str:
        video_file = genai.upload_file(path=file_path)
        while video_file.state.name == "PROCESSING":
            print(".", end="")
            time.sleep(10)
            video_file = genai.get_file(video_file.name)
        if video_file.state.name == "FAILED":
            raise ValueError(video_file.state.name)
        # print(video_file)
        return video_file
