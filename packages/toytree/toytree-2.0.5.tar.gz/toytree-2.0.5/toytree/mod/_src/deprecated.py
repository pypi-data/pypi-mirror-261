



def move_nni_unrooted():
    raise NotImplementedError("TODO")

def iter_spr_rooted(tree: ToyTree):
    """Return a generator that will visit all trees within one SPR
    move of the current tree.

    The returned set of trees does not visit the original tree.

    NOT YET WORKING/TESTED (you can help!)

    Examples
    --------
    >>> tree = toytree.rtree.unittree(ntips=10, seed=123)
    >>> spr_trees = iter_spr_unrooted(tree)
    >>> logliks = [func(stre) for stre in spr_trees]
    """
    # just iter over each possible subtree and each possible placement,
    # right? But some are redundant? Try it out...
    # raise NotImplementedError("TODO")
    raise NotImplementedError("TODO")
    edges = tree.get_edges()
    nedges = edges[edges[:, 0] != tree.treenode.idx]

    # iterate over rows of edge matrix
    for eidx in range(nedges.shape[0]):
        nnidx = nedges[eidx, 1]
        tips = tree.get_tip_labels(nnidx)
        print(nnidx, tips)

        # iterate over possible edges to place this subtree (not orig edge)
        _sub1 = tree.drop_tips(tips)
        for nidx in range(1, _sub1.nnodes):
            if nidx in [tree.treenode.idx, nnidx]:
                continue

            # toytrees
            sub0 = tree.prune(tips)
            sub1 = tree.drop_tips(tips)
            node = sub1[nidx]

            new = toytree.Node(name="spr", dist=node.dist / 2)
            node.up.children.append(new)
            node.up.children.remove(node)
            node.up = new
            new.children.append(node)
            new.children.append(sub0.treenode)
            sub0.up = new
            yield toytree.ToyTree(sub1.treenode)


def move_spr_unrooted(tree: ToyTree, seed:Optional[int]=None):
    """Return an unrooted ToyTree after one SPR move to input tree.

    Select one edge randomly from the tree and split on that edge to
    create two subtrees. Attach one of the subtrees (e.g., the
    smaller one) randomly to the larger tree to create a new node.
    """
    # ensure tree is unrooted
    if tree.is_rooted():
        tree = tree.unroot()

    # seed generator
    rng = np.random.default_rng(seed)

    # select a random edge
    nidx = rng.integers(tree.nnodes - 1)

    # get subtree below this edge
    sub0 = tree.prune(tree.get_tip_labels(nidx))

    # get subtree with sub0 removed
    sub1 = tree.drop_tips(tree.get_tip_labels(nidx))

    # randomly select an edge on sub1 to add sub0 back to
    nidx = rng.choice(range(1, sub1.nnodes))
    node = sub1[nidx]

    # randomly select a point on the branch to add new node
    if len(sub0) == 1:
        sub0 = sub0.treenode.children[0]
    else:
        sub0 = sub0.treenode
        # node.up.children.append(sub0)

    new = toytree.Node(name="spr", dist=rng.uniform(node.dist))
    node.up.children.append(new)
    node.up.children.remove(node)
    node.up = new
    new.children.append(node)
    new.children.append(sub0)
    sub0.up = new

    tree = toytree.ToyTree(sub1.treenode)
    return tree


def move_spr_rooted(
    tree: ToyTree,
    seed: Optional[int]=None,
    inplace: bool=False,
) -> ToyTree:
    """Return a rooted ToyTree one SPR move from the current tree.

    Performs a subtree pruning and regrafting move on the input tree.
    Selects one edge randomly from the tree and splits on that edge
    to create two subtrees, then attaches one of the subtrees (the
    smaller one) randomly to the larger tree to create a new node.

    This implementation is super slow, should not use prune and
    drop_tips since these require an update call.
    """
    # seed generator
    rng = np.random.default_rng(seed)

    # randomly select one edge that is not leading to the root
    edges = tree.get_edges()
    nedges = edges[edges[:, 0] != tree.treenode.idx]
    nidx = nedges[rng.integers(nedges.shape[0]), 0]
    tips = tree.get_tip_labels(nidx)

    # get subtree below selected edge
    # TODO: much faster methods would avoid prune and drop calls.
    sub0 = tree.prune(tips)

    # get subtree with sub0 clade removed
    sub1 = tree.drop_tips(tips)

    # randomly select an edge on sub1 to add sub0 back to
    # TODO, what is this selecting? why 1:?
    nidx = rng.choice(sub1.get_nodes()[1:])
    node = sub1[nidx]

    # randomly select a point on the branch to add new node
    new = toytree.Node(name="spr", dist=rng.uniform(node.dist))
    node.up.children.append(new)
    node.up.children.remove(node)
    node.up = new
    new.children.append(node)
    new.children.append(sub0.treenode)
    sub0.up = new

    tree = toytree.ToyTree(sub1.treenode)
    return tree


def _move_spr_rooted_fast(tree:toytree.ToyTree, seed:Optional[int]=None):
    """Faster implementation that avoids ToyTree coords updates.

    Returns an rooted ToyTree where one subtree pruning and
    regrafting move has been performed from the input tree.

    Select one edge randomly from the tree and split on that edge to
    create two subtrees. Attach one of the subtrees (e.g., the
    smaller one) randomly to the larger tree to create a new node.
    """
    # seed generator
    rng = np.random.default_rng(seed)

    # randomly select one edge that is not leading to the root
    edges = tree.get_edges()
    nedges = edges[edges[:, 0] != tree.treenode.idx]
    nidx = nedges[rng.integers(nedges.shape[0]), 0]
    tips = tree.get_tip_labels(nidx)

    # get subtree below selected edge
    tree1 = tree.treenode._clone()
    tree1.prune(tips)

    # get subtree with sub0 clade removed
    tree2 = tree.treenode._clone()
    tree2.prune([i for i in tree.get_tip_labels() if i not in tips])

    # randomly select a non-root node on sub1
    node = rng.choice(list(tree2.iter_descendants()))

    # randomly select a point on the branch to add new node
    new = toytree.Node(name="spr", dist=rng.uniform(node.dist))
    node.up.children.append(new)
    node.up.children.remove(node)
    node.up = new
    new.children.append(node)
    new.children.append(tree1)
    tree1.up = new

    tree = toytree.core.tree.ToyTree(tree2)
    return tree

