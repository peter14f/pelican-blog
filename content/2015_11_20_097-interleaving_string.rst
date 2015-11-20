097-interleaving_string
#######################

:date: 2015-11-20 23:19
:tags: Dynamic Programming
:category: LeetCode
:slug: 097-interleaving_string

`LeetCode Problem Link <https://leetcode.com/problems/interleaving-string/>`_

Let ``interleave`` be a 2D boolean array that have ``m+1`` rows and ``n+1`` columns where ``m`` is the length of input
String ``s1`` and ``n`` is the length of input string ``s2``. interleave[i][j] is true iff the first ``i+j``
characters of  ``s3`` is an interleave of the first ``i`` characters of ``s1`` and the first ``j`` characters of ``s2``.

.. code-block:: java

    public boolean isInterleave(String s1, String s2, String s3) {

        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();
        char[] arr3 = s3.toCharArray();

        if (arr1.length + arr2.length != arr3.length)
            return false;

        if (arr1.length == 0)
            return s2.equals(s3);

        if (arr2.length == 0)
            return s1.equals(s3);

        boolean[][] interleave = new boolean[arr1.length + 1][arr2.length + 1];

        // empty s3
        interleave[0][0] = true;

        // first row: first col characters of s2 matches with first col characters of s3?
        for (int col=1; col<=arr2.length; col++) {
            if (interleave[0][col-1] && arr2[col-1] == arr3[col-1]) {
                interleave[0][col] = true;
            }
        }

        // first column: first row characters of s1 matches with first row characters of s3?
        for (int row=1; row<=arr1.length; row++) {
            if (interleave[row-1][0] && arr1[row-1] == arr3[row-1]) {
                interleave[row][0] = true;
            }
        }

        // s3[row+col]
        for (int row=1; row<=arr1.length; row++) {
            for (int col=1; col<=arr2.length; col++) {
                if (interleave[row-1][col] && arr1[row-1] == arr3[col+row-1]) {
                    interleave[row][col] = true;
                }

                if (!interleave[row][col] &&
                        interleave[row][col-1] && arr2[col-1] == arr3[col+row-1]) {
                    interleave[row][col] = true;
                }
            }
        }

        return interleave[arr1.length][arr2.length];
    }
