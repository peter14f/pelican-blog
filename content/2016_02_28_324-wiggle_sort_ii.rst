324-wiggle_sort_ii
##################

:date: 2016-2-28 1:12
:tags: Wiggle Sort
:category: LeetCode
:slug: 324-wiggle_sort_ii

`LeetCode Problem Link <https://leetcode.com/problems/wiggle-sort-ii/>`_

Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Reorder ``nums`` in-place such that

::

    nums[0] < nums[1] > nums[2] < nums[3]

Wait, how is this different from 280-wiggle_sort?

Adjacent elements cannot be equal! The O(n) time solution to wiggle_sort_i will no longer work here.

Using sorting, this does not work either. Since if the middle elements in the sorted array are
duplicates.

.. code-block:: java

    public void wiggleSort(int[] nums) {

        int[] sorted = new int[nums.length];

        for (int i=0; i<nums.length; i++) {
            sorted[i] = nums[i];
        }

        Arrays.sort(sorted);

        int r = sorted.length - 1;
        int l = 0;

        int i=0;

        while (r >= l) {

            if (i%2 == 0) {
                nums[i] = sorted[l];
                l++;
            }
            else {
                nums[i] = sorted[r];
                r--;
            }
            i++;
        }
    }

Instead we can partition the sorted array into two halves, the small half and the big half.

Think of this n=5 case, [1, 1, 1, 2, 2]

We must have the the size of the small half to be 1 bigger than the big half in the case when
n is odd.

.. code-block:: java

    public void wiggleSort(int[] nums) {
        int[] sorted = new int[nums.length];

        for (int i=0; i<nums.length; i++) {
            sorted[i] = nums[i];
        }

        Arrays.sort(sorted);

        int l = nums.length/2;
        int r = nums.length - 1;

        if (nums.length % 2 == 0) {
            l--;
        }

        int i=0;

        while (i< nums.length) {
            if (i%2 == 0) {
                nums[i] = sorted[l];
                l--;
            }
            else {
                nums[i] = sorted[r];
                r--;
            }
            i++;
        }
    }

Note that we are starting at the back of each half. This makes sure that our two choices do not get any
closer.


