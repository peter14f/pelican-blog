035-search_insert_position
##########################

:date: 2015-09-27 10:47
:tags: Binary Search
:category: LeetCode
:slug: 035-search_insert_position

`LeetCode Problem Link <https://leetcode.com/problems/search-insert-position/>`_

Use binary search. If the number is not found, the ``l`` pointer actually will be the correct index if the
number were to be inserted.

.. code-block:: java

    public int searchInsert(int[] nums, int target) {

        int l = 0;
        int h = nums.length - 1;

        while (l <= h) {

            int middle = l + (h-l)/2;
            int middleNum = nums[middle];

            if (middleNum == target) {
                return middle;
            }
            else if (middleNum > target) {
                // look in the left part
                h = middle - 1;
            }
            else {
                // look in the right part
                l = middle + 1;
            }

        }

        // not found, and now l == h + 1
        return l;
    }
