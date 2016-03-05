314-binary_tree_vertical_order_traversal
########################################

:date: 2016-2-26 9:15
:tags: Binary Trees, Binary Tree Traversal
:category: LeetCode
:slug: 314-binary_tree_vertical_order_traversal

`LeetCode Problem Link <https://leetcode.com/problems/binary-tree-vertical-order-traversal/>`_

If we think of the root as in a horizontal position of ``0``. It's left child would be in position ``-1``, and
it's right child would be in position ``1``. We could get the position of children given the position of the
current node.

Using recursion, I can store the current node into the list that matches its position.
We can use a ``HashMap<Integer, List<TreeNode>>`` to store all the lists. The key is simply the position.

First Attempt

.. code-block:: java

    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> allLists = new ArrayList<List<Integer>>();

        if (root==null)
            return allLists;

        HashMap<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>();

        addNodeToItsList(root, 0, map);

        List<Integer> positions = new ArrayList<Integer>(map.keySet());

        Collections.sort(positions);

        // traverse the position in order
        for (int pos: positions) {
            allLists.add(map.get(pos));
        }

        return allLists;
    }

    private void addNodeToItsList(TreeNode node, int position, HashMap<Integer, List<Integer>> map) {

        if (node==null)
            return;

        if (!map.containsKey(position)) {
            map.put(position, new ArrayList<Integer>());
        }

        map.get(position).add(node.val);

        // got to go to left first according to the problem statement:
        //   If two nodes are in the same row and column,
        //   the order should be from left to right.

        addNodeToItsList(node.left, position-1, map);
        addNodeToItsList(node.right, position+1, map);
    }

::

    Input:
    [5,1,6,null,3,null,null,2,4]
    Output:
    [[1,2],[5,3],[4,6]]
    Expected:
    [[1,2],[5,3],[6,4]]

So it looks like nodes in the same column but different rows must be in the order of the rows.
Does that mean we should pass down the vertical position from root as well?

Wait a minute, perhaps we should we BFS instead DFS.
That way, we are guaranteed that the upper nodes are added into the list first.


.. code-block:: java

    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> allLists = new ArrayList<List<Integer>>();

        if (root==null)
            return allLists;

        HashMap<TreeNode, Integer> posLookup = new HashMap<TreeNode, Integer>();
        HashMap<Integer, List<Integer>> listLookup = new HashMap<Integer, List<Integer>>();

        posLookup.put(root, 0);

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);

        // with a binary tree we don't need to worry about coming back
        // to current node because the child does not have a parent pointer

        while (!q.isEmpty()) {
            TreeNode node = q.poll();

            int position = posLookup.get(node);

            if (!listLookup.containsKey(position)) {
                List<Integer> newList = new ArrayList<Integer>();
                listLookup.put(position, newList);
            }

            listLookup.get(position).add(node.val);

            if (node.left != null) {
                posLookup.put(node.left, position-1);
                q.offer(node.left);
            }

            if (node.right != null) {
                posLookup.put(node.right, position+1);
                q.offer(node.right);
            }
        }

        List<Integer> positions = new ArrayList<Integer>(listLookup.keySet());
        Collections.sort(positions);

        for (int pos: positions) {
            allLists.add(listLookup.get(pos));
        }

        return allLists;
    }

One the the observation I made when doing BFS on a graph is that we've got to make sure that we don't
end up going back to a node that we've been to. With BFS on a binary tree, we don't actually need to worry
about this because the nodes in a binary tree do not have a reference to the parent node.

