337-house_robber_iii
####################

:date: 2016-3-15 10:59
:tags: House Robber
:category: LeetCode
:slug: 337-house_robber_iii

`LeetCode Problem Link <https://leetcode.com/problems/house-robber-iii/>`_

At the very first glance, I thought we could use level order traversal and simply get the odd level sum and the
even level sum and then return the max of the two.

But it turns out that would not work. Here are two examples.

::

    Example # 1

          4
         /
        1
       /
      2
     /
    3


    Example # 2

      2
     / \
    1   3
     \
      4

In the first example, the max profit is 7 instead 6.
In the second example, the max profit is 7 as well, which involves robbing 1 house at level 1 and 1 house at level 2.

We should figure out the max profit from the bottom of the binary tree. If we decide to rob the current node, then we
must not rob either of its child. On the other hand, if we decide not to rob the current node, then there is no
restriction whether to rob the children or not. We should there do it in the way the maximizes the profit.

.. code-block:: java

    public int rob(TreeNode root) {
        int[] profit = profit(root);

        return Math.max(profit[0], profit[1]);
    }

    // return profit[] which is an int array of size 2
    // profit[0] is the max profit robbing houses in the subtree
    // with node being the root and node is robbed
    //
    // profit[1] is the max profit robbing houses in the subtree
    // with node being the root and node is NOT robbed
    private int[] profit(TreeNode node) {
        if (node==null) {
            int[] profit = {0, 0};
            return profit;
        }

        int[] profit = new int[2];

        int[] left = profit(node.left);
        int[] right = profit(node.right);

        // rob node, but not node.left and not node.right
        profit[0] = node.val + left[1] + right[1];

        // not robbing node, so no restriction on whether
        // node.left is robbed and whether node.right is robbed
        // We pick the way that gives the most amount of profit
        profit[1] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);

        return profit;
    }

We use recursion and each node is visited once, therefore the time complexity should be O(n).
Obviously recursion comes at the cost of the O(h) space complexity.