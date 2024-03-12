#!/usr/bin/env python

"""Cartesian class object.

In toyplot the Cartesian class is defined in coordinates.py with many
other objects and methods. Here it is isolated and simplified for
easier debugging.

TODO
----
- break finalize into several smaller functions.
- copy or inherit render function from toyplot.coordinates.Cartesian

"""

from __future__ import annotations
from typing import Optional, Sequence, Mapping, Any
from dataclasses import dataclass
import itertools
from loguru import logger

import numpy as np
import toyplot
import toyplot.text
from toyplot.mark import Mark
from toyplot.axis import Axis, LabelHelper


@dataclass(repr=False)
class CartesianLabelHelper(LabelHelper):
    """Controls the appearance and behavior of an Cartesian label."""
    def __post_init__(self):
        self.style = {
            "font-size": "14px",
            "font-weight": "bold",
            "stroke": "none",
            "text-anchor": "middle",
            "-toyplot-vertical-align": "bottom",
        }
        self.offset = 8


class Cartesian(toyplot.coordinates.Cartesian):
    """Cartesian class to map Marks on cartesian axes.

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
        self._finalized = None
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

        self._show = show
        """: Show or suppress both Cartesian axes."""
        self._aspect = aspect
        """: aspect options are 'fit-range' or None."""
        self._hyperlink = hyperlink
        """: str URI for axis ..."""
        self._label = CartesianLabelHelper(_text=label, _style={})
        """: Axes main label object w/ .text and .style attrs."""
        self._padding = toyplot.units.convert(padding, target="px", default="px")
        """: Padding between axes and data stored in px units."""
        self._palette = toyplot.color.Palette() if palette is None else palette
        """: Palette of colors used for sequentially added Marks."""

        # distinct cycling palettes for different Mark types
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

    def project(self, axis: str, values: np.ndarray) -> np.ndarray:
        """Project a set of domain values to coordinate system range values.

        Note that this API is intended for advanced users creating their own
        custom marks, end-users should never need to use it.

        Parameters
        ----------
        axis: "x" or "y", required
            The axis to be projected
        values: array-like, required
            The values to be projected

        Returns
        -------
        projected: :class:`numpy.ndarray`
            The projected values.
        """
        if axis == "x":
            return self._x_projection(values)
        elif axis == "y":
            return self._y_projection(values)
        raise ValueError("Unexpected axis: %s" % axis)

    def add_mark(self, mark: Mark) -> Mark:
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
        """TODO later."""
        pass

    # ----------------------------------------------------------------
    # Plotting functions that can be called from a Cart to create Marks
    # are located in cartesian2_funcs.py and wrapped using functools.
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
        """Update domain and range to fit Marks mapped to Cartesian axes."""
        # if already finalized then skip.
        if self._finalized is not None:
            return self._finalized

        # get Marks mapped to 'x' or 'y' (all are mapped to both for Cartesian)
        marks = self._scenegraph.targets(self.x, "map")

        # dict to store extents in each direction
        keys = ("x", "y", "left", "right", "top", "bottom")
        expand = {i: [] for i in keys}

        # iterate over marks updating domain and getting extents
        for mark in marks:

            # get finalized version of Mark
            fmark = mark._finalize()
            if fmark is not None:

                # get coordinates and extents of child marks
                (x, y), (left, right, top, bottom) = mark.extents(["x", "y"])

                # updates Axis._display_[min,max] and Axis._data_[min,max]
                # to fit Mark. Data only updated if not annotation.
                for ax in ('x', 'y'):
                    getattr(self, ax)._update_domain(
                        mark.domain(ax),
                        display=True,
                        data=not mark.annotation
                    )

                # store info to expand range to fit extents
                for key, val in zip(keys, (x, y, left, right, top, bottom)):
                    expand[key].extend(val)

        # convert expand values into arrays and store to self, else None
        for key, val in expand.items():
            # if not val:
            #     val = None
            attr = f"_expand_domain_range_{key}"
            setattr(self, attr, np.array(val))

            # extents...
            logger.info(f"{key}, {val}")

        # get implicit domain from data (data units), or use origin.
        xdomain_min = self.x._display_min if self.x._display_min else 0
        xdomain_max = self.x._display_max if self.x._display_max else 0
        ydomain_min = self.y._display_min if self.y._display_min else 0
        ydomain_max = self.y._display_max if self.y._display_max else 0

        # ensure domain is not empty (e.g., min and max 0).
        if xdomain_min == xdomain_max:
            xdomain_min -= 0.5
            xdomain_max += 0.5
        if ydomain_min == ydomain_max:
            ydomain_min -= 0.5
            ydomain_max += 0.5

        # ----------------- canvas width --------------------------
        # ------- self._xmin_range
        #                                  self._xmax_range -------
        #              |----------- range -----------|
        # margin + pad + ext-left + data + ext-right + pad + margin
        # note: margin left does affect _xmax_range, only margin right

        # get projection function to translate current domain in data
        # units to range in canvas (e.g., px) units. Example, project
        # data domain (0, 1) to range (50, 350) on a Canvas with
        # width=400 and margin=50. Padding is not relevant here.
        self.x_projection = _create_projection(
            self.x.scale,
            domain_min=xdomain_min,
            domain_max=xdomain_max,
            range_min=self._xmin_range,
            range_max=self._xmax_range,
        )
        logger.info(f"orig domain = {xdomain_min}, {xdomain_max}")
        logger.info(f"orig data domain to px: {self.x_projection([xdomain_min, xdomain_max])}")

        # get range needed to fit marks on the new expanded x range
        range_x = self.x_projection(self._expand_domain_range_x)
        logger.info(f"range_x: {range_x}")#self.x_projection([xdomain_min, xdomain_max])}")

        # get range left and right of marks needed to fit their extents
        range_left = range_x + self._expand_domain_range_left
        range_right = range_x + self._expand_domain_range_right
        logger.info(f"ext range: {range_x}, left: {range_left.round(3)}, right: {range_right.round(3)}")

        # project left and right from canvas units back into data units
        # and get the min max values to set as new domain min max.
        # e.g., prior domain was (0, 1) and now it may be (0.1, 0.9).
        domain_left = self.x_projection.inverse(range_left)
        domain_right = self.x_projection.inverse(range_right)
        xdomain_min, xdomain_max = toyplot.data.minimax(
            [xdomain_min, xdomain_max, domain_left, domain_right])
        logger.info(f"re domain = {xdomain_min}, {xdomain_max}")
        # min_range = min(range_left)
        # max_range = max(range_right)
        # logger.warning([min_range, max_range])
        # get min and max of range to fit extents
        # eidx = np.argmax(range_right)
        # right_most_extent_width = self._expand_domain_range_right[eidx]
        # eidx = np.argmin(range_left)
        # left_most_extent_width = self._expand_domain_range_left[eidx]
        # new_min_range = self._xmin_range - left_most_extent_width
        # new_max_range = self._xmax_range - right_most_extent_width

        # extents cannot push right beyond limits
        # print(new_min_range, new_max_range)
        # if new_min_range > new_max_range:
        #     mid = (new_min_range + new_max_range) / 2.
        #     new_min_range = mid - 1e-6
        #     new_max_range = mid + 1e-6

        # get projection function to translate current domain to expanded range
        # x_projection = _create_projection(
        #     self.x.scale,
        #     domain_min=xdomain_min,
        #     domain_max=xdomain_max,
        #     range_min=min_range,#20 + abs(left_most_extent_width), #new_min_range,
        #     range_max=max_range,##345.8 - 40,#new_max_range,
        # )

        # domain_left = x_projection.inverse(range_left)
        # domain_right = x_projection.inverse(range_right)
        # x0, x1 = x_projection.inverse([20, 460])
        # print('x0', x0, x1)
        # print("d", domain_left, domain_right)

        # # update domain
        # xdomain_min, xdomain_max = toyplot.data.minimax(
        #     [xdomain_min, xdomain_max, domain_left, domain_right])
        # print("xd", xdomain_min, xdomain_max)

        # ...
        self.y_projection = _create_projection(
            self.y.scale,
            domain_min=ydomain_min,
            domain_max=ydomain_max,
            range_min=self._ymin_range,
            range_max=self._ymax_range,
        )
        logger.info(f"orig domain = {ydomain_min}, {ydomain_max}")
        range_y = self.y_projection(self._expand_domain_range_y)
        range_top = range_y + self._expand_domain_range_top
        range_bottom = range_y + self._expand_domain_range_bottom
        domain_top = self.y_projection.inverse(range_top)
        domain_bottom = self.y_projection.inverse(range_bottom)
        ydomain_min, ydomain_max = toyplot.data.minimax(
            [ydomain_min, ydomain_max, domain_top, domain_bottom])
        logger.info(f"re domain = {ydomain_min}, {ydomain_max}")

        # optionally expand the domain to match x and y ranges
        if self._aspect == "fit-range":
            dwidth = xdomain_max - xdomain_min
            dheight = ydomain_max - ydomain_min
            daspect = dwidth / dheight
            raspect = (
                (self._xmax_range - self._xmin_range) /
                (self._ymax_range - self._ymin_range)
            )
            if daspect < raspect:
                offset = ((dwidth * (raspect / daspect)) - dwidth) * 0.5
                xdomain_min -= offset
                xdomain_max += offset
            elif daspect > raspect:
                offset = ((dheight * (daspect / raspect)) - dheight) * 0.5
                ydomain_min -= offset
                ydomain_max += offset

        # allow users to override the domain
        xdomain_min = self.x.domain.min if xdomain_min is None else xdomain_min
        xdomain_max = self.x.domain.max if xdomain_max is None else xdomain_max
        ydomain_min = self.y.domain.min if ydomain_min is None else ydomain_min
        ydomain_max = self.y.domain.max if ydomain_max is None else ydomain_max

        # ensure the domain is not empty after user could have modified
        if xdomain_min == xdomain_max:
            xdomain_min -= 0.5
            xdomain_max += 0.5
        if ydomain_min == ydomain_max:
            ydomain_min -= 0.5
            ydomain_max += 0.5

        # calculate x tick locations and labels
        xtick_locations = []
        xtick_labels = []
        xtick_titles = []
        if self.show and self.x.show:
            loc = self.x._locator()
            xtick_locations, xtick_labels, xtick_titles = (
                loc.ticks(xdomain_min, xdomain_max))

        # calculate y tick locations and labels
        ytick_locations = []
        ytick_labels = []
        ytick_titles = []
        if self.show and self.y.show:
            loc = self.y._locator()
            ytick_locations, ytick_labels, ytick_titles = (
                loc.ticks(ydomain_min, ydomain_max))

        # Allow tick locations to grow (never shrink) the domain.
        if len(xtick_locations):
            xdomain_min = np.amin((xdomain_min, xtick_locations[0]))
            xdomain_max = np.amax((xdomain_max, xtick_locations[-1]))
        if len(ytick_locations):
            ydomain_min = np.amin((ydomain_min, ytick_locations[0]))
            ydomain_max = np.amax((ydomain_max, ytick_locations[-1]))

        # Create projections for each axis.
        self._x_projection = _create_projection(
            scale=self.x.scale,
            domain_min=xdomain_min,
            domain_max=xdomain_max,
            range_min=self._xmin_range,
            range_max=self._xmax_range,
        )
        self._y_projection = _create_projection(
            scale=self.y.scale,
            domain_min=ydomain_min,
            domain_max=ydomain_max,
            range_min=self._ymax_range,
            range_max=self._ymin_range,
        )

        # Finalize positions for all axis components.
        if self.x.spine.position == "low":
            x_offset = self.padding
            x_spine_y = self._ymax_range
            x_ticks_near = 0
            x_ticks_far = 5
            x_tick_location = "below"
            x_label_location = "below"
        elif self.x.spine.position == "high":
            x_offset = -self.padding  # pylint: disable=invalid-unary-operand-type
            x_spine_y = self._ymin_range
            x_ticks_near = 5
            x_ticks_far = 0
            x_tick_location = "above"
            x_label_location = "above"
        else:
            x_offset = 0
            x_spine_y = self._y_projection(self.x.spine.position)
            x_ticks_near = 3
            x_ticks_far = 3
            x_tick_location = "below"
            x_label_location = "below"

        if self.y.spine._position == "low":
            y_offset = -self.padding  # pylint: disable=invalid-unary-operand-type
            y_spine_x = self._xmin_range
            y_ticks_near = 0
            y_ticks_far = 5
            y_tick_location = "above"
            y_label_location = "above"
        elif self.y.spine._position == "high":
            y_offset = self.padding
            y_spine_x = self._xmax_range
            y_ticks_near = 0
            y_ticks_far = 5
            y_tick_location = "below"
            y_label_location = "below"
        else:
            y_offset = 0
            y_spine_x = self._x_projection(self.y.spine._position)
            y_ticks_near = 3
            y_ticks_far = 3
            y_tick_location = "below"
            y_label_location = "below"

        # Finalize the axes.
        self.x._finalize(
            x1=self._xmin_range,
            x2=self._xmax_range,
            y1=x_spine_y,
            y2=x_spine_y,
            offset=x_offset,
            domain_min=xdomain_min,
            domain_max=xdomain_max,
            tick_locations=xtick_locations,
            tick_labels=xtick_labels,
            tick_titles=xtick_titles,
            default_tick_location=x_tick_location,
            default_ticks_far=x_ticks_far,
            default_ticks_near=x_ticks_near,
            default_label_location=x_label_location,
        )
        self.y._finalize(
            x1=y_spine_x,
            x2=y_spine_x,
            y1=self._ymax_range,
            y2=self._ymin_range,
            offset=y_offset,
            domain_min=ydomain_min,
            domain_max=ydomain_max,
            tick_locations=ytick_locations,
            tick_labels=ytick_labels,
            tick_titles=ytick_titles,
            default_tick_location=y_tick_location,
            default_ticks_far=y_ticks_far,
            default_ticks_near=y_ticks_near,
            default_label_location=y_label_location,
        )
        self._finalized = self
        return self._finalized


def _create_projection(scale, domain_min, domain_max, range_min, range_max):
    if isinstance(scale, toyplot.projection.Projection):
        return scale
    if scale == "linear":
        return toyplot.projection.linear(domain_min, domain_max, range_min, range_max)
    scale, base = scale
    return toyplot.projection.log(base, domain_min, domain_max, range_min, range_max)


def _mark_exportable(table, column, exportable=True):
    table.metadata(column)["toyplot:exportable"] = exportable



if __name__ == "__main__":

    import toyplot.browser
    import toyplot.dispatch
    canvas = toyplot.Canvas(width=500, height=500)

    dims = ["xmin_range", "xmax_range", "ymin_range", "ymax_range"]
    layout = toyplot.layout.region(0, canvas._width, 0, canvas._height)
    kwargs = dict(zip(dims, layout))
    axes = Cartesian(scenegraph=canvas._scenegraph, **kwargs)
    canvas._scenegraph.add_edge(canvas, "render", axes)

    # m0 = axes.text2(0, 0, "hello world")
    # m2 = axes.text2(0.5, 0.5, "hello world")
    # m2 = axes.text2(0.75, 0.75, "hello world")
    # m1 = axes.text2(1, 1, "hello world")

    # axes._finalize()
    # print(axes._expand_domain_range_right)
    # print(axes._expand_domain_range_y)
    # print()
    toyplot.browser.show(canvas)
