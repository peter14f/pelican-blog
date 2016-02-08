222-count_complete_tree_nodes
#############################

:date: 2016-2-4 22:24
:tags: Complete Binary Trees
:category: LeetCode
:slug: 222-count_complete_tree_nodes

`LeetCode Problem Link <https://leetcode.com/problems/count-complete-tree-nodes/>`_

How would I count the number of nodes for any binary tree?

.. code-block:: java

    public int countNodes(TreeNode root) {
        if (root==null)
            return 0;

        int[] sum = {0};

        countNodes(sum, root);

        return sum[0];
    }

    private void countNodes(int[] sum, TreeNode node) {
        if (node == null)
            return;

        countNodes(sum, node.left);
        sum[0]++;
        countNodes(sum, node.right);
    }

This solution will get TLE on OJ. So we must use some properties of a complete binary tree.

Notice that if you pick any node in the complete binary tree as the root of the subtree, that subtree is itself
a complete binary tree. So we can use recursion to count. The time complexity is O(h\ :superscript:`2`).

.. code-block:: java

    public int countNodes(TreeNode root) {
        if (root==null)
            return 0;

        int leftSubtreeH = treeHeight(root.left, true) + 1;
        int rightSubtreeH = treeHeight(root.right, false) + 1;

        if (leftSubtreeH == rightSubtreeH) {
            return (1 << leftSubtreeH) -1;
        }
        else {
            return countNodes(root.left) + countNodes(root.right) + 1;
        }
    }

    private int treeHeight(TreeNode node, boolean left) {
        if (node == null)
            return 0;

        int h = 0;
        while (node != null) {
            h++;
            if (left)
                node = node.left;
            else
                node = node.right;
        }

        return h;
    }
