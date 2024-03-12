#!/usr/bin/env python


import toytree


def logo():
    tree = toytree.rtree.unittree(5, seed=300)
    c, a, m = tree.draw(
        width=150, height=180,
        layout='d',
        edge_type='c', edge_widths=3, tip_labels=False,
    )
    toytree.annotate.add_tip_markers(tree, a, size=[4, 5, 6, 5, 4], style={"stroke": None}, yshift=8, color=toytree.color.COLORS1[0])
    toytree.annotate.add_tip_markers(tree, a, size=[6, 5, 4, 3, 4], style={"stroke": None}, yshift=16, color=toytree.color.COLORS1[1])
    toytree.annotate.add_tip_markers(tree, a, size=[4, 3, 4, 5, 6], style={"stroke": None}, yshift=24, color=toytree.color.COLORS1[2])
    toytree.annotate.add_tip_markers(tree, a, size=[5, 6, 7, 6, 5], style={"stroke": None}, yshift=32, color=toytree.color.COLORS1[3])
    toytree.annotate.add_tip_markers(tree, a, size=[6, 5, 4, 5, 6], style={"stroke": None}, yshift=40, color=toytree.color.COLORS1[4])
    return c, a, m


if __name__ == "__main__":
    logo()
