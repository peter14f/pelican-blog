108-convert_sorted_array_to_binary_search_tree
##############################################

:date: 2015-11-26 17:57
:tags: Binary Search Trees, Recursion
:category: LeetCode
:slug: 108-convert_sorted_array_to_binary_search_tree

`LeetCode Problem Link <https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/>`_

Use recursion. The middle element is already the root. This is because we're trying to build a height balanced BST.
Otherwise, we could have simply build a linked list.

.. code-block:: java

    public TreeNode sortedArrayToBST(int[] nums) {

        if (nums.length == 0)
            return null;

        return sortedArrayToBST(nums, 0, nums.length - 1);

    }

    private TreeNode sortedArrayToBST(int[] nums, int low, int high) {

        int middle = low + (high-low)/2;

        TreeNode root = new TreeNode(nums[middle]);

        if (middle - 1 >= low) {
            root.left = sortedArrayToBST(nums, low, middle - 1);
        }

        if (middle + 1 <= high) {
            root.right = sortedArrayToBST(nums, middle + 1, high);
        }

        return root;
    }
    
