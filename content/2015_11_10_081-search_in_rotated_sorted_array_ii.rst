081-search_in_rotated_sorted_array_ii
#####################################

:date: 2015-11-10 22:31
:tags: Binary Search
:category: LeetCode
:slug: 081-search_in_rotated_sorted_array_ii

`LeetCode Problem Link <https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/>`_

This is a followup problem for 033-search_in_rotated_sorted_array.rst.

Allowing duplicates means we can no longer easily detect if numbers from index ``low`` to
index ``middle`` are sorted or not. Let's check the following example:

The array ``[1, 3, 1, 1, 1]`` is sorted and then rotated. Using binary search, the ``low`` index would start
at ``0`` and the ``high`` index would start at ``4``. ``middle`` would therefore be ``2``. But guess what?
``nums[low]`` and ``numbers[middle]`` are both 1. But the section of the array from ``low`` to ``middle`` is
actually not sorted.


So what can we do when we are not able to tell which section of the current input array is sorted? Not much really.
We can eliminate one choice from the input set by decrementing ``high``. Before we do that, we need to make sure that
``nums[high]`` is actually not ``target``.

So what would be the worst case? An long array filled with duplicates except for one number and that number is at index
``low+1``. The time complexity is O(n). Yet for a lot of other cases (inputs without duplicates for example), the time
complexity can be as good as O(log n)

.. code-block:: java

    public boolean search(int[] nums, int target) {
        int l = 0;
        int h = nums.length - 1;

        while (l<=h) {
            int m = l + (h-l)/2;
            System.out.println("l=" + l + " h=" + h + " m=" + m);

            if (nums[m] == target) {
                return true;
            }

            if (nums[l] < nums[m]) {
                // we're sure that l to m is sorted
                if (target >= nums[l] && target < nums[m]) {
                    // target lies within the sorted range
                    h = m -1;
                }
                else {
                    // if target exists, it's in the other half
                    l = m + 1;
                }
            }
            else if (nums[h] > nums[m]) {
                // we're sure that m to h is sorted
                if (target > nums[m] && target <= nums[h]) {
                    l = m + 1;
                }
                else {
                    // if target exists, it's in the other half
                    h = m - 1;
                }
            }
            else {
                // cannot determine which half is sorted
                if (nums[h]==target)
                    return true;
                // h is also not the answer, decrement h now
                // note that in this particular step, we're going
                // eliminating the input set by one element
                h--;
            }
        }

        return false;
    }