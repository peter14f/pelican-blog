329-longest_increasing_path_in_a_matrix
#######################################

:date: 2016-2-28 14:54
:tags: DFS, Graph, Undirected Graph
:category: LeetCode
:slug: 329-longest_increasing_path_in_a_matrix

`LeetCode Problem Link <https://leetcode.com/problems/longest-increasing-path-in-a-matrix/>`_

My first thought is to use DFS.

.. code-block:: java

    public int longestIncreasingPath(int[][] matrix) {

        int[] ans = {0};

        int m = matrix.length;

        if (m == 0)
            return 0;

        int n = matrix[0].length;

        for (int row=0; row<m; row++) {
            for (int col=0; col<n; col++) {
                dfs(matrix, row, col, -1, -1, 1, ans);
            }
        }

        return ans[0];
    }

    private void dfs(int[][] matrix, int row, int col, int prevRow, int prevCol,
                     int curLen, int[] ans) {

        int m = matrix.length;
        int n = matrix[0].length;

        boolean deadEnd = true;

        // up
        if (row-1 >=0 && (prevRow != row-1 || prevCol != col) &&
                matrix[row-1][col] > matrix[row][col]) {

            deadEnd = false;
            dfs(matrix, row-1, col, row, col, curLen+1, ans);
        }

        // down
        if (row+1 < m && (prevRow != row+1 || prevCol != col) &&
                matrix[row+1][col] > matrix[row][col]) {

            if (deadEnd)
                deadEnd = false;
            dfs(matrix, row+1, col, row, col, curLen+1, ans);
        }

        // left
        if (col-1 >= 0 && (prevRow != row || prevCol != col-1) &&
                matrix[row][col-1] > matrix[row][col]) {

            if (deadEnd)
                deadEnd = false;

            dfs(matrix, row, col-1, row, col, curLen+1, ans);
        }


        // right
        if (col+1 < n && (prevRow != row || prevCol != col+1) &&
                matrix[row][col+1] > matrix[row][col]) {

            if (deadEnd)
                deadEnd = false;

            dfs(matrix, row, col+1, row, col, curLen+1, ans);
        }

        if (deadEnd && curLen > ans[0]) {
            ans[0] = curLen;
        }
    }

This got TLE on a large test case.

We could cache the result in cache[i][j].


.. code-block:: java

    public int[][] dirs = {
            {1, 0},  // right
            {0 ,1},  // down
            {-1, 0}, // left
            {0, -1}  // up
    };

    public int longestIncreasingPath(int[][] matrix) {
        int m = matrix.length;

        if (m == 0)
            return 0;

        int n = matrix[0].length;

        int[][] cache = new int[m][n];

        int max = 1;

        for (int row=0; row<m; row++) {
            for (int col=0; col<n; col++) {
                int len = dfs(matrix, row, col, -1, -1, cache);
                max = Math.max(max, len);
            }
        }

        return max;
    }

    private int dfs(int[][] matrix, int row, int col,
                    int prevRow, int prevCol, int[][] cache) {
        int m = matrix.length;
        int n = matrix[0].length;

        if (cache[row][col] > 0)
            return cache[row][col];

        int max = 1;

        for (int[] dir: dirs) {
            int x = col+dir[0];
            int y = row+dir[1];

            if (y < 0 || y >=m || x < 0 || x >= n || matrix[y][x] <= matrix[row][col])
                continue;

            int len = 1 + dfs(matrix, row+dir[1], col+dir[0], row, col, cache);
            max = Math.max(max, len);
        }

        cache[row][col] = max;
        return max;
    }