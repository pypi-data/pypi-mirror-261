#!/usr/bin/env python

"""...

"""

from __future__ import annotations
# from typing import Optional
import itertools

import numpy as np
import toytree
import toyplot
from toyplot.mark import Mark
from toyplot.coordinates import Axis
# from toyplot.html import RenderContext


class LabelHelper:
    """Controls the appearance and behavior of a Cartesian coordinate system label."""
    def __init__(self, text, style):
        self._style = {}
        self._text = None

        self.style = {
            "font-size": "14px",
            "font-weight": "bold",
            "stroke": "none",
            "text-anchor": "middle",
            "-toyplot-vertical-align": "bottom",
        }
        self.style = style
        self.text = text
        self.offset = 8


class Cart:
    """...

    Note
    ----
    See constructor function `canvas.cartesian` for user-facing func
    to create Cartesian axes.
    """
    def __init__(
        self,
        aspect: str = None,
        hyperlink: str = None,
        label: str = None,
        padding: int = 10,
        palette: toyplot.color.Palette = None,
        scenegraph: toyplot.scenegraph.SceneGraph = None,
        show: bool = True,
        xaxis: Axis = None,
        xlabel: str = None,
        xmax: float = None,
        xmax_range: float = None,
        xmin: float = None,
        xmin_range: float = None,
        xscale: str = "linear",
        xshow: bool = True,
        xticklocator: toyplot.locator.TickLocator = None,
        yaxis: Axis = None,
        ylabel: str = None,
        ymax: float = None,
        ymax_range: float = None,
        ymin: float = None,
        ymin_range: float = None,
        yscale: str = "linear",
        yshow: bool = True,
        yticklocator: toyplot.locator.TickLocator = None,
    ):
        self._finalized = Cart
        """: This Cartesian object after ._finalize() has been run on it."""
        self._scenegraph = scenegraph
        """: Graph connecting Canvas, Cartesian, and Marks. From Canvas."""

        self._xmin_range: float = xmin_range
        """: min range of data given Canvas dimensions and margin."""
        self._xmax_range: float = xmax_range
        """: max range of data given Canvas dimensions and margin."""
        self._ymin_range: float = ymin_range
        """: min range of data given Canvas dimensions and margin."""
        self._ymax_range: float = ymax_range
        """: max range of data given Canvas dimensions and margin."""

        self._aspect = aspect
        """: aspect options are 'fit-range' or None."""
        self._hyperlink = hyperlink
        """: str URI for axis ..."""
        self._label = LabelHelper(text=label, style={})
        """: Axes main label object w/ .text and .style attrs."""
        self._padding = toyplot.units.convert(padding, target="px", default="px")
        """: Padding between axes and data stored in px units."""
        self._palette = toyplot.color.Palette() if palette is None else palette
        """: Palette of colors used for sequentially added Marks."""

        # separate cycling palettes for different Mark types
        self._bar_colors = itertools.cycle(self._palette)
        self._ellipse_colors = itertools.cycle(self._palette)
        self._fill_colors = itertools.cycle(self._palette)
        self._graph_colors = itertools.cycle(self._palette)
        self._plot_colors = itertools.cycle(self._palette)
        self._scatterplot_colors = itertools.cycle(self._palette)
        self._rect_colors = itertools.cycle(self._palette)
        self._text_colors = itertools.cycle(self._palette)

        # set args to x Axis object
        self.x = xaxis if xaxis is not None else Axis()
        """: x Axis object for horizontal dimension of Cartesian."""
        self.x.show = xshow
        self.x.label.text = xlabel
        self.x.domain.min = xmin
        self.x.domain.max = xmax
        self.x.ticks.locator = xticklocator
        self.x.scale = xscale

        # set args to y Axis object
        self.y = yaxis if xaxis is not None else Axis()
        """: y Axis object for vertical dimension of Cartesian."""
        self.y.show = yshow
        self.y.label.text = ylabel
        self.y.domain.min = ymin
        self.y.domain.max = ymax
        self.y.ticks.locator = yticklocator
        self.y.scale = yscale

        # private attrs used in .finalize() to fit data & text extents
        self._expand_domain_range_x: np.ndarray = None
        """: array shape=(3, nMarks) w/ [position, left-extent, right-extent]"""
        self._expand_domain_range_y: np.ndarray = None
        """: array shape=(3, nMarks) w/ [position, top-extent, bottom-extent]"""

    # exposed property for set/get padding in px units
    @property
    def padding(self) -> float:
        return self._padding

    @padding.setter
    def padding(self, value: float) -> None:
        self._padding = toyplot.units.convert(value, target="px", default="px")

    # exposed property for set/get show boolean
    @property
    def show(self) -> bool:
        return self._show

    @show.setter
    def show(self, value: bool) -> None:
        self._show = value

    # exposed property for set/get hyperlink URI
    @property
    def hyperlink(self) -> str:
        return self._hyperlink

    @hyperlink.setter
    def hyperlink(self, value: str) -> None:
        self._hyperlink = value

    # exposed property for set/get aspect str
    @property
    def aspect(self) -> str:
        return self._aspect

    @aspect.setter
    def aspect(self, value: str) -> None:
        if value not in [None, "fit-range"]:
            raise ValueError(
                f"Unknown aspect value: {value}. Options are 'fit-range' or None.")
        self._aspect = value

    # private functions to set/get xmin_range used internally here.
    @property
    def xmin_range(self) -> float:
        return self._xmin_range

    @property
    def xmax_range(self) -> float:
        return self._xmax_range

    @property
    def ymin_range(self) -> float:
        return self._ymin_range

    @property
    def ymax_range(self) -> float:
        return self._ymax_range

    @xmin_range.setter
    def xmin_range(self, value: float) -> None:
        self._xmin_range = value

    @xmax_range.setter
    def xmax_range(self, value: float) -> None:
        self._xmax_range = value

    @ymin_range.setter
    def ymin_range(self, value: float) -> None:
        self._ymin_range = value

    @ymax_range.setter
    def ymax_range(self, value: float) -> None:
        self._ymax_range = value

    def project(self, axis, values) -> np.ndarray:
        pass

    def add_mark(self, mark):
        """Add a mark to the axes.

        This is only of use when creating your own custom Toyplot marks.  It is
        not intended for end-users.

        Example
        -------
        >>> mark = axes.add(MyCustomMark())

        Parameters
        ----------
        mark: :class:`toyplot.mark.Mark`, required

        Returns
        -------
        mark: :class:`toyplot.mark.Mark`
        """
        self._scenegraph.add_edge(self, "render", mark)
        self._scenegraph.add_edge(self.x, "map", mark)
        self._scenegraph.add_edge(self.y, "map", mark)
        return mark

    def share(self):
        pass

    # ----------------------------------------------------------------
    # Plotting functions that can be called from a Cart to create Marks
    # are located in cartesian_funcs.py and wrapped using functools.
    # ----------------------------------------------------------------
    # bars()
    # color_scale()
    # ellipse()
    # fill()
    # graph()
    # hlines()
    # plot()
    # rectangle()
    # scatterplot()
    # text()
    # vlines()
    # ----------------------------------------------------------------

    def _finalize(self) -> None:
        """...

        """
        if self._finalized is not None:
            return self._finalized

        # Begin with the implicit domain defined by our children.
        for name, axis in zip(("x", "y"), (self.x, self.y)):
            expand = []

            # iterate over Marks mapped to this axis
            for child in self._scenegraph.targets(axis, "map"):

                # get finalized version of Mark
                child = child._finalize()
                if child is not None:

                    # update display to fit Mark, and data if not annotation
                    axis._update_domain(
                        child.domain(name),
                        display=True,               # updates axis._display_[min,max]
                        data=not child.annotation,  # updates axis._data_[min,max]
                    )

                    # get coordinates and extents of child marks
                    (x, y), (left, right, top, bottom) = child.extents(["x", "y"])

                    # expand domain x range for mark positions
                    if name == "x":
                        expand.append([x, left, right])
                    else:
                        expand.append([y, top, bottom])

            # store x position and extents of Marks as arrays
            if expand:
                if name == "x":
                    self._expand_domain_range_x = np.concatenate(expand, axis=1)
                else:
                    self._expand_domain_range_y = np.concatenate(expand, axis=1)

        return self._finalized


if __name__ == "__main__":

    # from toytree.drawing.src.cartesian import Cart
    canvas = toyplot.Canvas()

    dims = ["xmin_range", "xmax_range", "ymin_range", "ymax_range"]
    layout = toyplot.layout.region(0, canvas._width, 0, canvas._height)
    kwargs = dict(zip(dims, layout))
    axes = Cart(scenegraph=canvas._scenegraph, **kwargs)
    canvas._scenegraph.add_edge(canvas, "render", axes)

    m0 = axes.text(0, 0, "hello world")
    m1 = axes.text(1, 1, "hello world")

    print(axes._expand_domain_range_x)
    print(axes._expand_domain_range_y)