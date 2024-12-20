from typing import Dict


class Audio:
    """
    A class representing the audio element schema for the JSON2Video API.
    """

    def __init__(
        self,
        src: str,
        type: str = "audio",
        cache: bool = True,
        comment: str = None,
        condition: str = None,
        duration: float = -1,
        extra_time: float = 0,
        fade_in: float = None,
        fade_out: float = None,
        id: str = None,
        loop: int = 1,
        muted: bool = False,
        seek: float = 0,
        start: float = 0,
        variables: Dict = None,
        volume: float = 1,
        z_index: int = 0,
    ):
        """
        Initializes an Audio object.

        Args:
            src (str): URL to the asset file. Audios can be in MP3, WAV or any common audio format.
            type (str): Type of the element. Defaults to "audio".
            cache (bool): Use the cached version of the element if its available. Defaults to True.
            comment (str): Used for adding your comments. Defaults to None.
            condition (str): Condition to be met for the element to be rendered. Defaults to None.
            duration (float): Element's duration in seconds. Defaults to -1.
            extra_time (float): Element's time span added after the playback. Defaults to 0.
            fade_in (float): Adds a fade in effect to the element. Value in seconds. Defaults to None.
            fade_out (float): Adds a fade out effect to the element. Value in seconds. Defaults to None.
            id (str): ID of the element. Defaults to None.
            loop (int): Sets the number of loops the audio to play. Defaults to 1.
            muted (bool): Mutes the audio. Defaults to False.
            seek (float): Seek to the specified time in seconds relative to the begining of the asset. Defaults to 0.
            start (float): Element's starting time in seconds relative to the container scene. Defaults to 0.
            variables (Dict): Local variables of the element. Defaults to None.
            volume (float): Volume gain of the audio. Defaults to 1.
            z_index (int): Element's z-index. Defaults to 0.
        """
        self.src = src
        self.type = type
        self.cache = cache
        self.comment = comment
        self.condition = condition
        self.duration = duration
        self.extra_time = extra_time
        self.fade_in = fade_in
        self.fade_out = fade_out
        self.id = id
        self.loop = loop
        self.muted = muted
        self.seek = seek
        self.start = start
        self.variables = variables if variables is not None else {}
        self.volume = volume
        self.z_index = z_index

    # ... (setter methods for each attribute) ...
    def set_id(self, id: str):
        """Sets the ID of the audio."""
        self.id = id

    def set_loop(self, loop: int):
        """Sets the number of loops."""
        self.loop = loop

    def set_muted(self, muted: bool):
        """Sets mute status."""
        self.muted = muted

    def set_seek(self, seek: float):
        """Sets seek time."""
        self.seek = seek

    def set_start(self, start: float):
        """Sets start time."""
        self.start = start

    def set_variables(self, variables: Dict):
        """Sets variables."""
        self.variables = variables

    def set_volume(self, volume: float):
        """Sets volume."""
        self.volume = volume

    def set_z_index(self, z_index: int):
        """Sets z-index."""
        self.z_index = z_index

    def to_dict(self) -> Dict:
        """Returns a dictionary representing the Audio object."""
        return {
            "src": self.src,
            "type": self.type,
            "cache": self.cache,
            "comment": self.comment,
            "condition": self.condition,
            "duration": self.duration,
            "extra_time": self.extra_time,
            "fade_in": self.fade_in,
            "fade_out": self.fade_out,
            "id": self.id,
            "loop": self.loop,
            "muted": self.muted,
            "seek": self.seek,
            "start": self.start,
            "variables": self.variables,
            "volume": self.volume,
            "z_index": self.z_index,
        }
