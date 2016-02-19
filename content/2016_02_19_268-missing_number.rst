268-missing_number
##################

:date: 2016-2-19 13:40
:tags:
:category: LeetCode
:slug: 268-missing_number

`LeetCode Problem Link <https://leetcode.com/problems/missing-number/>`_

This problem is trivial if you can use a hashtable. But we're asked to do this in O(n) time and O(1) space.

We can find the sum of integers from 0 to n.

sum = (n+1)*(n+0)/2

The actual sum over the array must be smaller or the same.

The difference is the missing number.

.. code-block:: java

    public int missingNumber(int[] nums) {
        int n = nums.length;

        int expectedSum = (n+1)*n/2;

        int actualSum = 0;

        for (int i=0; i<nums.length; i++) {
            actualSum += nums[i];
        }

        int difference = expectedSum - actualSum;

        return difference;
    }

I saw another way to do this problem by swapping numbers into the correct bucket. Just need to make sure that
after swapping, make sure you decrement i because you need to check the number just swapped here again.

.. code-block:: java

    public int missingNumber(int[] nums) {

        for (int i=0; i<nums.length; i++) {
            if (nums[i] == nums.length) {
                nums[i] = -1;
                i--;
            }
            else if (nums[i] != i && nums[i] >= 0) {
                swap(nums, nums[i], i);
                i--;
            }
        }

        for (int i=0; i<nums.length; i++) {
            if (nums[i] != i) {
                return i;
            }
        }

        return nums.length;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
