041-first_missing_positive
##########################

:date: 2015-9-27 19:50
:tags:
:category: LeetCode
:slug: 041-first_missing_positive

`LeetCode Problem Link <https://leetcode.com/problems/first-missing-positive/>`_

The input array ``nums`` is of size ``n`` and could have integers < 1.

In the first pass, we try to place the number (``nums[i]``) in the correct bin if the number
is >= 1 and <= n. The correct bin is at index ``nums[i] - 1``.

1 should be stored at index 1, 2 should be stored at index 1, ... etc.

We continue swapping the number at index ``i`` with the number at the desired index until either index ``i`` now stores
 the number ``i+1`` or the number at index ``i`` cannot be placed in the desired location. (The number is less than 1 or
 greater than ``n``)

Even though there is a while loop, but there are at most n numbers that need to move to a different bin. So the
first pass takes O(n) time.

In the second pass, we check if ``nums[i] != i + 1`` then ``i+1`` is the first missing positive.
If no such number is found, we return ``n+1``

.. code-block:: java

     public int firstMissingPositive(int[] nums) {

        // at most n numbers will be placed
        for (int i=0; i<nums.length; i++) {

            int num = nums[i];
            int newIndex = num - 1;

            while (num > 0 && newIndex >= 0 && newIndex < nums.length && nums[newIndex] != num) {
                int temp = nums[newIndex];
                nums[newIndex] = num;
                nums[i] = temp;

                num = temp;
                newIndex = num - 1;
            }
        }

        int ans = nums.length + 1;

        for (int i=0; i<nums.length; i++) {
            if (nums[i] != i + 1) {
                ans = i + 1;
                break;
            }
        }

        return ans;
    }