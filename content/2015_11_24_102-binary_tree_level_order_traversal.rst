102-binary_tree_level_order_traversal
#####################################

:date: 2015-11-24 22:11
:tags: Binary Trees, Level Order Traversal
:category: LeetCode
:slug: 102-binary_tree_level_order_traversal

`LeetCode Problem Link <https://leetcode.com/problems/binary-tree-level-order-traversal/>`_

.. code-block:: java

    public List<List<Integer>> levelOrder(TreeNode root) {

        List<List<Integer>> levels = new ArrayList<List<Integer>>();

        List<Integer> curLevel = new ArrayList<Integer>();
        List<TreeNode> nodes = new ArrayList<TreeNode>();

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
                levels.add(new ArrayList<Integer>(curLevel));
                curLevel.clear();
            }

            cnt = nodes.size();
        }

        return levels;
    }