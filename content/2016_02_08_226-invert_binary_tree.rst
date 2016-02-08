227-invert_binary_tree
######################

:date: 2016-2-8 18:38
:tags: Binary Trees, Recursion
:category: LeetCode
:slug: 227-invert_binary_tree

`LeetCode Problem Link <https://leetcode.com/problems/invert-binary-tree/>`_

Use recursion. The base case is the empty true where the tree root is simply returned.

.. code-block:: java

    public TreeNode invertTree(TreeNode root) {
        if (root == null)
            return null;

        invertTree(root.left);
        invertTree(root.right);

        TreeNode oldLeft = root.left;
        root.left = root.right;
        root.right = oldLeft;

        return root;
    }
