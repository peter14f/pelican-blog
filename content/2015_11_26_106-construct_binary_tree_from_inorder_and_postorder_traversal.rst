106-construct_binary_tree_from_inorder_and_postorder_traversal
##############################################################

:date: 2015-11-26 12:40
:tags: Binary Trees, Recursion
:category: LeetCode
:slug: 106-construct_binary_tree_from_inorder_and_postorder_traversal

`LeetCode Problem Link <https://leetcode.com/problems/maximum-depth-of-binary-tree/>`_

It's very similar to the previous problem 105-construct_binary_tree_from_preorder_and_inorder_traversal.
Use recursion. ``postorder[pHigh]`` is always the root. Try to find that value in ``inorder``. Once found,
the numbers to the left belong in the left subtree and the numbers to the right belong in the right subtree.

.. code-block:: java

    public TreeNode buildTree(int[] inorder, int[] postorder) {

        if (inorder.length != postorder.length)
            throw new IllegalArgumentException();

        int n = inorder.length;

        if (n==0)
            return null;

        return buildTree(inorder, 0, n-1, postorder, 0, n-1);
    }

    private TreeNode buildTree(int[] inorder, int iLow, int iHigh,
                               int[] postorder, int pLow, int pHigh) {

        TreeNode root = new TreeNode(postorder[pHigh]);

        int rootIndex = -1;
        for (int i=iLow; i<=iHigh; i++) {
            if (inorder[i] == root.val) {
                rootIndex = i;
                break;
            }
        }

        if (rootIndex==-1)
            throw new IllegalArgumentException();

        int numLeft = rootIndex - iLow;
        if (numLeft > 0) {
            root.left = buildTree(inorder, iLow, rootIndex-1,
                                  postorder, pLow, pLow+numLeft-1);
        }

        int numRight = iHigh - rootIndex;
        if (numRight > 0) {
            root.right = buildTree(inorder, rootIndex+1, iHigh,
                                   postorder, pHigh-numRight, pHigh-1);
        }

        return root;
    }