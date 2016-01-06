156-binary_tree_upside_down
###########################

:date: 2016-1-5 19:10
:tags: Binary Trees, Recursion
:category: LeetCode
:slug: 156-binary_tree_upside_down

`LeetCode Problem Link <https://leetcode.com/problems/binary-tree-upside-down/>`_

Properly null-terminate the left and right child is very important, just like when we are
reversing a linked list.

.. code-block:: java

  public TreeNode upsideDownBinaryTree(TreeNode root) {
        if (root == null)
            return null;

        if (root.left == null && root.right == null)
            return root;

        TreeNode origLeft = root.left;
        TreeNode treeRoot = upsideDownBinaryTree(origLeft);
        origLeft.right = root;
        origLeft.left = root.right;
        root.left = null;
        root.right = null;

        return treeRoot;
    }

Since we are using recursion, the space complexity is again the O(h) where ``h`` is the height of the binary tree.

