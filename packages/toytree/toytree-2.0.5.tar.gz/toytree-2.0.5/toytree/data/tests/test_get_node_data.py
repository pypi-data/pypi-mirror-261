#!/usr/bin/env python

"""Test get_node_data 

- normal use
- missing data
- complex dtypes
- complex mixed dtypes
"""

import unittest
import numpy as np
import toytree


class TestNodeData(unittest.TestCase):

    def setUp(self):
        self.tree = toytree.rtree.unittree(6)

    def test_int_data(self):
        self.tree.set_node_data("x", range(self.tree.nnodes), inplace=True)
        self.assertListEqual(
            list(self.tree.get_node_data('x').values),
            list(range(self.tree.nnodes))
        )

    def test_int_data_w_missing(self):
        """This will convert the ints to floats in get_node_data."""
        self.tree.set_node_data("x", {5: 5, 6: 6}, inplace=True)
        self.assertListEqual(
            list(self.tree.get_node_data('x').values),
            [np.nan, np.nan, np.nan, np.nan, np.nan, 5, 6, np.nan, np.nan, np.nan, np.nan]
        )


    def test_get_node_data(self):
        pass


if __name__ == "__main__":
    unittest.main()
