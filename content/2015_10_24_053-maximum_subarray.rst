053-maximum_subarray
####################

:date: 2015-10-24 15:30
:tags: Subarray
:category: LeetCode
:slug: 053-maximum_subarray

`LeetCode Problem Link <https://leetcode.com/problems/maximum-subarray/>`_

The obvious straightforward solution takes O(n :superscript:`2`) time. But we can do better than that.

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

Another way to think of the problem is whenever you encounter a new number, you have a choice to make.
You either add the new number to the current running sum, or you begin a new running sum starting with this
new number. If adding the new number to the current running sum yields a greater sum than starting a new running
at the new number, then we should choose to add the new number to the current running sum.

On the other hand, if starting a new running sum yields a greater sum than adding the new number to the
current running sum, then we should choose to start a new running sum at this new number.

.. code-block:: java

    public int maxSubArray(int[] nums) {

        int n = nums.length;

        int sum = nums[0];
        int max = nums[0];

        for (int i=1; i<n; i++) {
            sum = Math.max(nums[i], nums[i] + sum);
            max = Math.max(sum, max);
        }

        return max;
    }

