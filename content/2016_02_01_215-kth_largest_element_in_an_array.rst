215-kth_largest_element_in_an_array
###################################

:date: 2016-2-1 13:10
:tags: Quick Select
:category: LeetCode
:slug: 215-kth_largest_element_in_an_array

`LeetCode Problem Link <https://leetcode.com/problems/kth-largest-element-in-an-array/>`_

``left`` is the final location where the pivot element should be placed.
In this implementation, we always pick the element at ``end`` index as the pivot.

.. code-block:: java

    public int findKthLargest(int[] nums, int k) {
        if (k<1 || k>nums.length)
            throw new IllegalArgumentException();

        return findKth(nums, 0, nums.length-1, k);
    }

    private int findKth(int[] nums, int start, int end,  int k) {
        int pivot = end;
        int left = start;
        int right = end - 1;

        while (left <= right) {
            if (nums[left] > nums[pivot]) {
                swap(nums, left, right);
                right--;
            }
            else {
                left++;
            }
        }

        // left is the final position where the pivot element should be placed
        swap(nums, left, pivot);

        int rank = nums.length - left;

        if (rank == k) {
            return nums[left];
        }
        else if (rank > k) {
            return findKth(nums, left+1, end, k);
        }
        else {
            return findKth(nums, start, left-1, k);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

The worst case runtime complexity is O(n\ :superscript:`2`). The average runtime complexity is O(n).
