230-kth_smallest_element_in_a_bst
#################################

:date: 2016-2-10 18:27
:tags: Binary Search Trees, Recursion
:category: LeetCode
:slug: 230-kth_smallest_element_in_a_bst

`LeetCode Problem Link <https://leetcode.com/problems/majority-element-ii/>`_

I use recursion to solve the original problem. In the method, I find the size of the left subtree first. If the left
subtree has a size of ``l`` and ``k`` happens to be ``l+1``, then we know the root is the answer. If ``k<=l``, then
we know the answer is in the left subtree. If ``k > l+1``, then we know the answer is in the right subtree.

.. code-block:: java

    public int kthSmallest(TreeNode root, int k) {
        int leftSize = getTreeSize(root.left);

        if (leftSize + 1 == k)
            return root.val;

        if (k <= leftSize)
            return kthSmallest(root.left, k);

        return kthSmallest(root.right, k - 1 - leftSize);
    }

    private int getTreeSize(TreeNode node) {
        if (node==null)
            return 0;

        int leftSize = getTreeSize(node.left);
        int rightSize = getTreeSize(node.right);

        return leftSize + rightSize + 1;
    }

What is the runtime complexity? In the worst case, k happens to be the right most leaf in the BST. In this case,
the algorithm takes O(n).

The follow-up asks for an optimization if the BST is inserting and deleting happens frequently.
The hint even says that we can modify the BST node structure.

What we will do is then keep another field in each node, ``numLeftNodes``. This is the number of nodes in the left
subtree. As long as we keep that field updated as we do insert and delete, we can guarantee that getting the
kth node takes O(h) time where ``h`` is the height of the BST.
