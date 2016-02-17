240-search_a_2d_matrix_ii
#########################

:date: 2016-2-16 21:58
:tags: 2D Matrix
:category: LeetCode
:slug: 240-search_a_2d_matrix_ii

`LeetCode Problem Link <https://leetcode.com/problems/search-a-2d-matrix-ii/>`_

Let ``m`` be the number of rows and ``n`` be the number of columns.

Solution 1: O(n+m) time

I'm starting at the lower-left corner, but this should work if you start at the upper-right corner as well.
In the worst case, the element is not in the matrix and you have to walk to the opposite corner to find that out.
So  a total of ``(n + m)`` steps need to be taken.

.. code-block:: java

    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0)
            return false;

        int m = matrix.length;
        int n = matrix[0].length;

        int row = m-1;
        int col = 0;

        while (true) {
            if (row < 0)
                break;
            if (col >= n)
                break;

            int num = matrix[row][col];
            if (num == target) {
                return true;
            }
            else if (num < target) {
                // too small
                col++;
            }
            else {
                // too big
                row--;
            }
        }

        return false;
    }

There is also the divide-and-conquer approach. You break the matrix into 4 parts: upper-left, upper-right,
lower-left, and lower-right. At the first few attempts, I keep getting stack overflows due to never ending
recursive calls. I suggest drawing out the rectangles and labeling each rectangles not thrown away as
A, B, and C.

The recurrence relation is ``T(nm) = 3T(nm/4) + c``. Since we are throwing away a quarter of the input at a time,
the time complexity is not quite O(log (nm)).

.. code-block:: java

    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0)
            return false;

        int m = matrix.length;
        int n = matrix[0].length;

        return search(matrix, 0, m-1, 0, n-1, target);
    }

    private boolean search(int[][] matrix, int beginRow, int endRow,
                           int beginCol, int endCol, int target) {

        if (beginRow > endRow || beginCol > endCol)
            return false;

        int row = beginRow + (endRow - beginRow) / 2;
        int col = beginCol + (endCol - beginCol) / 2;

        if (matrix[row][col] == target) {
            return true;
        }
        else if (matrix[row][col] > target) {
            // too big
            return search(matrix, beginRow, row-1, col, endCol, target) ||
                    search(matrix, beginRow, row-1, beginCol, col-1, target) ||
                    search(matrix, row, endRow, beginCol, col-1, target);
        }
        else {
            // too small
            return search(matrix, beginRow, row, col+1, endCol, target) ||
                    search(matrix, row+1, endRow, col+1, endCol, target) ||
                    search(matrix, row+1, endRow, beginCol, col, target);
        }
    }


