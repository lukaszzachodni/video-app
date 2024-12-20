from typing import Dict, List, Union


class Subtitles:
    """
    A class representing the subtitles element schema for the JSON2Video API.
    """

    def __init__(
        self,
        type: str = "subtitles",
        captions: str = None,
        comment: str = None,
        language: str = "auto",
        model: str = None,
        settings: Dict = None,
    ):
        """
        Initializes a Subtitles object.

        Args:
            type (str): Type of the element. Defaults to "subtitles".
            captions (str): Captions to use as subtitles. Defaults to None.
            comment (str): Use it for your comments. Defaults to None.
            language (str): Language of the audio. Defaults to "auto".
            model (str): Model to use for transcription. Defaults to None.
            settings (Dict): Settings to customize the subtitles. Defaults to None.
        """
        self.type = type
        self.captions = captions
        self.comment = comment
        self.language = language
        self.model = model
        self.settings = settings if settings is not None else {}

    def set_captions(self, captions: str):
        """Sets the captions to use as subtitles."""
        self.captions = captions

    def set_comment(self, comment: str):
        """Sets the comment."""
        self.comment = comment

    def set_language(self, language: str):
        """Sets the language of the audio."""
        self.language = language

    def set_model(self, model: str):
        """Sets the model to use for transcription."""
        self.model = model

    def set_settings(self, settings: Dict):
        """Sets the settings to customize the subtitles."""
        self.settings = settings

    def to_dict(self) -> Dict:
        """Returns a dictionary representing the Subtitles object."""
        return {
            "type": self.type,
            "captions": self.captions,
            "comment": self.comment,
            "language": self.language,
            "model": self.model,
            "settings": self.settings,
        }
