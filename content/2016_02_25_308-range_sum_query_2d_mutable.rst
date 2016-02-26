308-range_sum_query_2d_mutable
##############################

:date: 2016-2-25 9:13
:tags: Query Sum, Segment Tree
:category: LeetCode
:slug: 308-range_sum_query_2d_mutable

`LeetCode Problem Link <https://leetcode.com/problems/range-sum-query-2d-mutable/>`_

``m`` rows and ``n`` columns.

Use 2d array ``rowSums`` to store the prefix sums for each row.

When update occurs, a row in ``rowSums`` has to be updated. O(n) time.

When query occurs, sum over at most ``m`` rows. O(m) time.

.. code-block:: java

    private int[][] rowSums;
    private int[][] matrix;

    public NumMatrix(int[][] matrix) {
         this.matrix = matrix;

         int m = matrix.length;

         if (m==0)
             return;

         int n = matrix[0].length;

         rowSums = new int[m][n];

         for(int row=0; row<m; row++){
            for(int col=0; col<n; col++){
                if(col==0)
                    rowSums[row][col] = matrix[row][col];
                else
                    rowSums[row][col] = rowSums[row][col - 1] + matrix[row][col];
            }
         }
    }

    // time complexity for the worst case scenario: O(n)
    public void update(int row, int col, int val) {
        int n = matrix[0].length;

        for(int i = col; i < n; i++){
            rowSums[row][i] = rowSums[row][i] - matrix[row][col] + val;
        }

        matrix[row][col] = val;
    }

    // time complexity for the worst case scenario: O(m)
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int ret = 0;

        for (int j = row1; j <= row2; j++){
            if (col1 == 0)
                ret += rowSums[j][col2];
            else
                ret += rowSums[j][col2] - rowSums[j][col1 - 1];
        }

        return ret;
    }


