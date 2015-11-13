026-remove_duplicates_from_sorted_array
#######################################

:date: 2015-09-07 20:28
:tags: Remove Duplicates, Sorted Array
:category: LeetCode
:slug: 026-remove_duplicates_from_sorted_array

`LeetCode Problem Link <https://leetcode.com/problems/reverse-nodes-in-k-group/>`_

The solution I came up with is to simply overwrite the array as we go.

``i`` should start at 1 as nums[0] must be the smallest number.

.. code-block:: java

    public int removeDuplicates(int[] nums) {

        if (nums==null || nums.length==0)
            return 0;

        int i = 0;

        for (int j=1; j<nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }

        return i+1;
    }