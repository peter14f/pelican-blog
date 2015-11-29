119-pscals_triangle_ii
######################

:date: 2015-11-29 23:23
:tags:
:category: LeetCode
:slug: 119-pscals_triangle_ii

`LeetCode Problem Link <https://leetcode.com/problems/pascals-triangle/>`_

.. code-block:: java
    public List<Integer> getRow(int rowIndex) {

        List<Integer> prevRow = new ArrayList<Integer>();
        prevRow.add(1);

        if (rowIndex == 0) {
            return prevRow;
        }

        List<Integer> tmp = new ArrayList<Integer>();

        for (int row=1; row <= rowIndex; row++) {
            tmp.clear();

            for (int j=0; j<=row; j++) {
                if (j==0 || j==row) {
                    tmp.add(1);
                }
                else {
                    tmp.add(prevRow.get(j) + prevRow.get(j-1));
                }
            }

            if (row==rowIndex)
                return tmp;

            List<Integer> p = prevRow;
            prevRow = tmp;
            tmp = p;
        }

        return prevRow;
    }
