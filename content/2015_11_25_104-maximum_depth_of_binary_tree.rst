104-maximum_depth_of_binary_tree
################################

:date: 2015-11-25 12:54
:tags: Binary Trees, Tree Height, Recursion
:category: LeetCode
:slug: 104-maximum_depth_of_binary_tree

`LeetCode Problem Link <https://leetcode.com/problems/maximum-depth-of-binary-tree/>`_

Pretty straightforward. The height of an empty tree is ``0``. The height of a tree with only one node is ``1``.

.. code-block:: java

    public int maxDepth(TreeNode root) {
        if (root == null)
            return 0;

        int leftChildHeight = maxDepth(root.left);
        int rightChildHeight = maxDepth(root.right);

        if (leftChildHeight >= rightChildHeight)
            return 1 + leftChildHeight;
        else
            return 1 + rightChildHeight;
    }