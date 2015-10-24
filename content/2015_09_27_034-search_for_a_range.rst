034-search_for_a_range
######################

:date: 2015-09-27 10:46
:tags: Binary Search
:category: LeetCode
:slug: 034-search_for_a_range

`LeetCode Problem Link <https://leetcode.com/problems/search-for-a-range/>`_

Run the regular binary search, once the ``target`` if found, we cannot just stop searching. We must continue looking
for a higher index and a lower index that also store ``target``.

.. code-block:: java

    public int[] searchRange(int[] nums, int target) {

        int[] ans = {-1, -1};

        int l = 0;
        int h = nums.length - 1;

        while (l <= h) {
            int middle = l + (h-l)/2;

            if (nums[middle] == target) {
                ans[0] = middle;
                ans[1] = middle;

                // look for a lower low index
                lookForLowIndex(nums, target, middle, ans);

                // look for a higher high index
                lookForHighIndex(nums, target, middle, ans);
                break;
            }
            else if (nums[middle] > target) {
                // look in the left part
                h = middle - 1;
            }
            else {
                // look in the right part
                l = middle + 1;
            }
        }

        return ans;
    }

    private void lookForLowIndex(int[] nums, int target, int foundIndex, int[] ans) {
        int h = foundIndex - 1;
        int l = 0;

        while (l <= h) {
            int middle = l + (h-l)/2;

            if (nums[middle] == target) {
                ans[0] = middle;
                lookForLowIndex(nums, target, middle, ans);
                break;
            }
            else if (nums[middle] > target) {
                // look in the left part
                h = middle - 1;
            }
            else {
                // look in the right part
                l = middle + 1;
            }
        }
    }

    private void lookForHighIndex(int[] nums, int target, int foundIndex, int[] ans) {
        int h = nums.length - 1;
        int l = foundIndex + 1;

        while (l <= h) {
            int middle = l + (h-l)/2;

            if (nums[middle] == target) {
                ans[1] = middle;
                lookForHighIndex(nums, target, middle, ans);
                break;
            }
            else if (nums[middle] > target) {
                // look in the left part
                h = middle - 1;
            }
            else {
                // look in the right part
                l = middle + 1;
            }
        }
    }