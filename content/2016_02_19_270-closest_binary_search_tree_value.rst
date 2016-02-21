270-closest_binary_search_tree_value
####################################

:date: 2016-2-19 23:13
:tags: Binary Search Trees, Closest Value In BST
:category: LeetCode
:slug: 270-closest_binary_search_tree_value

`LeetCode Problem Link <https://leetcode.com/problems/closest-binary-search-tree-value/>`_

Record the closest element traversed so far and the minimum difference.

The iterative approach definitely makes more sense here.

Just because the diff is greater than the min diff, it does not mean you should stop there. Continue with the BST
search.

.. code-block:: java

    // tree is non-empty
    public int closestValue(TreeNode root, double target) {

        TreeNode cur = root;
        double minDiff = Math.abs(root.val - target);
        int curVal = root.val;

        while (cur != null) {
            double myDiff = Math.abs(cur.val - target);

            if (myDiff < minDiff) {
                minDiff = myDiff;
                curVal = cur.val;
            }

            if (cur.val == target) {
                break;
            }
            else if (cur.val > target) {
                // too big
                cur = cur.left;
            }
            else {
                // too small
                cur = cur.right;
            }
        }

        return curVal;
    }
