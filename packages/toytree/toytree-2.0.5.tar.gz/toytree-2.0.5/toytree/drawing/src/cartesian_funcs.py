#!/usr/bin/env python

"""...

"""


from typing import Sequence, Mapping, Any, TypeVar
from toyplot.mark import Mark
import toyplot
from toytree.drawing.src.cartesian import Cart
from toytree.drawing.src.cartesian_api import add_cartesian_method

Color = TypeVar("Color")
__all__ = [
    "text",
]


def _mark_exportable(table, column, exportable=True):
    table.metadata(column)["toyplot:exportable"] = exportable


@add_cartesian_method(Cart)
def text(
    axes: Cart,
    a: Sequence[float],
    b: Sequence[float],
    text: Sequence[str],
    angle: float = 0,
    color: Color = None,
    opacity: float = 1.0,
    title: str = None,
    style: Mapping[str, Any] = None,
    filename: str = None,
    annotation: bool = True,
) -> Mark:
    """Add text to the axes.

    Parameters
    ----------
    a, b: float
      Coordinates of the text anchor.
    text: string
      The text to be displayed.
    title: string, optional
      Human-readable title for the mark.  The SVG / HTML backends render the
      title as a tooltip.
    style: dict, optional
      Collection of CSS styles to apply to the mark.  See
      :class:`toyplot.mark.Text` for a list of useful styles.
    annotation: boolean, optional
      Set to True if this mark should be considered an annotation.

    Returns
    -------
    text: :class:`toyplot.mark.Text`
    """
    table = toyplot.data.Table()
    table["x"] = toyplot.require.scalar_vector(a)
    table["y"] = toyplot.require.scalar_vector(b, table.shape[0])
    table["text"] = toyplot.broadcast.pyobject(text, table.shape[0])
    _mark_exportable(table, "x")
    _mark_exportable(table, "y")
    _mark_exportable(table, "text")

    table["angle"] = toyplot.broadcast.scalar(angle, table.shape[0])
    table["opacity"] = toyplot.broadcast.scalar(opacity, table.shape[0])
    table["title"] = toyplot.broadcast.pyobject(title, table.shape[0])
    style = toyplot.style.require(style, allowed=toyplot.style.allowed.text)

    default_color = [next(axes._text_colors)]

    color = toyplot.color.broadcast(
        colors=color,
        shape=(table.shape[0], 1),
        default=default_color,
    )
    table["fill"] = color[:, 0]

    mark = toyplot.mark.Text(
        coordinate_axes=["x", "y"],
        table=table,
        coordinates=["x", "y"],
        text=["text"],
        angle=["angle"],
        fill=["fill"],
        opacity=["opacity"],
        title=["title"],
        style=style,
        annotation=annotation,
        filename=filename,
    )
    return axes.add_mark(mark)


if __name__ == "__main__":

    import toytree

    canvas = toyplot.Canvas()
    axes = Cart(scenegraph=canvas._scenegraph)
    canvas._scenegraph.add_edge(canvas, "render", axes)
    m0 = axes.text(0, 0, "hello world")
    m1 = axes.text(1, 1, "hello world")

    toytree.utils.show(canvas)
