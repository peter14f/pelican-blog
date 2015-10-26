059-spiral_matrix_ii
####################

:date: 2015-10-26 17:48
:tags: 2D Array
:category: LeetCode
:slug: 059-spiral_matrix_ii

`LeetCode Problem Link <https://leetcode.com/problems/spiral-matrix-ii/>`_

This problem is very similar to 054-spiral_matrix. We use the variable ``direction`` to keep track of the current
direction and it can take 4 values: ``RIGHT``, ``DOWN``, ``LEFT``, and ``UP``.

.. code-block:: java

    public static final int RIGHT = 0;
    public static final int DOWN = 1;
    public static final int LEFT = 2;
    public static final int UP = 3;

    public int[][] generateMatrix(int n) {

        int[][] matrix = new int[n][n];

        int i=1;
        int total = n*n;
        int direction = RIGHT;
        int wall = 0;
        int row = 0;
        int col = 0;

        while (i<=total) {
            matrix[row][col] = i;

            switch (direction) {
                case RIGHT:
                    if (col == n - 1 - wall) {
                        direction = DOWN;
                        row++;
                    }
                    else {
                        col++;
                    }
                    break;
                case DOWN:
                    if (row == n - 1 - wall) {
                        direction = LEFT;
                        col--;
                    }
                    else {
                        row++;
                    }
                    break;
                case LEFT:
                    if (col == wall) {
                        direction = UP;
                        wall++;
                        row--;
                    }
                    else {
                        col--;
                    }
                    break;
                case UP:
                    if (row == wall) {
                        direction = RIGHT;
                        col++;
                    }
                    else {
                        row--;
                    }
                    break;
            }
            i++;
        }

        return matrix;
    }
