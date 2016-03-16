quick_sort
##########

:date: 2016-3-15 21:13
:tags: Quick Sort, Sorting, Recursion
:category:
:slug: quick_sort

Note that in this implementation we always pick the last element as the pivot.
The implementation is simpler and the runtime would be the same for the same input array.

Unlike in quick select (215-kth_largest_element_in_an_array), we don't actually care about the rank for the pivot.
We just need to make sure that after the while loop, the pivot element is placed at the its sorted position.

Note the two recursive calls after the pivot element is properly placed.

.. code-block:: java

    public void quickSort(int[] nums) {

        if (nums==null ||nums.length == 0)
            return;

        quickSort(nums, 0, nums.length-1);
    }

    private void quickSort(int[] nums, int begin, int end) {

        if (begin >= end) {
            // 1 element or no element to sort
            return;
        }

        int pivot = end;
        int right = pivot - 1;
        int left = begin;

        // after the loop, left is the location where the pivot element should be placed
        while (left <= right) {
            if (nums[left] >= nums[pivot]) {
                swap(nums, left, right);
                right--;
            }
            else {
                left++;
            }
        }

        swap(nums, left, pivot);

        quickSort(nums, left + 1, end);
        quickSort(nums, begin, left - 1);
    }

    private void swap(int[] nums, int left, int right) {
        int tmp = nums[left];
        nums[left] = nums[right];
        nums[right] = tmp;
    }
