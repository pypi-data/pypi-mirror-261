#!/usr/bin/env python

"""Neighbor-joining distance based tree inference method.

Algorithm is available in both a performant version (...) as well 
as a didactic version (...).

TODO
----
Implement BioNJ algorithm.
 Gascuel, O (1997) "BIONJ: an improved version of the NJ 
 algorithm based on a simple model of sequence data."

References
----------
...
"""

from typing import TypeVar
from numpy.typing import ArrayLike
import numpy as np
from numba import njit


ToyTree = TypeVar("ToyTree")


def infer_neigbor_joining_tree(matrix: ArrayLike) -> ToyTree:
    """Return a ToyTree inferred by NeighborJoining on a distance matrix.

    Parameters
    ----------
    matrix: ArrayLike
        A symmetric matrix (e.g., ndarray or dataframe) with float or
        int values representing distances between samples. If dataframe
        the returned tree will use the index labels as tip names, else
        the tip labels will be the numeric row indices.

    Examples
    --------
    ...

    References
    ----------
    ...
    """
    # store current nodes indices: [0, 1, 2, 3, ...]. This will 
    # initially contain only tips, but later internal node idxs also.
    idxs = np.arange(matrix.shape[0])
    
    # create a copy of original matrix as float type
    arr = np.array(matrix).astype(np.float64)
    
    # iteratively reduce matrix dims by joining nodes until shape=3
    nodes = []
    while mat.shape[0] > 3:
        
        # cluster nodes with shortest distance, returns node indices,
        # distances, and new matrix with its node indices.
        fidx, gidx, dist_fu, dist_gu, mat, idxs = nj_reduce_matrix_jit(mat, idxs)

        # store info about Nodes that were clustered.
        nodes.append([fidx, gidx, dist_fu, dist_gu, max(idxs)])
    
    # final dist: get dist from internal to newnode
    v0 = (1 / 2.) * mat[0, -1]   
    v1 = (1 / (2 * (3 - 2))) * (mat[-1, :].sum() - mat[0, :].sum())
    dist_vw = v0 + v1
    dist_dw = mat[0, -1] - dist_vw
    dist_ew = mat[1, -1] - dist_vw
    nodes.append([idxs[0], idxs[1], dist_dw, dist_ew, dist_vw])
    
    # build tree from nodes info
    tree = build_tree(nodes)

    # relabel tips with dataframe indices if input was a dataframe
    if isinstance(matrix, pd.DataFrame):
        tree = tree.set_node_data(
            feature="name", 
            mapping=dict(enumerate(matrix.index)),
        )
    return tree


@njit
def get_new_matrix_jit(
    mat: ArrayLike, mask: ArrayLike, f: float, g: float) -> ArrayLike:
    """Return matrix w/ distance of all nodes to the new node. 

    The returned matrix has dimension - 1 relative to original.
    """
    # get new matrix with dim-1 to fill
    ntips = mat.shape[0] - 1
    newmat = np.zeros((ntips, ntips))
    
    # fill newmat with dist between remaining tips
    newmat[:ntips - 1, :ntips - 1] = mat[mask, :][:, mask]  
    
    # fill final row/col with dists to newnode
    val = (1 / 2.) * (mat[f][mask] + mat[g][mask] - mat[f, g])
    newmat[-1, :-1] = val
    newmat[:-1, -1] = val 
    return newmat
        
@njit
def get_q_matrix_jit(mat: ArrayLike) -> ArrayLike:
    """Return q-matrix w/ distance of each tip to all other nodes.

    $$
    Q(i,j) = (n-2)d(i,j) - Sum(d(i,k) - Sum(d(j,k)
    $$
    """
    # create an empty matrix of same size
    qmat = np.zeros(mat.shape)
    nrows = mat.shape[0]

    # iterate over all cells in the lower-left triangle
    for i in range(nrows):
        for j in range(i + 1, nrows):
            if i != j:
                # fill values 
                val0 = (nrows - 2) * mat[i, j]
                val1 = mat[i, :].sum() 
                val2 = mat[j, :].sum()
                val = val0 - val1 - val2
                qmat[i, j] = val
                qmat[j, i] = val
    return qmat

@njit
def get_new_dist_jit(mat: ArrayLike, f: float, g: float) -> float:
    """Return distance from tips (f, g) to new node."""
    n = mat.shape[0]
    v0 = (1 / 2.) * mat[f, g]
    v1 = 1 / (2. * (n - 2))
    v2 = mat[f, :].sum()
    v3 = mat[g, :].sum()
    val = v0 + v1 * (v2 - v3)
    return val

@njit
def nj_reduce_matrix_jit(mat: ArrayLike, idxs: ArrayLike) -> ArrayLike:
    """Returns one agglomeration of the shortest distance in matrix.
    """
    # the q-matrix compares all-by-all
    qmat = get_q_matrix_jit(mat)

    # join the nodes with lowest q-score to create new node u
    min_idxs = np.where(qmat == qmat.min())
    f = min_idxs[0][0]
    g = min_idxs[1][0]

    # get distance of new node from children
    dist_fu = get_new_dist_jit(mat, f, g)
    dist_gu = mat[f, g] - dist_fu

    # get mask to hide rows and columns of agglomerated indices
    mask0 = np.arange(mat.shape[0]) != f
    mask1 = np.arange(mat.shape[0]) != g
    mask = mask0 & mask1

    # create new matrix removing (f, g) and adding (u)
    mat = get_new_matrix_jit(mat, mask, f, g)

    # get index labels
    fidx = idxs[f]
    gidx = idxs[g]

    # reset labels
    nidxs = np.zeros(mat.shape[0], dtype=np.int64)
    nidxs[:-1] = idxs[mask]
    nidxs[-1] = max(idxs) + 1
    idxs = nidxs

    # return f, g, u, fdist, gdist, nidx
    return fidx, gidx, dist_fu, dist_gu, mat, idxs

def build_tree_from_xxx(nodes):
    """Return a ToyTree constructed from ...

    Build a newick string and parse into a tree. Nodes are nested
    in order in the nodes list. Each element contains:
    [node_index0, node_index1, dist0, dist1, parent_index]
    except the final element in which the last element is the 
    internal edge length.
    """
    # store internal node indices to newick strings
    relate = {}
    
    # iterate over internal nodes in order
    for n in nodes[:-1]:
        
        # expand internal nodes to newick strings
        if n[0] in relate:
            n[0] = relate[n[0]]
        if n[1] in relate:
            n[1] = relate[n[1]]
            
        # make newick of the new node pair
        newick = "({}:{},{}:{})".format(n[0], n[2], n[1], n[3])
        
        # store internal node 
        relate[n[4]] = newick
    
    # create final unrooted polytomy
    n0, n1, dist0, dist1, iedge = nodes[-1]    
    newick = "({}:{}, {}:{}, {}:{});".format(newick, iedge, n0, dist0, n1, dist1)
    return toytree.tree(newick)



if __name__ == "__main__":

    import pandas as pd
    import toyplot.browser

    MAT = pd.DataFrame(
        columns=list("abcde"),
        index=list("abcde"),
        data=[
            [0, 5, 9, 9, 8],
            [5, 0, 10, 10, 9],
            [9, 10, 0, 8, 7],
            [9, 10, 8, 0, 3],
            [8, 9, 7, 3, 0],
        ],
    )

    # piecewise example
    IDXS = np.arange(MAT.shape[0])
    ARR = np.array(MAT).astype(np.float64)

    print(IDXS)
    print(ARR)

    fidx, gidx, dist_fu, dist_gu, mat, idxs = nj_reduce_matrix_jit(ARR, IDXS)
    print(fidx, gidx, dist_fu, dist_gu, mat, idxs)

    # full example
    # TREE = infer_neigbor_joining_tree(MAT)
    # TREE._draw_browser()

