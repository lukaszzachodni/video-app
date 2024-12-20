from typing import List, Dict

from .Audio import Audio
from .Audiogram import Audiogram
from .Component import Component
from .HTML import HTML
from .Image import Image
from .Scene import Scene
from .Subtitles import Subtitles
from .Text import Text
from .Video import Video
from .Voice import Voice


class Movie:
    """
    A class representing the movie schema for the JSON2Video API.
    """

    def __init__(
        self,
        scenes: List[Scene] = [],
        resolution: str = "custom",
        width: int = 640,
        height: int = 360,
        cache: bool = True,
        comment: str = None,
        draft: bool = True,
        elements: List[
            Video
            | Image
            | Text
            | HTML
            | Component
            | Audio
            | Voice
            | Audiogram
            | Subtitles
        ] = None,
        exports: List[Dict] = None,
        id: str = None,
        quality: str = "high",
        variables: Dict = None,
    ):
        """
        Initializes a Movie object.

        Args:
            scenes (List[Dict]): List of scenes in the movie.
            resolution (str): Resolution of the movie. Defaults to "custom".
            width (int): Width of the movie. Defaults to 640.
            height (int): Height of the movie. Defaults to 360.
            cache (bool): Use the cached version of the movie if it's available. Defaults to True.
            comment (str): Used for adding your comments. Defaults to None.
            draft (bool): Set to true to add a watermark to the movie. Defaults to True.
            elements (List[Dict]): List of elements in the movie. Defaults to None.
            exports (List[Dict]): List of exports for the movie. Defaults to None.
            id (str): Movie ID string. Defaults to None.
            quality (str): Quality of the final rendered movie. Defaults to "high".
            variables (Dict): Variables of the template. Defaults to None.
        """
        self.scenes = scenes
        self.resolution = resolution
        self.width = width
        self.height = height
        self.cache = cache
        self.comment = comment
        self.draft = draft
        self.elements = elements if elements is not None else []
        self.exports = exports if exports is not None else []
        self.id = id
        self.quality = quality
        self.variables = variables if variables is not None else {}

    def add_scene(self, scene: Scene):
        """Adds a scene to the list of scenes."""
        self.scenes.append(scene)

    def set_resolution(self, resolution: str):
        """Sets the resolution of the movie."""
        self.resolution = resolution

    def set_width(self, width: int):
        """Sets the width of the movie."""
        self.width = width

    def set_height(self, height: int):
        """Sets the height of the movie."""
        self.height = height

    def set_cache(self, cache: bool):
        """Sets whether to use the cached version of the movie."""
        self.cache = cache

    def set_comment(self, comment: str):
        """Sets the comment."""
        self.comment = comment

    def set_draft(self, draft: bool):
        """Sets whether to add a watermark to the movie."""
        self.draft = draft

    def add_element(
        self,
        element: (
            Video
            | Image
            | Text
            | HTML
            | Component
            | Audio
            | Voice
            | Audiogram
            | Subtitles
        ),
    ):
        """Adds an element to the list of elements."""
        self.elements.append(element)

    def add_export(self, export: Dict):
        """Adds an export to the list of exports."""
        self.exports.append(export)

    def set_id(self, id: str):
        """Sets the movie ID string."""
        self.id = id

    def set_quality(self, quality: str):
        """Sets the quality of the final rendered movie."""
        self.quality = quality

    def set_variables(self, variables: Dict):
        """Sets the variables of the template."""
        self.variables = variables

    def to_dict(self) -> Dict:
        """Returns a dictionary representing the Movie object."""
        return {
            "scenes": self.scenesToDict(),
            "resolution": self.resolution,
            "width": self.width,
            "height": self.height,
            "cache": self.cache,
            "comment": self.comment,
            "draft": self.draft,
            "elements": self.elementsToDict(),
            "exports": self.exports,
            "id": self.id,
            "quality": self.quality,
            "variables": self.variables,
        }

    def scenesToDict(self):
        scenesDict = []
        for scene in self.scenes:
            scenesDict.append(scene.to_dict())
        return scenesDict

    def elementsToDict(self):
        elementsDict = []
        for element in self.elements:
            elementsDict.append(element.to_dict())
        return elementsDict
