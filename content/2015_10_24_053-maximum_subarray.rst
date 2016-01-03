053-maximum_subarray
####################

:date: 2015-10-24 15:30
:tags: Contiguous Subarray
:category: LeetCode
:slug: 053-maximum_subarray

`LeetCode Problem Link <https://leetcode.com/problems/maximum-subarray/>`_

The obvious straightforward solution takes O(n) time. But we can do better than that.


The only time we want to start counting from the current number is when the accumulated sum so far is negative and
the current number bigger than the accumulated sum.

.. code-block:: java

    public int maxSubArray(int[] nums) {

        int sum = nums[0];
        int maxSum = sum;

        for (int i=1; i<nums.length; i++) {
            if (sum < 0 && nums[i] > sum)
                sum = nums[i];
            else
                sum += nums[i];

            if (sum > maxSum)
                maxSum = sum;
        }

        return maxSum;
    }

