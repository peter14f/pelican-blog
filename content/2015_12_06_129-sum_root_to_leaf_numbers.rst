129-sum_root_to_leaf_numbers
############################

:date: 2015-12-6 16:11
:tags: DFS, Recursion, Binary Trees
:category: LeetCode
:slug: 129-sum_root_to_leaf_numbers

`LeetCode Problem Link <https://leetcode.com/problems/sum-root-to-leaf-numbers/>`_

The nodes in the binary tree have integer values from 0 to 9.

.. code-block:: java

    // values are integers from 0 to 9 only
    public int sumNumbers(TreeNode root) {
        if (root==null)
            return 0;

        int curNum = 0;
        int totalSum[] = {0};

        sumNumbers(root, curNum, totalSum);

        return totalSum[0];
    }

    private void sumNumbers(TreeNode node, int curSum, int[] totalSum) {
        curSum = curSum*10 + node.val;

        if (node.left == null && node.right == null) {
            totalSum[0] += curSum;
            return;
        }

        if (node.left != null)
            sumNumbers(node.left, curSum, totalSum);

        if (node.right != null)
            sumNumbers(node.right, curSum, totalSum);
    }

Each node is visited once so the time complexity is O(n).
