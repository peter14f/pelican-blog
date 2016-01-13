167-two_sum_ii_input_array_is_sorted
####################################

:date: 2016-1-12 18:40
:tags: X-Sum
:category: LeetCode
:slug: 167-two_sum_ii_input_array_is_sorted
:status: draft

`LeetCode Problem Link <https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/>`_

Since the input array is sorted, we can do this in O(n) time.

.. code-block:: java

    public int[] twoSum(int[] numbers, int target) {
        int[] ans = {-1, -1};

        int r = numbers.length - 1;
        int l = 0;

        while (r > l) {
            int sum = numbers[l] + numbers[r];

            if (sum == target) {
                ans[0] = l + 1;
                ans[1] = r + 1;
                break;
            }
            else if (sum > target) {
                r--;
            }
            else {
                l++;
            }
        }

        return ans;
    }

