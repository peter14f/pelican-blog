116-populating_next_right_pointers_in_each_node
###############################################

:date: 2015-11-29 16:09
:tags: Binary Trees
:category: LeetCode
:slug: 116-populating_next_right_pointers_in_each_node

`LeetCode Problem Link <https://leetcode.com/problems/distinct-subsequences/>`_

Very similar to 102-binary_tree_level_order_traversal.

.. code-block:: java

    public void connect(TreeLinkNode root) {

        List<TreeLinkNode> nodes = new ArrayList<TreeLinkNode>();

        int cnt = 0;
        if (root != null) {
            nodes.add(root);
            cnt = 1;
        }

        while (!nodes.isEmpty()) {
            TreeLinkNode prev = null;
            for (int i=0; i<cnt; i++) {
                TreeLinkNode node = nodes.remove(0);

                if (node.left != null)
                    nodes.add(node.left);

                if (node.right != null)
                    nodes.add(node.right);

                if (prev != null) {
                    prev.next = node;
                }

                prev = node;
            }

            cnt = nodes.size();
        }
    }
