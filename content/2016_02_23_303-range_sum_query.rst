303-range_sum_query
###################

:date: 2016-2-23 20:34
:tags: Memoization, Range Sum
:category: LeetCode
:slug: 303-range_sum_query

`LeetCode Problem Link <https://leetcode.com/problems/range-sum-query-immutable/>`_

There are many calls to ``sumRange()``, so if we can store the result then ``sumRange()`` can become O(1) time.

We could use a 2d int array called ``sum`` where ``sum[i][j]`` is the sum from index ``i`` all the way to
index ``j``.

.. code-block:: java

    public class NumArray {

        int[][] sum;

        public NumArray(int[] nums) {
            int n = nums.length;

            sum = new int[n][n];

            for (int row=0; row<n; row++) {
                // sum over a single value
                sum[row][row] = nums[row];
            }

            // d is the distance from diagonal
            for (int d=1; d<n; d++) {
                for (int row=0; row<n; row++) {
                    if (row + d < n)
                        sum[row][row+d] = sum[row][row+d-1] + nums[row+d];
                }
            }

            //System.out.println(Arrays.deepToString(sum));
        }

        public int sumRange(int i, int j) {
            return sum[i][j];
        }
    }

But I got TLE for the very large Test Case.

::

    Submission Result: Time Limit Exceeded


Well, well, well. In this implementation the constructor call will take O(n \ :superscript:`2`) time.

We can actually obtain the range sum given the prefix sum

::

    rangeSum(b, a) = prefixSum(b) - prefixSum(a-1)

Filling out the ``prefixsum`` array will only take O(n) time.

Just be very careful that when ``a`` is 0, don't access ``prefixSum(a-1)``


