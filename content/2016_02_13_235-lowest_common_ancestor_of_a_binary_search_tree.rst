235-lowest_common_ancestor_of_a_binary_search_tree
##################################################

:date: 2016-2-13 23:28
:tags: Binary Search Trees, Common Ancestor
:category: LeetCode
:slug: 235-lowest_common_ancestor_of_a_binary_search_tree

`LeetCode Problem Link <https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/>`_

This problem would be a lot more difficult if we need to check if ``p`` and ``q`` are actually in the BST.

But the problem statement states that the two given nodes are in the BST.

So we can simply use recursion and the property of a BST.

.. code-block:: java

     public TreeNode lowestCommonAncestor(
            TreeNode root,
            TreeNode p,
            TreeNode q) {

        if (root == null)
            return null;

        if (p.val <= root.val && q.val >= root.val) {
            return root;
        }
        else if (p.val < root.val && q.val < root.val) {
            return lowestCommonAncestor(root.left, p, q);
        }
        else if (p.val > root.val && q.val > root.val) {
            return lowestCommonAncestor(root.right, p, q);
        }

        return root;
    }

In the worst case ``p`` and ``q`` are leaf nodes who has the same parent. The time complexity would be O(h) where
``h`` is the height of the BST.
