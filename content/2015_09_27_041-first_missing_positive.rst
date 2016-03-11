041-first_missing_positive
##########################

:date: 2015-9-27 19:50
:tags: Sorting, Bucket Sort
:category: LeetCode
:slug: 041-first_missing_positive

`LeetCode Problem Link <https://leetcode.com/problems/first-missing-positive/>`_

Finding the smallest positive number seen so far would not work.
I gave that as an answer during a phone interview.

I said sorting next. But failed to deal with duplicates.

This here handles duplicates find.

.. code-block:: java

    public int firstMissingPositive(int[] nums) {

        int smallest = Integer.MAX_VALUE;

        for (int i=0; i<nums.length; i++) {
            if (nums[i] <= 0)
                continue;

            if (nums[i] < smallest) {
                smallest = nums[i];
            }
        }

        return smallest + 1;
    }

Asked the runtime complexity. This is clearly O(nlogn).

Here's the O(n) space and O(1) time solution using a hash table.

.. code-block:: java

    public int firstMissingPositive(int[] nums) {

        HashSet<Integer> positiveNums = new HashSet<Integer>();

        for (int i=0; i<nums.length; i++) {
            if (nums[i] > 0) {
                positiveNums.add(nums[i]);
            }
        }

        int i=1;

        while (true) {
            if (!positiveNums.contains(i))
                return i;
            i++;
        }
    }

Finally this is the O(n) time and O(1) space solution.

This is O(n) time because there are at most ``n`` items to be swapped.

The idea is the same as bucket sort. We can place 1 at index 0, 2 at index 1, 3 and index 2, and so on.

The right location for positive integer ``x`` is ``x-1``.

.. code-block:: java

    public int firstMissingPositive(int[] nums) {

        for (int i=0; i<nums.length; i++) {
            if (nums[i] == i+1)
                continue;

            int index = nums[i] - 1;

            if (index >= 0 && index < nums.length && nums[i] != nums[index]) {
                swap(nums, i, index);
                i--; // decrement i because we want to examine the nums[i] again after the swap
            }
        }

        for (int i=0; i<nums.length; i++) {
            if (nums[i] != i+1) {
                return i+1;
            }
        }

        return nums.length+1;
    }
