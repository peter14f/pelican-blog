073-set_matrix_zeroes
#####################

:date: 2015-11-4 22:15
:tags:
:category: LeetCode
:slug: 073-set_matrix_zeroes

`LeetCode Problem Link <https://leetcode.com/problems/set-matrix-zeroes/>`_

The first solution that I came up with requires using two sets. As we traverse the elements in the matrix. We store
the row and the column of the element that is zero. We can later zero out these rows and columns. There are at most
``m`` rows and at most ``n`` columns. So the space complexity is O(m+n).

.. code-block:: java

    public void setZeroes(int[][] matrix) {

        int m = matrix.length;

        if (m<1) {
            return;
        }

        int n = matrix[0].length;
        HashSet<Integer> resetRows = new HashSet<Integer>();
        HashSet<Integer> resetColumns = new HashSet<Integer>();

        for (int row=0; row<m; row++) {
            for (int col=0; col<n; col++) {
                if (matrix[row][col] == 0) {
                    if (!resetRows.contains(row))
                        resetRows.add(row);
                    if (!resetColumns.contains(col))
                        resetColumns.add(col);
                }
            }
        }

        for (int row: resetRows) {
            for (int col=0; col<n; col++) {
                matrix[row][col] = 0;
            }
        }

        for (int col: resetColumns) {
            for (int row=0; row<m; row++) {
                matrix[row][col] = 0;
            }
        }
    }


The hint given says there is a constant space solution though... The solution I came up with is to make use of the
first row and the first column for bookkeeping purpose. We first traverse all elements not in the first row and not in
the first column. If the element is zero then the mark that row ``r`` by setting ``matrix[r][0]`` to zero and mark that
column ``c`` by setting ``matrix[0][c]`` to zero.

After the traversal, we examine which rows and which columns need to be zeroed out.

The only catcha is that we also need to keep track if there was originally any zero in the first row and first column.

This way, we're not using any extra space to solve this problem.


.. code-block:: java

    public void setZeroes(int[][] matrix) {

        int m = matrix.length;

        if (m<1) {
            return;
        }
        int n = matrix[0].length;

        boolean zeroOutFirstRow = false;
        for (int col=0; col<n; col++) {
            if (matrix[0][col]==0) {
                zeroOutFirstRow = true;
                break;
            }
        }

        boolean zeroOutFirstCol = false;
        for (int row=0; row<m; row++) {
            if (matrix[row][0] == 0) {
                zeroOutFirstCol = true;
                break;
            }
        }

        for (int row=1; row<m; row++) {
            for (int col=1; col<n; col++) {
                if (matrix[row][col] == 0) {
                    matrix[row][0] = 0;
                    matrix[0][col] = 0;
                }
            }
        }

        // check first row
        for (int col=1; col<n; col++) {
            if (matrix[0][col] == 0) {
                // zero out the column
                for (int row=1; row<m; row++) {
                    matrix[row][col] = 0;
                }
            }
        }

        // check first column
        for (int row=1; row<m; row++) {
            if (matrix[row][0] == 0) {
                // zero out the row
                for (int col=1; col<n; col++) {
                    matrix[row][col] = 0;
                }
            }
        }

        if (zeroOutFirstCol) {
            for (int row=0; row<m; row++) {
                matrix[row][0] = 0;
            }
        }

        if (zeroOutFirstRow) {
            for (int col=0; col<n; col++) {
                matrix[0][col] = 0;
            }
        }
    }