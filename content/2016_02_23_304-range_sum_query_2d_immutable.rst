304-range_sum_query_2d_immutable
################################

:date: 2016-2-23 22:52
:tags: Range Sum
:category: LeetCode
:slug: 304-range_sum_query_2d_immutable

`LeetCode Problem Link <https://leetcode.com/problems/range-sum-query-2d-immutable/>`_

My original thought is to use the same approach used in 303-range_sum_query. The ``prefixSum`` array just has ``m``
rows instead of just 1.

.. code-block:: java

    public class NumMatrix {
        int[][] prefixSum;

        public NumMatrix(int[][] matrix) {
            int m = matrix.length;

            if (m==0)
                return;

            int n = matrix[0].length;

            prefixSum = new int[m][n];

            for (int row=0; row < m; row++) {
                prefixSum[row][0] = matrix[row][0];

                for (int col = 1; col < n; col++) {
                    prefixSum[row][col] = prefixSum[row][col-1] + matrix[row][col];
                }
            }

            System.out.println(Arrays.deepToString(prefixSum));
            System.out.println(prefixSum);
        }

        public int sumRegion(int row1, int col1,
                             int row2, int col2) {
            System.out.println(prefixSum);

            int sum = 0;


            for (int row=row1; row <= row2; row++) {
                if (col1 == 0)
                    sum += prefixSum[row][col2];
                else {
                    /*
                    System.out.println("col1=" + col1 +
                          " col2=" + col2 + " row1=" + row1 + " row2=" + row2 + " row=" + row);
                    System.out.println(Arrays.toString(prefixSum[row]));
                    */
                    sum += (prefixSum[row][col2] - prefixSum[row][col1-1]);
                }

            }

            return sum;
        }
    }

But I got TLE for the large test case.

::

    Submission Result: Time Limit Exceeded


Here we will make ``prefixSum`` a 2d prefixSum. ``prefixSum[i][j]`` will be the sum over ``j`` columns over ``i`` rows.

How can we fill out this in O(mn) time in the constructor? It will be very useful if you write out the sum in an
example. ``prefixSum`` will be of size ``[m+1][n+1]``.

::

    0     |  0      |   0       |
    0     |a1       |a1+a2      |
    0     |a1+b1    |a1+a2+b1+b2|


``prefixSum[2][2] = prefixSum[1][2] + prefixSum[2][1] - prefixSum[1][1] + matrix[2][2]``

Once the 2d array ``prefixSum`` is filled, we can do ``sumRegions()`` in constant time.

::

    sumRegions(row1, col1, row2, col2) = prefixSum[row2+1][col2+1] -
                                           prefixSum[row2+1][col1] -
                                           prefixSum[row1][col2+1] +
                                           prefixSum[row1][col1]

