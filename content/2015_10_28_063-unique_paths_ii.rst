063-unique_paths_ii
###################

:date: 2015-10-28 18:14
:tags: Dynamic Programming, 2D Grid Move Right Move Down, Count Ways
:category: LeetCode
:slug: 063-unique_paths_ii

`LeetCode Problem Link <https://leetcode.com/problems/unique-paths-ii/>`_

The solution is very much like the one to the previous problem. There is however no way to get a cell that is an
obstacle.

.. code-block:: java

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {

        if (obstacleGrid==null | obstacleGrid[0].length < 1) {
            throw new IllegalArgumentException();
        }

        int m = obstacleGrid.length;

        if (m < 1) {
            throw new IllegalArgumentException();
        }

        int n = obstacleGrid[0].length;

        for (int row=0; row<m; row++) {
            for (int col=0; col<n; col++) {
                if (obstacleGrid[row][col] == 1)
                    obstacleGrid[row][col] = -1;
            }
        }

        // first row
        boolean obstacleSeen = false;
        if (obstacleGrid[0][0] == -1)
            obstacleSeen = true;

        for (int col=0; col<n; col++) {
            if (obstacleSeen) {
                // can't get here
                obstacleGrid[0][col] = -1;
            }
            else if (obstacleGrid[0][col] != -1) {
                obstacleGrid[0][col] = 1;
            }
            else {
                obstacleSeen = true;
            }
        }

        obstacleSeen = false;
        if (obstacleGrid[0][0] == -1)
            obstacleSeen = true;

        // first col
        for (int row=0; row<m; row++) {
            if (obstacleSeen) {
                // can't get here
                obstacleGrid[row][0] = -1;
            }
            else if (obstacleGrid[row][0] != -1) {
                obstacleGrid[row][0] = 1;
            }
            else {
                obstacleSeen = true;
            }
        }

        for (int row=1; row<m; row++) {
            for (int col=1; col<n; col++) {

                if (obstacleGrid[row][col]==-1)
                    continue;

                int up = obstacleGrid[row-1][col];
                int left = obstacleGrid[row][col-1];

                if (up==-1)
                    up = 0;
                if (left==-1)
                    left = 0;

                obstacleGrid[row][col] = up+left;
            }
        }

        if (obstacleGrid[m-1][n-1]==-1)
            return 0;
        else
            return obstacleGrid[m-1][n-1];
    }