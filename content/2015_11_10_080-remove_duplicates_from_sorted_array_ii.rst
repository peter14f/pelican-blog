080-remove_duplicates_from_sorted_array_ii
##########################################

:date: 2015-11-10 22:25
:tags: Remove Duplicates, Sorted Array
:category: LeetCode
:slug: 080-remove_duplicates_from_sorted_array_ii

`LeetCode Problem Link <https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/>`_

This is a followup problem for 026-remove_duplicates_from_sorted_array. The idea is the same, we just have to
keep a counter to keep track of the number of times a number has show up in the sorted array consecutively.

.. code-block:: java

    public int removeDuplicates(int[] nums) {
        if (nums==null)
            return 0;
        if (nums.length < 3) {
            return nums.length;
        }

        int lastNum = nums[0];
        int cnt = 1;
        int index = 1;

        for (int i=1; i<nums.length; i++) {
            if (nums[i] == lastNum) {
                cnt++;
            }
            else {
                cnt = 1;
            }

            lastNum = nums[i];

            if (cnt < 3) {
                nums[index] = lastNum;
                index++;
            }
        }

        return index;
    }

