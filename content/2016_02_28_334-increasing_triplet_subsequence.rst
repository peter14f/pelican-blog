334-increasing_triplet_subsequence
##################################

:date: 2016-2-28 22:59
:tags:
:category: LeetCode
:slug: 334-increasing_triplet_subsequence

`LeetCode Problem Link <https://leetcode.com/problems/increasing-triplet-subsequence/>`_

Trivial solution is to use 3 nested for loops. But the time complexity is O(n :superscript:`3`).

.. code-block:: java

    public boolean increasingTriplet(int[] nums) {
        for (int i=0; i<nums.length-2; i++) {
            for (int j=i+1; j<nums.length-1; j++) {
                if (nums[j] <= nums[i])
                    continue;

                for (int k=j+1; k<nums.length; k++) {
                    if (nums[k] <= nums[j])
                        continue;

                    if (nums[k] > nums[j] && nums[j] > nums[i])
                        return true;
                }
            }
        }

        return false;
    }


Maintain ``smallestSeen`` and ``secondSmallestSeen`` s you traverse the array.

We had to do similar comparisons back in 265-paint_house_ii.

.. code-block:: java

    public boolean increasingTriplet(int[] nums) {

        int x = Integer.MAX_VALUE;
        int y = Integer.MAX_VALUE;

        for (int i=0; i<nums.length; i++) {

            if (nums[i] <= x) {
                x = nums[i]; // update smallest seen so far
            }
            else if (nums[i] <= y) {
                y = nums[i]; // update 2nd smallest seen so far
            }
            else {
                return true;
            }
        }

        return false;
    }

Note the **<=** comparision. It's important because it makes sure that a number the same as the
smallestSeen does not get pass the first if statement.


