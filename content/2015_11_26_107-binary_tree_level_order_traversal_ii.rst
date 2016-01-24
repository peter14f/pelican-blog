107-binary_tree_level_order_traversal_ii
########################################

:date: 2015-11-26 13:11
:tags: Binary Trees, Level Order Traversal
:category: LeetCode
:slug: 107-binary_tree_level_order_traversal_ii

`LeetCode Problem Link <https://leetcode.com/problems/binary-tree-level-order-traversal-ii/>`_

It's basically the same as 102-binary_tree_level_order_traversal besides the order in the returned list.

.. code-block:: java

    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> levels = new ArrayList<List<Integer>>();

        List<TreeNode> nodes = new ArrayList<TreeNode>();
        List<Integer> curLevel = new ArrayList<Integer>();

        int cnt = 0;
        if (root != null) {
            nodes.add(root);
            cnt = 1;
        }

        while (!nodes.isEmpty()) {
            for (int i=0; i<cnt; i++) {
                TreeNode node = nodes.remove(0);
                curLevel.add(node.val);

                if (node.left != null)
                    nodes.add(node.left);

                if (node.right != null)
                    nodes.add(node.right);
            }

            if (!curLevel.isEmpty()) {
                levels.add(0, new ArrayList<Integer>(curLevel));
                curLevel.clear();
            }

            cnt = nodes.size();
        }

        return levels;
    }
