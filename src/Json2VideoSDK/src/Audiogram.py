from typing import Dict


class Audiogram:
    """
    A class representing the audiogram element schema for the JSON2Video API.
    """

    def __init__(
        self,
        type: str = "audiogram",
        amplitude: float = 5,
        cache: bool = True,
        chroma_key: Dict = None,
        color: str = None,
        comment: str = None,
        condition: str = None,
        correction: Dict = None,
        crop: Dict = None,
        duration: float = -2,
        extra_time: float = 0,
        fade_in: float = None,
        fade_out: float = None,
        flip_horizontal: bool = False,
        flip_vertical: bool = False,
        height: int = -1,
        id: str = None,
        mask: str = None,
        opacity: float = 0.5,
        pan: str = None,
        pan_crop: bool = True,
        pan_distance: float = 0.1,
        position: str = "custom",
        rotate: Dict = None,
        scale: Dict = None,  # Deprecated, use width and height instead
        start: float = 0,
        variables: Dict = None,
        width: int = -1,
        x: int = 0,
        y: int = 0,
        z_index: int = 0,
        zoom: int = 0,
    ):
        """
        Initializes an Audiogram object.

        Args:
            type (str): Type of the element. Defaults to "audiogram".
            amplitude (float): Relative amplitude of the audiogram. Defaults to 5.
            cache (bool): Use the cached version of the element if its available. Defaults to True.
            chroma_key (Dict): Allows to define a color (or a range of colors) that will be converted to transparent. Defaults to None.
            color (str): Color of the audiogram waves in hexadecimal format. Defaults to None.
            comment (str): Used for adding your comments. Defaults to None.
            condition (str): Condition to be met for the element to be rendered. Defaults to None.
            correction (Dict): Allows to adjust the contrast, brightness, saturation and gamma of the element. Defaults to None.
            crop (Dict): Crops the element. Defaults to None.
            duration (float): Element's duration in seconds. Defaults to -2.
            extra_time (float): Element's time span added after the playback. Defaults to 0.
            fade_in (float): Adds a fade in effect to the element. Value in seconds. Defaults to None.
            fade_out (float): Adds a fade out effect to the element. Value in seconds. Defaults to None.
            flip_horizontal (bool): Flips the element horizontally. Defaults to False.
            flip_vertical (bool): Flips the element vertically. Defaults to False.
            height (int): Sets the height of the element. Defaults to -1.
            id (str): ID of the element. Defaults to None.
            mask (str): URL to a PNG or video file defining a mask for the element. Defaults to None.
            opacity (float): Opacity of the audiogram. Defaults to 0.5.
            pan (str): Pans the element to the specified direction. Defaults to None.
            pan_crop (bool): Enable or disable the crop effect when panning. Defaults to True.
            pan_distance (float): Pans the element to the specified distance. Defaults to 0.1.
            position (str): Sets the element position in the scene. Defaults to "custom".
            rotate (Dict): Rotates the element. Defaults to None.
            scale (Dict): This property is deprecated. Use 'width' and 'height' instead. Defaults to None.
            start (float): Element's starting time in seconds relative to the container scene. Defaults to 0.
            variables (Dict): Local variables of the element. Defaults to None.
            width (int): Sets the width of the element. Defaults to -1.
            x (int): Sets the horizontal position of the element in the scene. Defaults to 0.
            y (int): Sets the vertical position of the element in the scene. Defaults to 0.
            z_index (int): Element's z-index. Defaults to 0.
            zoom (int): Zooms the element with the specified level percentage. Defaults to 0.
        """
        self.type = type
        self.amplitude = amplitude
        self.cache = cache
        self.chroma_key = chroma_key
        self.color = color
        self.comment = comment
        self.condition = condition
        self.correction = correction
        self.crop = crop
        self.duration = duration
        self.extra_time = extra_time
        self.fade_in = fade_in
        self.fade_out = fade_out
        self.flip_horizontal = flip_horizontal
        self.flip_vertical = flip_vertical
        self.height = height
        self.id = id
        self.mask = mask
        self.opacity = opacity
        self.pan = pan
        self.pan_crop = pan_crop
        self.pan_distance = pan_distance
        self.position = position
        self.rotate = rotate
        self.scale = scale
        self.start = start
        self.variables = variables if variables is not None else {}
        self.width = width
        self.x = x
        self.y = y
        self.z_index = z_index
        self.zoom = zoom

    def set_id(self, id: str):
        """Sets the ID of the audiogram."""
        self.id = id

    def set_mask(self, mask: str):
        """Sets the mask."""
        self.mask = mask

    def set_pan(self, pan: str):
        """Sets panning."""
        self.pan = pan

    def set_pan_crop(self, pan_crop: bool):
        """Sets pan crop."""
        self.pan_crop = pan_crop

    def set_pan_distance(self, pan_distance: float):
        """Sets pan distance."""
        self.pan_distance = pan_distance

    def set_position(self, position: str):
        """Sets position."""
        self.position = position

    def set_rotate(self, rotate: Dict):
        """Sets rotation."""
        self.rotate = rotate

    def set_scale(self, scale: Dict):
        """Sets scale (deprecated)."""
        self.scale = scale

    def set_start(self, start: float):
        """Sets start time."""
        self.start = start

    def set_variables(self, variables: Dict):
        """Sets variables."""
        self.variables = variables

    def set_width(self, width: int):
        """Sets width."""
        self.width = width

    def set_x(self, x: int):
        """Sets x coordinate."""
        self.x = x

    def set_y(self, y: int):
        """Sets y coordinate."""
        self.y = y

    def set_z_index(self, z_index: int):
        """Sets z-index."""
        self.z_index = z_index

    def to_dict(self) -> Dict:
        """Returns a dictionary representing the Audiogram object."""
        return {
            "type": self.type,
            "amplitude": self.amplitude,
            "cache": self.cache,
            "chroma_key": self.chroma_key,
            "color": self.color,
            "comment": self.comment,
            "condition": self.condition,
            "correction": self.correction,
            "crop": self.crop,
            "duration": self.duration,
            "extra_time": self.extra_time,
            "fade_in": self.fade_in,
            "fade_out": self.fade_out,
            "flip_horizontal": self.flip_horizontal,
            "flip_vertical": self.flip_vertical,
            "height": self.height,
            "id": self.id,
            "mask": self.mask,
            "opacity": self.opacity,
            "pan": self.pan,
            "pan_crop": self.pan_crop,
            "pan_distance": self.pan_distance,
            "position": self.position,
            "rotate": self.rotate,
            "scale": self.scale,
            "start": self.start,
            "variables": self.variables,
            "width": self.width,
            "x": self.x,
            "y": self.y,
            "z_index": self.z_index,
            "zoom": self.zoom,
        }
