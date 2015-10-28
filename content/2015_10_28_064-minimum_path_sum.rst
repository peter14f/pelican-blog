064-minimum_path_sum
####################

:date: 2015-10-28 21:57
:tags: Dynamic Programming, 2D Grid Move Right Move Down
:category: LeetCode
:slug: 064-minimum_path_sum

The the grid contains only non-negative numbers. We can just choose to arrive to the current from top or from left
based on which path produces a smaller sum.

.. code-block:: java

    public int minPathSum(int[][] grid) {

        if (grid==null || grid.length < 1) {
            return 0;
        }

        int m = grid.length;
        int n = grid[0].length;

        int[][] sum = new int[m][n];

        // first row
        sum[0][0] = grid[0][0];
        for (int col=1; col<n; col++) {
            sum[0][col] = sum[0][col-1] + grid[0][col];
        }

        // first col
        for (int row=1; row<m; row++) {
            sum[row][0] = sum[row-1][0] + grid[row][0];
        }

        for (int row=1; row<m; row++) {
            for (int col=1; col<n; col++) {
                int fromTop = grid[row][col] + sum[row-1][col];
                int fromLeft = grid[row][col] + sum[row][col-1];
                sum[row][col] = Math.min(fromTop, fromLeft);
            }
        }

        return sum[m-1][n-1];
    }
