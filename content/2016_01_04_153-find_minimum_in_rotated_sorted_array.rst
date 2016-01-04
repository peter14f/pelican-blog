153-find_minimum_in_rotated_sorted_array
########################################

:date: 2016-1-4 12:57
:tags: Binary Search, Rotated Sorted Array
:category: LeetCode
:slug: 153-find_minimum_in_rotated_sorted_array

`LeetCode Problem Link <https://leetcode.com/problems/maximum-product-subarray/>`_

Reminds me of 33-search_in_rotated_sorted_array. It helps to write all versions of a rotated sorted array out.

When the input array is sorted, return the element at the lowest index.
If ``l == h``, then return the only element.
If ``h == l + 1``, then return the smaller element.
In other cases, we know that the array is rotated in some way,
we can find the middle index ``m`` and throw away the sorted part of the array.

.. code-block:: java

  public int findMin(int[] nums) {
        int l = 0;
        int h = nums.length - 1;

        while (h >= l) {
            if (h==l)
                return nums[l];
            else if (h == l + 1) {
                if (nums[h] > nums[l])
                    return nums[l];
                else
                    return nums[h];
            }


            if (nums[h] > nums[l]) {
                return nums[l];
            }

            int m = l + (h-l)/2;

            if (nums[m] > nums[l]) {
                l = m + 1;
            }
            else {
                h = m;
            }
        }

        return Integer.MIN_VALUE;
    }
