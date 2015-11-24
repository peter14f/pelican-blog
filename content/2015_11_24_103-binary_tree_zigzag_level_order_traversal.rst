103-binary_tree_zigzag_level_order_traversal
############################################

:date: 2015-11-24 23:18
:tags: Binary Trees
:category: LeetCode
:slug: 103-binary_tree_zigzag_level_order_traversal

`LeetCode Problem Link <https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/>`_

This is very similar to the previous problem 102-binary_tree_level_order_traversal. We just need to
alternate the direction in which we go through the nodes in the current level each time we finish
with the current level.

.. code-block:: java

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {

        List<List<Integer>> levels = new ArrayList<List<Integer>>();

        List<TreeNode> nodes = new ArrayList<TreeNode>();
        List<Integer> curLevel = new ArrayList<Integer>();

        int cnt = 0;
        boolean back = false;

        if (root != null) {
            nodes.add(root);
            cnt = 1;
        }

        while (!nodes.isEmpty()) {

            for (int i=0; i<cnt; i++) {
                TreeNode node = nodes.get(i);

                if (!back) {
                    curLevel.add(node.val);
                }
                else {
                    TreeNode tail = nodes.get(cnt-1-i);
                    curLevel.add(tail.val);
                }

                if (node.left != null)
                    nodes.add(node.left);
                if (node.right != null)
                    nodes.add(node.right);
            }

            for (int i=0; i<cnt; i++)
                nodes.remove(0);

            if (!curLevel.isEmpty()) {
                levels.add(new ArrayList<Integer>(curLevel));
                curLevel.clear();
            }

            cnt = nodes.size();
            back = !back;

        }

        return levels;
    }