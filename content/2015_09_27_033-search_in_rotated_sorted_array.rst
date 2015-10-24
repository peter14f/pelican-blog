033-search_in_rotated_sorted_array
##################################

:date: 2015-09-27 10:45
:tags: Binary Search
:category: LeetCode
:slug: 033-search_in_rotated_sorted_array

`LeetCode Problem Link <https://leetcode.com/problems/search-in-rotated-sorted-array/>`_

The best way is to list all rotated versions of a sorted array and then think about all cases.

| [1, 2, 3, 4, 5, 6, 7]
| [2, 3, 4, 5, 6, 7, 1]
| [3, 4, 5, 6, 7, 1, 2]
| [4, 5, 6, 7, 1, 2, 3]
| [5, 6, 7, 1, 2, 3, 4]
| [6, 7, 1, 2, 3, 4, 5]
| [7, 1, 2, 3, 4, 5, 6]
|
| nums[l] to nums[m] can be sorted like in case 1 ~ case 4.
| otherwise nums[m] to nums[h] must be sorted like in case 5 ~ case 7.

The ``target`` could lie within the sorted region or the non-sorted region.

Assume no duplicates exist in ``nums``.

.. code-block:: java

    public int search(int[] nums, int target) {

        int l = 0;
        int h = nums.length - 1;

        while (l <= h) {
            int middle = l + (h-l)/2;

            if (nums[middle] == target) {
                return middle;
            }
            else if (nums[l] == target) {
                return l;
            }
            else if (nums[h] == target) {
                return h;
            }

            if (nums[middle] >= nums[l]) {
                // l to middle is sorted

                if (target > nums[l] && target < nums[middle]) {
                    // within sorted region

                    h = middle - 1;
                    l = l + 1;
                }
                else {
                    l = middle + 1;
                }
            }
            else {
                // middle to h is sorted
                if (target > nums[middle] && target < nums[h]) {
                    // within sorted region

                    l = middle + 1;
                    h = h - 1;
                }
                else {

                    h = middle - 1;
                }
            }
        }

        return -1;
    }
