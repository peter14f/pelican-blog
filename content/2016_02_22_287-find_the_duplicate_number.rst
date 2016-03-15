287-find_the_duplicate_number
#############################

:date: 2016-2-22 10:43
:tags: Bucket Sort
:category: LeetCode
:slug: 287-find_the_duplicate_number

`LeetCode Problem Link <https://leetcode.com/problems/find-the-duplicate-number/>`_

input array ``nums`` is of size ``n+1`` and each number is in the range [1, n], we are ask to find
a duplicated element.

1) You must not modify the array ---> cannot sort.
2) O(1) space ---> don't use a hash table
3) do better than O(n \ :superscript:`2`) time ---> no two nested for loops
4) only one duplicate number, but may repeat more than once

Just use bucket sort. Place ``1`` at bucket 0. Place ``2`` at bucket 1. Place ``x`` at bucket (x-1).

If the index we are trying to move to already contains the same number, then there must be a duplicate.

.. code-block:: java

    public int findDuplicate(int[] nums) {
        // use bucket sort
        // store 1 at [0]
        // store 2 at [1]
        // store x at [x-1]
        for (int i=0; i<nums.length; i++) {
            int index = nums[i] - 1;

            if (i != index) {

                if (nums[index] == nums[i]) {
                    // the index we're trying to move nums[i] to
                    // alreay contains the same number as nums[i] --> a duplicate is found
                    return nums[i];
                }
                else {
                    swap(nums, index, i);
                    i--;
                }
            }
        }

        return Integer.MAX_VALUE;
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }


The bucket sort approach is straightforward. I wouldn't recommend using the binary search approach.

.. code-block:: java

    public int findDuplicate(int[] nums) {

        int l = 1;
        int h = nums.length-1;

        while (l < h) {
            int m = l + (h-l)/2;

            int cnt = 0;

            for (int i=0; i<nums.length; i++) {
                if (nums[i] <= m)
                    cnt++;
            }

            if (cnt <= m) {
                // repeated value must be in [m+1, h]
                l = m + 1;
            }
            else {
                // repeated value must be in [l, m]
                h = m;
            }

        }

        return h;
    }


