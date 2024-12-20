from typing import Dict


class Voice:
    """
    A class representing the voice element schema for the JSON2Video API.
    """

    def __init__(
        self,
        text: str,
        type: str = "voice",
        cache: bool = True,
        comment: str = None,
        condition: str = None,
        connection: str = None,
        duration: float = -1,
        extra_time: float = 0,
        fade_in: float = None,
        fade_out: float = None,
        id: str = None,
        model: str = None,
        muted: bool = False,
        start: float = 0,
        variables: Dict = None,
        voice: str = None,
        volume: float = 1,
        z_index: int = 0,
    ):
        """
        Initializes a Voice object.

        Args:
            text (str): The sentence or sentences to be converted to voice audio.
            type (str): Type of the element. Defaults to "voice".
            cache (bool): Use the cached version of the element if its available. Defaults to True.
            comment (str): Used for adding your comments. Defaults to None.
            condition (str): Condition to be met for the element to be rendered. Defaults to None.
            connection (str): Connection ID to use for generation. Defaults to None.
            duration (float): Element's duration in seconds. Defaults to -1.
            extra_time (float): Element's time span added after the playback. Defaults to 0.
            fade_in (float): Adds a fade in effect to the element. Value in seconds. Defaults to None.
            fade_out (float): Adds a fade out effect to the element. Value in seconds. Defaults to None.
            id (str): ID of the element. Defaults to None.
            model (str): The model to use for generation. Defaults to None.
            muted (bool): Mutes the audio. Defaults to False.
            start (float): Element's starting time in seconds relative to the container scene. Defaults to 0.
            variables (Dict): Local variables of the element. Defaults to None.
            voice (str): The voice name to be used. Defaults to None.
            volume (float): Volume gain of the audio. Defaults to 1.
            z_index (int): Element's z-index. Defaults to 0.
        """
        self.text = text
        self.type = type
        self.cache = cache
        self.comment = comment
        self.condition = condition
        self.connection = connection
        self.duration = duration
        self.extra_time = extra_time
        self.fade_in = fade_in
        self.fade_out = fade_out
        self.id = id
        self.model = model
        self.muted = muted
        self.start = start
        self.variables = variables if variables is not None else {}
        self.voice = voice
        self.volume = volume

        self.z_index = z_index

    # ... (setter methods for each attribute) ...
    def set_id(self, id: str):
        """Sets the ID of the voice."""
        self.id = id

    def set_model(self, model: str):
        """Sets the model."""
        self.model = model

    def set_muted(self, muted: bool):
        """Sets mute status."""
        self.muted = muted

    def set_start(self, start: float):
        """Sets start time."""
        self.start = start

    def set_variables(self, variables: Dict):
        """Sets variables."""
        self.variables = variables

    def set_voice(self, voice: str):
        """Sets voice."""
        self.voice = voice

    def set_volume(self, volume: float):
        """Sets volume."""
        self.volume = volume

    def set_z_index(self, z_index: int):
        """Sets z-index."""
        self.z_index = z_index

    def to_dict(self) -> Dict:
        """Returns a dictionary representing the Voice object."""
        return {
            "text": self.text,
            "type": self.type,
            "cache": self.cache,
            "comment": self.comment,
            "condition": self.condition,
            "connection": self.connection,
            "duration": self.duration,
            "extra_time": self.extra_time,
            "fade_in": self.fade_in,
            "fade_out": self.fade_out,
            "id": self.id,
            "model": self.model,
            "muted": self.muted,
            "start": self.start,
            "variables": self.variables,
            "voice": self.voice,
            "volume": self.volume,
            "z_index": self.z_index,
        }
