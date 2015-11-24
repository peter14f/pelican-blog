101-symmetric_tree
##################

:date: 2015-11-24 19:54
:tags: Binary Trees, Recursion
:category: LeetCode
:slug: 101-symmetric_tree

`LeetCode Problem Link <https://leetcode.com/problems/symmetric-tree/>`_

The method ``isSymmetric()`` takes two arguments, the ``left`` child and the ``right`` child from the parent.
We must recursively check that the outer nodes (left child of ``left`` and right child of ``right``) and the
innter nodes (right child of ``left`` and left child of ``child``) contain the same values.

.. code-block:: java

    public boolean isSymmetric(TreeNode root) {
        if (root==null)
            return true;

        return isSymmetric(root.left, root.right);
    }

    private boolean isSymmetric(TreeNode left, TreeNode right) {

        if (left==null)
            return right==null;

        if (right==null)
            return left==null;

        if (left.val != right.val)
            return false;

        boolean out = isSymmetric(left.left, right.right);

        if (!out)
            return false;

        return isSymmetric(left.right, right.left);
    }
