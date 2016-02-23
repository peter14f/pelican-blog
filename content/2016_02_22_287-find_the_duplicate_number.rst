287-find_the_duplicate_number
#############################

:date: 2016-2-22 10:43
:tags:
:category: LeetCode
:slug: 287-find_the_duplicate_number

`LeetCode Problem Link <https://leetcode.com/problems/find-the-duplicate-number/>`_

input array ``nums`` is of size ``n+1`` and each number is in the range [1, n], we are ask to find
a duplicated element.

1) You must not modify the array ---> cannot sort.
2) O(1) space ---> don't use a hash table
3) do better than O(n \ :superscript:`2`) time ---> no two nested for loops
4) only one duplicate number, but may repeat more than once

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


