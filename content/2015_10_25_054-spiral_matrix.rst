054-spiral_matrix
#################

:date: 2015-10-25 16:08
:tags: 2D Array
:category: LeetCode
:slug: 054-spiral_matrix

`LeetCode Problem Link <https://leetcode.com/problems/spiral-matrix/>`_

I use the variable ``direction`` to keep track the direction we are going right now. Another variable needed is
``wall``.

.. code-block:: java

    public class Solution {

        public static final int RIGHT = 0;
        public static final int DOWN = 1;
        public static final int LEFT = 2;
        public static final int UP = 3;

        public List<Integer> spiralOrder(int[][] matrix) {

            List<Integer> ans = new ArrayList<Integer>();

            if (matrix==null || matrix.length == 0)
                return ans;

            int m = matrix.length;
            int n = matrix[0].length;
            int cnt = m*n;

            int row=0;
            int col=0;
            int wall=0;
            int direction = RIGHT;

            while (ans.size() < cnt) {
                ans.add(matrix[row][col]);

                switch (direction) {
                    case RIGHT:
                        if (col == n-1-wall) {
                            direction = DOWN;
                            row++;
                        }
                        else {
                            col++;
                        }
                        break;
                    case DOWN:
                        if (row == m-1-wall) {
                            direction = LEFT;
                            col--;
                        }
                        else {
                            row++;
                        }
                        break;
                    case LEFT:
                        if (col==wall) {
                            direction = UP;
                            row--;
                            wall++;
                        }
                        else {
                            col--;
                        }
                        break;
                    case UP:
                        if (row==wall) {
                            direction = RIGHT;
                            col++;
                        }
                        else {
                            row--;
                        }
                        break;
                }
            }

            return ans;
        }
    }
