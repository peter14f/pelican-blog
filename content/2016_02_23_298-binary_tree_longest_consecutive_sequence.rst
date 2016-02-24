298-binary_tree_longest_consecutive_sequence
############################################

:date: 2016-2-23 8:26
:tags: DFS, Recursion
:category: LeetCode
:slug: 298-binary_tree_longest_consecutive_sequence

`LeetCode Problem Link <https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/>`_

This is a binary tree, not necessarily a binary search tree.

My idea is to use DFS and recursion.

.. code-block:: java

    public int longestConsecutive(TreeNode root) {
        return findLongestConsecutive(root, 0, 0);
    }

    private int findLongestConsecutive(TreeNode node, int curLength, int prevNum) {

        if (node==null) {
            return curLength;
        }

        int left = 0;
        int right = 0;

        if (curLength==0) {
            left = findLongestConsecutive(node.left, 1, node.val);
            right = findLongestConsecutive(node.right, 1, node.val);
        }
        else {
            if (node.val == prevNum + 1) {
                left = findLongestConsecutive(node.left, curLength+1, node.val);
                right = findLongestConsecutive(node.right, curLength+1, node.val);
            }
            else {
                // in this case curLength might be longer than digger further
                left = findLongestConsecutive(node.left, 1, node.val);
                right = findLongestConsecutive(node.right, 1, node.val);
                return Math.max(curLength, Math.max(left, right));
            }
        }

        return Math.max(left,  right);
    }

