098-validate_binary_search_tree
###############################

:date: 2015-11-21 11:50
:tags: Recursion, Binary Search Trees
:category: LeetCode
:slug: 098-validate_binary_search_tree

`LeetCode Problem Link <https://leetcode.com/problems/validate-binary-search-tree/>`_

The check needs to be recursive. All nodes in ``cur``'s left subBST must be less than ``cur``.
All nodes in ``cur``'s right subBST must be greater than ``cur``. And this check must be done on all subBSTs
within the input BST.

.. code-block:: java

    public boolean isValidBST(TreeNode root) {

        if (root == null)
            return true;

        return isValidBST(root.left, null, root) &&
                isValidBST(root.right, root, null);
    }

    private boolean isValidBST(TreeNode cur, TreeNode min, TreeNode max) {

        if (cur==null)
            return true;

        if (min != null && cur.val <= min.val)
            return false;

        if (max != null && cur.val >= max.val)
            return false;

        // left subBST must be greater than min and smaller than cur
        // right subBST must be greater than cur and smaller than max
        return isValidBST(cur.left, min, cur) &&
                isValidBST(cur.right, cur, max);
    }
