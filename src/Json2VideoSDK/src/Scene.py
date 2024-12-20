from typing import List, Dict
from .Audio import Audio
from .Audiogram import Audiogram
from .Component import Component
from .HTML import HTML
from .Image import Image
from .Subtitles import Subtitles
from .Text import Text
from .Video import Video
from .Voice import Voice


class Scene:
    """
    A class representing the scene schema for the JSON2Video API.
    """

    def __init__(
        self,
        duration: float = -1,
        background_color: str = "#000000",
        cache: bool = True,
        comment: str = None,
        condition: str = None,
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
        id: str = None,
        transition: Dict = None,
        variables: Dict = None,
    ):
        """
        Initializes a Scene object.

        Args:
            duration (float): Sets the scene duration in seconds. Defaults to -1.
            background_color (str): A hexadecimal representation of a color or 'transparent'. Defaults to "#000000".
            cache (bool): Use the cached version of the scene if it's available. Defaults to True.
            comment (str): Used for adding your comments. Defaults to None.
            condition (str): Condition to be met for the scene to be rendered. Defaults to None.
            elements (List[Dict]): List of elements in the scene. Defaults to None.
            id (str): ID of the scene. Defaults to None.
            transition (Dict): Transition effect for the scene. Defaults to None.
            variables (Dict): Local variables of the scene. Defaults to None.
        """
        self.duration = duration
        self.background_color = background_color
        self.cache = cache
        self.comment = comment
        self.condition = condition
        self.elements = elements if elements is not None else []
        self.id = id
        self.transition = transition
        self.variables = variables if variables is not None else {}

    def set_duration(self, duration: float):
        """Sets the scene duration in seconds."""
        self.duration = duration

    def set_background_color(self, background_color: str):
        """Sets the background color of the scene."""
        self.background_color = background_color

    def set_cache(self, cache: bool):
        """Sets whether to use the cached version of the scene."""
        self.cache = cache

    def set_comment(self, comment: str):
        """Sets the comment."""
        self.comment = comment

    def set_condition(self, condition: str):
        """Sets the condition to be met for the scene to be rendered."""
        self.condition = condition

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

    def set_id(self, id: str):
        """Sets the ID of the scene."""
        self.id = id

    def set_transition(self, transition: Dict):
        """Sets the transition effect for the scene."""
        self.transition = transition

    def set_variables(self, variables: Dict):
        """Sets the local variables of the scene."""
        self.variables = variables

    def to_dict(self) -> Dict:
        """Returns a dictionary representing the Scene object."""
        return {
            "duration": self.duration,
            "background-color": self.background_color,
            "cache": self.cache,
            "comment": self.comment,
            "condition": self.condition,
            "elements": self.elementsToDict(),
            "id": self.id,
            "transition": self.transition,
            "variables": self.variables,
        }

    def elementsToDict(self):
        elementsDict = []
        for element in self.elements:
            elementsDict.append(element.to_dict())
        return elementsDict
