110-balanced_binary_tree
########################

:date: 2015-11-26 22:54
:tags: Binary Trees, Tree Height, Recursion
:category: LeetCode
:slug: 110-balanced_binary_tree

`LeetCode Problem Link <https://leetcode.com/problems/balanced-binary-tree/>`_

An empty tree is balanced. This check needs to be recursive. We only return true if all subtrees in the binary tree
are balanced (not just the root).

.. code-block:: java

    public boolean isBalanced(TreeNode root) {

        if (root == null)
            return true;

        int leftSubtreeHeight = getHeight(root.left);
        int rightSubtreeHeight = getHeight(root.right);

        if (Math.abs(leftSubtreeHeight-rightSubtreeHeight) > 1)
            return false;

        return isBalanced(root.left) && isBalanced(root.right);
    }

    private int getHeight(TreeNode node) {
        if (node == null)
            return 0;

        int left = getHeight(node.left);
        int right = getHeight(node.right);

        if (left >= right)
            return 1 + left;
        else
            return 1 + right;
    }