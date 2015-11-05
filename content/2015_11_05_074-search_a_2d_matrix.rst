074-search_a_2d_matrix
######################

:date: 2015-11-5 20:39
:tags: Binary Search
:category: LeetCode
:slug: 074-search_a_2d_matrix

`LeetCode Problem Link <https://leetcode.com/problems/search-a-2d-matrix/>`_

This problem is essentially binary search in disguise. Treat the 2d matrix as if its an 1d array and simply
transform the index in the 1d array to the correct row and column index.

.. code-block:: java

    public boolean searchMatrix(int[][] matrix, int target) {

        int m = matrix.length;

        if (m < 1)
            return false;

        int n = matrix[0].length;

        int low = 0;
        int high = m*n - 1;

        while (low <= high) {
            int middle = low + (high-low)/2;
            int num = getMiddleNum(matrix, m, n, middle);

            if (num==target) {
                return true;
            }
            else if (num < target) {
                // num too small
                low = middle + 1;
            }
            else {
                // num too big
                high = middle - 1;
            }
        }

        return false;
    }

    private int getMiddleNum(int[][] matrix, int m, int n, int middle) {
        int row = middle/n;
        int col = middle%n;

        return matrix[row][col];
    }