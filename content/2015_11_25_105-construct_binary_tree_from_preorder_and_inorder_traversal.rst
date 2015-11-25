105-construct_binary_tree_from_preorder_and_inorder_traversal
#############################################################

:date: 2015-11-25 21:58
:tags: Binary Trees
:category: LeetCode
:slug: 105-construct_binary_tree_from_preorder_and_inorder_traversal

`LeetCode Problem Link <https://leetcode.com/problems/maximum-depth-of-binary-tree/>`_

Use recursion, ``preorder[pLow]`` is always the root. Try to find that value in ``inorder``. Once found, the numbers to
the left belong in the left subtree and the numbers to the right belong in the right subtree.

.. code-block:: java

    public TreeNode buildTree(int[] preorder, int[] inorder) {

        if (preorder.length != inorder.length)
            throw new IllegalArgumentException();

        int n = preorder.length;

        if (n==0)
            return null;

        return buildTree(preorder, 0, n-1, inorder, 0, n-1);
    }

    private TreeNode buildTree(int[] preorder, int pLow, int pHigh,
                               int[] inorder, int iLow, int iHigh) {

        TreeNode root = new TreeNode(preorder[pLow]);
        int rootIndex = -1;
        for (int i=iLow; i<=iHigh; i++) {
            if (inorder[i] == root.val) {
                rootIndex = i;
                break;
            }
        }

        if (rootIndex == -1)
            throw new IllegalArgumentException();

        int numLeft = rootIndex-iLow;
        if (numLeft > 0) {
            root.left = buildTree(preorder, pLow+1, pLow+numLeft,
                                  inorder, iLow, rootIndex-1);
        }

        int numRight = iHigh-rootIndex;
        if (numRight > 0) {
            root.right = buildTree(preorder, pLow+numLeft+1, pHigh,
                                   inorder, rootIndex+1, iHigh);
        }

        return root;
    }