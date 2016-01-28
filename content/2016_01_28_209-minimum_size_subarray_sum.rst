209-minimum_size_subarray_sum
#############################

:date: 2016-1-28 17:43
:tags: Sliding Window
:category: LeetCode
:slug: 209-minimum_size_subarray_sum

`LeetCode Problem Link <https://leetcode.com/problems/minimum-size-subarray-sum/>`_

The O(n) time approach uses a sliding window defined by ``start`` and ``end``.

.. code-block:: java

    public int minSubArrayLen(int s, int[] nums) {
        if (nums.length == 0)
            return 0;

        int start = 0;
        int end = 0;

        int sum = nums[start];
        int minLength = nums.length + 1;

        while (end < nums.length) {
            if (sum >= s) {
                int len = end - start + 1;
                if (len < minLength)
                    minLength = len;

                if (start < end) {
                    sum -= nums[start];
                    start++;
                }
            }
            else {
                end++;
                if (end < nums.length)
                    sum += nums[end];
            }
        }

        if (minLength == nums.length + 1)
            return 0;
        else
            return minLength;

    }

The O(n log n ) solution is trickier. We need to allocate an int array of size ``n+1`` call it ``sum``.

``sum[0]`` is 0, ``sum[i]`` is sum( nums[0], ..., nums[i-1] ).

Once we have this array built, we know that do ``sum[n] - sum[0]`` is sum( nums[0], ..., nums[n-1] and
``sum[a] - sum[b]`` = sum( nums[b], ..., nums[a-1]) provided that a > b.

In the outer for loop, we iterate ``i`` from 0 to ``n``, for each sum[i], we want to look for the lowest possible
``end`` index that satisfies ``sum[end] - sum[i] >= s`` The length of the subarray found is ``end - i``.

.. code-block:: java

    public int minSubArrayLen(int s, int[] nums) {
        int n = nums.length;
        int[] sum = new int[n+1];

        for (int i=1; i<n+1; i++) {
            sum[i] = sum[i-1] + nums[i-1];
        }
        //System.out.println(Arrays.toString(nums));
        //System.out.println(Arrays.toString(sum));

        /*  now sum[a] - sum[b]
         *    = sum( nums[b], ..., nums[a-1] )
         *  as long as x > i
         *
         *  sum[n] - sum[0] = sum (nums[0], ..., nums[n-1]) = sum of n values
         */

        int len = n + 1;

        for (int i=0; i<n; i++) {
            if (sum[n] - sum[i] < s)
                break;
            int end = binarySearch(i+1, n, sum[i]+s, sum);

            len = Math.min(len, end - i);
        }

        if (len == n + 1)
            return 0;
        else
            return len;
    }

    private int binarySearch(int low, int high, int key, int[] sum) {
        if (low == high)
            return low;

        int index = 0;
        int lastValidIndex = high;

        while (low < high) {
            index = low + (high-low)/2;

            if (sum[index] == key) {
                return index;
            }
            else if (sum[index] > key) {
                // too big
                lastValidIndex = index;
                high--;
            }
            else {
                // too small
                low++;
            }
        }

        return lastValidIndex;
    }


