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
search until you hit the leaf node.

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

Here's the recursive approach. Either way I think the whole point is that the time complexity should
be O(h) instead of O(n). ``h`` is the height of the binary tree and ``n`` is the total number of nodes in
the BST.

.. code-block:: java

    public int closestValue(TreeNode root, double target) {
        int[] closestValue = {root.val};
        findClosestValue(root, target, closestValue);
        return closestValue[0];
    }

    private void findClosestValue(TreeNode node, double target, int[] closestVal) {

        if (node==null)
            return;

        double oldDiff = Math.abs(closestVal[0] - target);
        double newDiff = Math.abs(node.val - target);

        if (newDiff < oldDiff) {
            closestVal[0] = node.val;
        }

        if (newDiff==0)
            return;

        if (target > node.val) {
            findClosestValue(node.right, target, closestVal);
        }
        else {
            findClosestValue(node.left, target, closestVal);
        }
    }
