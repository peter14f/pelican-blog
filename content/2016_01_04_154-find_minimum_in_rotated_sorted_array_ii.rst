154-find_minimum_in_rotated_sorted_array_ii
###########################################

:date: 2016-1-4 21:26
:tags: Rotated Sorted Array, Binary Search
:category: LeetCode
:slug: 154-find_minimum_in_rotated_sorted_array_ii

`LeetCode Problem Link <https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/>`_

Depending on the input array, the worst case time complexity will be O(n).

We need to use a variable ``min`` to keep track of the smallest element found so far.
Even when we are throwing away the sorted half of the array. We should update ``min`` to the
smallest number on the sorted half if it's smaller.

A good example to show that this is needed is ``[3, 1, 3]``.

.. code-block:: java

  public int findMin(int[] nums) {
        int l = 0;
        int h = nums.length - 1;
        int min = nums[0];

        while (h >= l) {
            if (h==l) {
                min = Math.min(min, nums[l]);
                break;
            }
            else if (h == l + 1) {
                min = Math.min(min, Math.min(nums[h], nums[l]));
                break;
            }


            if (nums[h] > nums[l]) {
                min = Math.min(min, nums[l]);
                break;
            }

            int m = l + (h-l)/2;

            if (nums[m] > nums[l]) {
                min = Math.min(min, nums[l]);
                l = m + 1;
            }
            else if (nums[m] == nums[l]) {
                l++;
            }
            else if (nums[h] > nums[m]) {
                min = Math.min(min, nums[m]);
                h = m - 1;
            }
            else if (nums[m] == nums[h]) {
                h--;
            }
        }

        return min;
    }
