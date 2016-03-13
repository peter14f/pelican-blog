230-kth_smallest_element_in_a_bst
#################################

:date: 2016-2-10 18:27
:tags: Binary Search Trees, Recursion
:category: LeetCode
:slug: 230-kth_smallest_element_in_a_bst

`LeetCode Problem Link <https://leetcode.com/problems/kth-smallest-element-in-a-bst/>`_

In the following approach, I basically use the iterative inorder traversal. Return the
kth number once it's found. The time complexity is O(n) and the space complexity is O(h).ffsdfds

.. code-block:: java

    public int kthSmallest(TreeNode root, int k) {
      int i = 0;

      Stack<TreeNode> stk = new Stack<TreeNode>();
      TreeNode cur = root;

      while (!stk.isEmpty() || cur != null) {

        if (cur == null) {
          TreeNode top = stk.pop();
          i++;

          if (i == k)
            return top.val;

          cur = top.right;

        }
        else {
          stk.push(cur);
          cur = cur.left;
        }
      }

      return Integer.MIN_VALUE;
    }

This is a bad recursion. In the case of k=1, we have to repeated find the size of the trees over and over again.

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

If you want to do this recursively. Here is the proper way of doing it.

.. code-block:: java

    public int kthSmallest(TreeNode root, int k) {

        int[] i = {0};
        int[] ans = {0};

        inorderKth(root, k, i, ans);

        return ans[0];
    }

    private void inorderKth(TreeNode node, int k, int[] i, int[] ans) {

        if (node==null)
            return;

        inorderKth(node.left, k, i, ans);

        if (i[0] == k)
            return;

        i[0]++;

        if (i[0] == k)
            ans[0] = node.val;

        inorderKth(node.right, k, i, ans);
    }




The follow-up asks for an optimization if the BST is inserting and deleting happens frequently.
The hint even says that we can modify the BST node structure.

What we will do is then keep another field in each node, ``numLeftNodes``. This is the number of nodes in the left
subtree. As long as we keep that field updated as we do insert and delete, we can guarantee that getting the
kth node takes O(h) time where ``h`` is the height of the BST.
