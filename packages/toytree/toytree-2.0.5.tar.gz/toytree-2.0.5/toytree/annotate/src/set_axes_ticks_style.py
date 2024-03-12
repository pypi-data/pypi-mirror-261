# #!/usr/bin/env python

# """DEPRECATED FOR add_scale_bar and ...

# """

# import numpy as np
# import toyplot
# from toytree import ToyTree
# from toytree.core import Cartesian
# from toytree.core.apis import add_subpackage_method, AnnotationAPI
# from toytree.annotate.src.annotation_mark import (
#     get_last_toytree_mark_from_cartesian,
#     assert_tree_matches_mark,
# )


# def set_axes_ticks_style(
#     tree: ToyTree,
#     axes: Cartesian,
#     only_inside: bool = True,
#     **kwargs,
# ) -> Cartesian:
#     """Return a Cartesian axes modified for custom tick marks.

#     This gets tick locations first using toyplot.locator.Extended and
#     then sets labels on them using toyplot.locator.Explicit, because
#     we need time scale bar to be non-negative when axes are rotated
#     for trees facing different directions.

#     Note
#     -----
#     Some work is done internally to try to nicely handle floating point
#     precision.

#     Parameters
#     ----------
#     ...
#     style: TreeStyle
#         A TreeStyle object with options for styling axes.
#     only_inside: bool
#         Option used by toyplot.locator.Extended to automatically find
#         tick marks given the data range.
#     """
#     mark = get_last_toytree_mark_from_cartesian(axes)
#     assert_tree_matches_mark(tree, mark)

#     # the axes is either new or passed as an arg, and the scale_bar
#     # arg is True or a (float, int), so we need to style the ticks.
#     if mark.layout in ("r", "l"):
#         nticks = max((4, np.floor(mark.width / 75).astype(int)))
#         axes.y.show = False
#         axes.x.show = True
#         axes.x.ticks.show = True
#     elif mark.layout in ("u", "d"):
#         nticks = max((4, np.floor(mark.height / 75).astype(int)))
#         axes.x.show = False
#         axes.y.show = True
#         axes.y.ticks.show = True
#     # e.g., unrooted layout with axes shown (e.g., ts='p')
#     else:
#         # nticks = max((4, np.floor(style.height / 75).astype(int)))
#         nticks = 5
#         axes.x.show = False
#         axes.y.show = False

#     # get tick locator
#     lct = toyplot.locator.Extended(count=nticks, only_inside=only_inside)

#     # get root tree height
#     if mark.layout in ("r", "u"):
#         locs = lct.ticks(-tree_height, -0)[0]
#     else:
#         locs = lct.ticks(0, tree_height)[0]

#     # apply unit scaling
#     if mark.scale_bar is False:
#         labels = abs(locs.copy())
#     elif isinstance(mark.scale_bar, (int, float)):
#         labels = abs(locs / mark.scale_bar)
#     else:
#         labels = abs(locs.copy())
#     labels = [np.format_float_positional(i, precision=6, trim="-") for i in labels]

#     # set the ticks locator
#     if mark.layout in ("r", "l"):
#         axes.x.ticks.locator = toyplot.locator.Explicit(
#             locations=locs + mark.xbaseline,
#             labels=labels,
#         )
#     elif mark.layout in ("u", "d"):
#         axes.y.ticks.locator = toyplot.locator.Explicit(
#             locations=locs + mark.ybaseline,
#             labels=labels,
#         )
#     # print(locs, labels)
#     return axes
