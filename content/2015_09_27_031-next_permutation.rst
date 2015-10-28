031-next_permutation
####################

:date: 2015-09-27 10:43
:tags: Permutations
:category: LeetCode
:slug: 031-next_permutation

`LeetCode Problem Link <https://leetcode.com/problems/next-permutation/>`_

| Start from the end of the array and find the first number that's not in ascending order.
| Say that number is at index ``pivotIndex``.
| Again start from the end of the array and find the first number that's bigger than ``nums[pivotIndex]``
| Say that number is at index ``swapIndex``
| swap the two numbers
| reverse the array from index ``pivotIdex + 1``

There is one exception, if all numbers are in ascending order, then simply reverse the whole array.

.. code-block:: java

    public void nextPermutation(int[] nums) {

        int pivotIndex = -1;

        for (int i=nums.length - 2; i>=0; i--) {
            if (nums[i] < nums[i+1]) {
                pivotIndex = i;
                break;
            }
        }

        if (pivotIndex == -1) {
            reverseArray(nums, 0, nums.length - 1);
        }
        else {
            int swapIndex = -1;

            // swapIndex is the first number found that's bigger than nums[pivotIndex]
            for (int i=nums.length - 1; i>=0; i--) {
                if (nums[i] > nums[pivotIndex]) {
                    swapIndex = i;
                    break;
                }
            }

            int temp = nums[pivotIndex];
            nums[pivotIndex] = nums[swapIndex];
            nums[swapIndex] = temp;
            reverseArray(nums, pivotIndex + 1, nums.length - 1);
        }
    }

    // reverse the section of the the array nums [low, high]
    private void reverseArray(int[] nums, int low, int high) {
        while (low < high) {
            int temp = nums[low];
            nums[low] = nums[high];
            nums[high] = temp;
            low++;
            high--;
        }
    }

