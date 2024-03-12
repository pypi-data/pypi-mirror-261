#!/usr/bin/env python

"""Axis class object definition.

In toyplot the Axis is defined in coordinates.py along with
Cartesian, whereas here we split it into a separate module.
"""

from typing import Mapping, Any, List, Sequence, Union, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import itertools
import numpy
import toyplot


@dataclass(repr=False)
class Helper:
    """Base class for Axis Helpers with a clean repr."""
    def __repr__(self):
        """Return dict-like repr of _{key} attributes in object"""
        data = {i[1:]: j for (i, j) in self.__dict__.items() if i[0] == "_"}
        x = ", ".join(f"{i}={j}" for i, j in data.items())
        return f"{self.__class__.__name__}({x})"


@dataclass(repr=False)
class Label(Helper):
    _text: str = None

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value


@dataclass(repr=False)
class Show(Helper):
    _show: bool = True

    @property
    def show(self) -> bool:
        """Control whether the domain should be made visible using the
        axis spine.
        """
        return self._show

    @show.setter
    def show(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("A boolean value is required.")
        self._show = value


@dataclass(repr=False)
class Near(Helper):
    _near: float = None

    @property
    def near(self) -> float:
        return self._near

    @near.setter
    def near(self, value: float) -> None:
        if value is None:
            self._near = None
        else:
            self._near = toyplot.units.convert(value, target="px", default="px")


@dataclass(repr=False)
class Far(Helper):
    _far: float = None

    @property
    def far(self) -> float:
        return self._far

    @far.setter
    def near(self, value: float) -> None:
        if value is None:
            self._far = None
        else:
            self._far = toyplot.units.convert(value, target="px", default="px")


@dataclass(repr=False)
class TextStyle(Helper):
    """Dictionary of CSS property-value pairs.

    Use the *style* property to control the text appearance.  The
    following CSS properties are allowed:

    * alignment-baseline
    * baseline-shift
    * fill
    * fill-opacity
    * font-size
    * font-weight
    * opacity
    * stroke
    * stroke-opacity
    * stroke-width
    * text-anchor
    * -toyplot-anchor-shift

    Note that when assigning to the *style* property, the properties you
    supply are merged with the existing properties.
    """
    _style: Mapping[str, Any] = field(default_factory=dict)

    @property
    def style(self) -> Mapping[str, Any]:
        return self._style

    @style.setter
    def style(self, value: Mapping) -> None:
        self._style = toyplot.style.combine(
            self._style,
            toyplot.style.require(
                value,
                allowed=toyplot.style.allowed.text,
            )
        )


@dataclass(repr=False)
class Offset(Helper):
    _offset: bool = True

    @property
    def offset(self) -> float:
        return self._offset

    @offset.setter
    def offset(self, value: float) -> None:
        if value is None:
            self._offset = None
        else:
            self._offset = toyplot.units.convert(value, target="px", default="px")


@dataclass(repr=False)
class Location(Helper):
    """Controls the position of ticks (and labels) relative to the axis.

    Allowed values are "above" (force labels to appear above the axis),
    "below" (the opposite), or `None` (use default, context-sensitive
    behavior).
    """
    _location: str = None

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, value: str) -> None:
        if value is None:
            self._location = None
        else:
            self._location = toyplot.require.value_in(
                value,
                [None, "above", "below"],
            )


@dataclass(repr=False)
class LineStyle(Helper):
    """Dictionary of CSS property-value pairs.

    Use the *style* property to control the appearance of the line. The
    following CSS properties are allowed:

    * opacity
    * stroke
    * stroke-dasharray
    * stroke-opacity
    * stroke-width

    Note that when assigning to the *style* property, the properties you
    supply are merged with the existing properties.
    """
    _style: Mapping[str, Any] = None

    @property
    def style(self) -> Mapping[str, Any]:
        return self._style

    @style.setter
    def style(self, value: Mapping) -> None:
        self._style = toyplot.style.combine(
            self._style,
            toyplot.style.require(
                value,
                allowed=toyplot.style.allowed.line,
            )
        )


@dataclass(repr=False)
class MinMax(Helper):
    _min: float = None
    _max: float = None

    @property
    def min(self) -> float:
        """Specify an explicit domain minimum for this axis.  By default
        the implicit domain minimum is computed from visible data.
        """
        return self._min

    @property
    def max(self) -> float:
        """Specify an explicit domain maximum for this axis.  By default
        the implicit domain maximum is computed from visible data.
        """
        return self._max

    @min.setter
    def min(self, value: float) -> None:
        self._min = value

    @max.setter
    def max(self, value: float) -> None:
        self._max = value


@dataclass(repr=False)
class DomainHelper(Show, MinMax, Helper):
    """Controls domain related behavior for this axis."""

    # override show.getter
    @property
    def show(self) -> bool:
        """Control whether the domain should be made visible using the
        axis spine.
        """
        return self._show

    # override show.setter
    @show.setter
    def show(self, value):
        toyplot.log.warning("Altering <axis>.domain.show is experimental.")
        self._show = True if value else False


@dataclass(repr=False)
class InteractiveCoordinatesLabelHelper(Show, TextStyle, Helper):
    """Controls the appearance and behavior of interactive coordinate labels."""
    def __post_init__(self):
        self.style = {
            "fill": "slategray",
            "font-size": "10px",
            "font-weight": "normal",
            "stroke": "none",
            "text-anchor": "middle",
        }


@dataclass(repr=False)
class InteractiveCoordinatesTickHelper(Show, LineStyle, Helper):
    """Controls the appearance and behavior of interactive coordinate ticks."""
    def __post_init__(self):
        self.style = {
            "stroke": "slategray",
            "stroke-width": 1.0,
        }


@dataclass(repr=False)
class InteractiveCoordinatesHelper(Show, Location, Helper):
    _label: InteractiveCoordinatesLabelHelper = (
        field(default_factory=InteractiveCoordinatesLabelHelper))
    _tick: InteractiveCoordinatesTickHelper = (
        field(default_factory=InteractiveCoordinatesTickHelper))

    @property
    def label(self) -> InteractiveCoordinatesLabelHelper:
        return self._label

    @property
    def tick(self) -> InteractiveCoordinatesTickHelper:
        return self._tick


@dataclass(repr=False)
class InteractiveHelper(Helper):
    """Controls interactive behavior for this axis."""
    _coordinates: InteractiveCoordinatesHelper = (
        field(default_factory=InteractiveCoordinatesHelper))

    @property
    def coordinates(self) -> InteractiveCoordinatesHelper:
        return self._coordinates


@dataclass(repr=False)
class LabelHelper(TextStyle, Offset, Label, Location, Helper):
    """Controls the appearance and behavior of an axis label."""
    def __post_init__(self):
        self.style = {
            "font-size": "12px",
            "font-weight": "bold",
            "stroke": "none",
            "text-anchor": "middle",
        }


@dataclass(repr=False)
class SpineHelper(Show, LineStyle, Helper):
    """Controls the appearance and behavior of an axis label."""
    _position: str = "low"

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value) -> None:
        """TODO: which other values are allowed or not?"""
        self._position = value


@dataclass(repr=True)
class TickProxy(Helper):
    _tick: Mapping = None
    _allowed: Mapping[str, Any] = None

    @property
    def style(self) -> Mapping[str, Any]:
        return self._tick.get("style", {})

    @style.setter
    def style(self, value: Mapping[str, Any]) -> None:
        self._tick["style"] = toyplot.style.combine(
            self.style,
            toyplot.style.require(value, allowed=self._allowed)
        )


@dataclass(repr=False)
class PerTickHelper(Helper):
    """Controls the appearanace and behavior of individual axis ticks."""
    _allowed: Mapping[str, Any] = field(default_factory=dict)
    _indices: Mapping = field(default_factory=defaultdict)
    _values: Mapping = field(default_factory=defaultdict)

    def __call__(self, index: int = None, value: float = None):
        if index is None and value is None:
            raise ValueError("Must specify tick index or value.")  # pragma: no cover
        if index is not None and value is not None:
            raise ValueError("Must specify either index or value, not both.")  # pragma: no cover
        if index is not None:
            return TickProxy(self._indices[index], self._allowed)
        elif value is not None:
            return TickProxy(self._values[value], self._allowed)

    def styles(self, values: Sequence[float]) -> List[Mapping]:
        """Return styles associated with tick values."""
        # get list of style dicts, or None, in indices order
        results = [
            self._indices[index].get("style", None) if index in self._indices
            else None for index in range(len(values))
        ]
        # get difference between 
        for value in self._values:
            deltas = numpy.abs(values - value)
            results[numpy.argmin(deltas)] = (
                self._values[value].get("style", None))
        return results


@dataclass(repr=False)
class TickLabelsHelper(Offset, Show, TextStyle, Helper):
    """Controls the appearance and behavior of axis tick labels."""
    _angle: float = 0
    _label: PerTickHelper = None

    def __post_init__(self):
        self._label = PerTickHelper(toyplot.style.allowed.text)
        self.style = {
            "font-size": "10px",
            "font-weight": "normal",
            "stroke": "none",
        }

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, value: float) -> None:
        self._angle = value

    @property
    def label(self):
        return self._label


@dataclass(repr=False)
class TicksHelper(Near, Far, Location, Show, LineStyle, Helper):
    """Controls the appearance and behavior of axis ticks."""
    _locator: toyplot.locator.TickLocator = None
    _angle: float = 0.

    _labels: TickLabelsHelper = None
    _tick: PerTickHelper = None

    def __post_init__(self):
        self.show = False
        self._tick = PerTickHelper(_allowed=toyplot.style.allowed.line)
        self._labels = TickLabelsHelper(_angle=self._angle)

    @property
    def labels(self) -> TickLabelsHelper:
        return self._labels

    @property
    def locator(self) -> toyplot.locator.TickLocator:
        return self._locator

    @locator.setter
    def locator(self, value: toyplot.locator.TickLocator) -> None:
        self._locator = value

    @property
    def tick(self) -> PerTickHelper:
        return self._tick


class Axis:
    """Axis for data projection and styling of ticks, labels, and spine.

    """
    def __init__(
        self,
        label: str = None,
        domain_min: float = None,
        domain_max: float = None,
        scale: str = "linear",
        show: bool = True,
        tick_angle: int = 0,
        tick_locator: toyplot.locator.TickLocator = None,
    ):

        self._finalized = None
        self._data_max = None
        self._data_min = None
        self._display_max = None
        self._display_min = None
        self._domain = DomainHelper(_min=domain_min, _max=domain_max)
        self._interactive = InteractiveHelper()
        self._label = LabelHelper()
        self._scale = None
        """: str arg converted to 'linear' or ('log', base) where base is a int."""
        self._show = show
        self._spine = SpineHelper()
        self._tick_labels = []
        self._tick_locations = []
        self._tick_titles = []
        self._ticks = TicksHelper(_tick=tick_locator, _angle=tick_angle)

        self.scale = scale

    @property
    def interactive(self) -> InteractiveHelper:
        return self._interactive

    @property
    def domain(self) -> DomainHelper:
        return self._domain

    @property
    def label(self) -> LabelHelper:
        return self._label

    @property
    def scale(self) -> str:
        return self._scale

    @property
    def show(self) -> bool:
        return self._show

    @property
    def spine(self) -> SpineHelper:
        return self._spine

    @property
    def ticks(self) -> TicksHelper:
        return self._ticks

    @show.setter
    def show(self, value: bool) -> None:
        self._show = value

    @scale.setter
    def scale(self, value: str) -> None:
        if value == "linear":
            self._scale = "linear"
            return
        elif value in ["log", "log10"]:
            self._scale = ("log", 10)
            return
        elif value == "log2":
            self._scale = ("log", 2)
            return
        elif isinstance(value, tuple) and len(value) == 2:
            scale, base = value
            if scale == "log":
                self._scale = ("log", base)
                return
        raise ValueError(
            """Scale must be "linear", "log", "log10", "log2" or a ("log", base) tuple.""")

    def _locator(self) -> toyplot.locator.TickLocator:
        """Return the tick locator set for this Axis, or an appropriate
        one, which can be used to get Tick locations given a domain.

        Exampel: This is called in Cartesian._finalize().
        """
        if self.ticks.locator is not None:
            return self.ticks.locator
        if self.scale == "linear":
            return toyplot.locator.Extended()
        if isinstance(self.scale, toyplot.projection.Projection):
            return toyplot.locator.Null()
        else:
            scale, base = self.scale
            if scale == "log":
                return toyplot.locator.Log(base=base)
        raise RuntimeError("Unable to create an appropriate locator.")  # pragma: no cover

    def _update_domain(self, values, display=True, data=True) -> None:
        """Update axis domain (display and/or data) given a set of
        values from the Marks mapped to Axis.

        This is called in Cartesian._finalize()
        """
        if display:
            self._display_min, self._display_max = toyplot.data.minimax(
                itertools.chain(
                    [self._display_min, self._display_max],
                    values
                )
            )
        if data:
            self._data_min, self._data_max = toyplot.data.minimax(
                itertools.chain(
                    [self._data_min, self._data_max],
                    values,
                )
            )

    def _finalize(
        self,
        x1: float,
        x2: float,
        y1: float,
        y2: float,
        offset: float,
        domain_min: float,
        domain_max: float,
        tick_locations: Sequence[float],
        tick_labels: Sequence[str],
        tick_titles: Sequence[str],
        default_tick_location,
        default_ticks_near,
        default_ticks_far,
        default_label_location,
    ):
        """Project position of spine, ticks and labels given the domain
        and range of data along the Axis.

        Example: This is called at the end of Cartesian._finalize().
        """
        # return if already finalized
        if self._finalized is not None:
            return self._finalized

        # store values to self
        self._x1 = x1
        """: xmin_range (canvas units)."""
        self._x2 = x2
        """: xmax_range (canvas units)."""
        self._y1 = y1
        """: ymin_range (canvas units)."""
        self._y2 = y2
        """: ymax_range (canvas units)."""
        self._offset = offset
        """: padding between axis and data Marks."""
        self._domain_min = domain_min
        """: domain_min (data units)."""
        self._domain_max = domain_max
        """: domain_max (data units)."""
        self._tick_locations = tick_locations
        """: Sequence of locations in data units."""
        self._tick_labels = tick_labels
        """: Sequence of str labels for ticks."""
        self._tick_titles = tick_titles
        """: Sequence of str titles for ticks."""
        self._tick_location = (
            default_tick_location if self.ticks.location is None
            else self.ticks.location
        )
        """: below or above."""
        self._ticks_near = (
            default_ticks_near if self.ticks.near is None
            else self.ticks.near
        )
        """: Length of tick mark inside axis in px units."""
        self._ticks_far = (
            default_ticks_far if self.ticks.far is None
            else self.ticks.far
        )
        """: Length of tick outside axis in px units."""
        self._tick_labels_location = self._tick_location
        """: below or above."""
        self._tick_labels_offset = (
            6 if self.ticks.labels.offset is None
            else self.ticks.labels.offset
        )
        """: padding between tick label and axis in px units."""
        self._label_location = (
            default_label_location if self.label.location is None
            else self.label.location
        )
        """: below or above."""
        self._label_offset = (
            22 if self.label.offset is None else self.label.offset
        )
        """: padding between axis label and axis in px units."""
        self._interactive_coordinates_location = (
            _opposite_location(self._tick_labels_location) if
            self.interactive.coordinates.location is None
            else self.interactive.coordinates.location
        )
        """: below or above."""

        # rowstack [min,min], [max, max]
        endpoints = numpy.row_stack(((x1, y1), (x2, y2)))
        # get matrix norm of [xlen, ylen]
        length = numpy.linalg.norm(endpoints[1] - endpoints[0])
        # get projection of domain_min to (0, length)
        self.projection = _create_projection(
            scale=self.scale,
            domain_min=domain_min,
            domain_max=domain_max,
            range_min=0.0,
            range_max=length,
        )

        self._finalized = self
        return self._finalized


def _create_projection(
    scale: Union[str, Tuple[str, int]],
    domain_min: float,
    domain_max: float,
    range_min: float,
    range_max: float,
) -> toyplot.projection.Projection:
    """Return a Projection to map data units to canvas units given scale type

    ...
    """
    # return the supplied projection
    if isinstance(scale, toyplot.projection.Projection):
        return scale

    # return a linear projection
    args = (domain_min, domain_max, range_min, range_max)
    if scale == "linear":
        return toyplot.projection.linear(*args)

    # return a log projection. log scale format: ('log', int)
    scale, base = scale
    return toyplot.projection.log(base, *args)


def _opposite_location(location: str) -> str:
    """Return the opposite of current location arg."""
    return "above" if location == "below" else "below"


if __name__ == "__main__":

    ax = Axis()
    print(ax)

    ax._finalize(
        x1=0,
        x2=500,
        y1=0,
        y2=0,
        offset=0,
        domain_min=0,
        domain_max=1,
        tick_locations=[0, 0.5, 1],
        tick_labels=['0', '0.5', '1'],
        tick_titles=[],
        default_tick_location="below",
        default_ticks_far=5,
        default_ticks_near=0,
        default_label_location="below",
    )
    print(ax.projection([0, 1]))