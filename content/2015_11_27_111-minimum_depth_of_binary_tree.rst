111-minimum_depth_of_binary_tree
################################

:date: 2015-11-27 18:04
:tags: Binary Trees, Tree Node Depth
:category: LeetCode
:slug: 111-minimum_depth_of_binary_tree

`LeetCode Problem Link <https://leetcode.com/problems/minimum-depth-of-binary-tree/>`_

Use recursion. A leaf node (node whose left child and right child are both null) has a depth of 1.

If a node only has a left child, then going to its right child would not lead to a leaf node.
If a node only has a right child, then going to its left child would not lead to a leaf node.

.. code-block:: java

    public int minDepth(TreeNode root) {
        if (root==null)
            return 0;

        if (root.left == null && root.right == null) {
            // I'm a leaf node
            return 1;
        }

        int leftChildDepth = Integer.MAX_VALUE;
        int rightChildDepth = Integer.MAX_VALUE;

        if (root.left != null) {
            leftChildDepth = minDepth(root.left);
        }

        if (root.right != null) {
            rightChildDepth = minDepth(root.right);
        }

        if (leftChildDepth <= rightChildDepth)
            return leftChildDepth + 1;
        else
            return rightChildDepth + 1;
    }

