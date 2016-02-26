311-sparse_matrix_multiplication
################################

:date: 2016-2-25 15:06
:tags: Matrix Multiplication
:category: LeetCode
:slug: 311-sparse_matrix_multiplication

`LeetCode Problem Link <https://leetcode.com/problems/sparse-matrix-multiplication/>`_


.. code-block:: java

    public int[][] multiply(int[][] A, int[][] B) {

        int m = A.length;

        if (m==0 || B.length == 0)
            return new int[0][];

        int n = A[0].length;
        int l = B[0].length;

        Map<Integer, Map<Integer, Integer>> denseA = new HashMap<Integer, Map<Integer, Integer>>();

        for (int row=0; row<m; row++) {
            for (int col=0; col<n; col++) {
                if (A[row][col] != 0) {
                    if (!denseA.containsKey(row)) {
                        denseA.put(row, new HashMap<Integer, Integer>());
                    }
                    denseA.get(row).put(col, A[row][col]);
                }
            }
        }

        Map<Integer, Map<Integer, Integer>> denseB = new HashMap<Integer, Map<Integer, Integer>>();

        for (int row=0; row<n; row++) {
            for (int col=0; col<l; col++) {
                if (B[row][col] != 0) {
                    if (!denseB.containsKey(row))
                        denseB.put(row, new HashMap<Integer, Integer>());
                    denseB.get(row).put(col, B[row][col]);
                }
            }
        }

        int[][] C = new int[m][l];

        for (int row: denseA.keySet()) {
            for (int col: denseA.get(row).keySet()) {
                if (!denseB.containsKey(col))
                    continue;

                for (int k: denseB.get(col).keySet()) {
                    C[row][k] += denseA.get(row).get(col) * denseB.get(col).get(k);
                }
            }
        }

        return C;
    }

