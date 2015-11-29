118-pascals_triangle
####################

:date: 2015-11-29 18:22
:tags:
:category: LeetCode
:slug: 118-pascals_triangle

`LeetCode Problem Link <https://leetcode.com/problems/pascals-triangle/>`_

.. code-block:: java

    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> rows = new ArrayList<List<Integer>>();

        List<Integer> curList = new ArrayList<Integer>();
        curList.add(1);

        if (numRows < 1)
            return rows;

        rows.add(new ArrayList<Integer>(curList));

        if (numRows < 2)
            return rows;

        curList.add(1);
        rows.add(new ArrayList<Integer>(curList));

        for (int i=2; i<numRows; i++) {
            List<Integer> prev = rows.get(i-1);
            curList.clear();

            for (int j=0; j<=i; j++) {
                if (j==0 || j==i)
                    curList.add(1);
                else
                    curList.add(prev.get(j) + prev.get(j-1));
            }

            rows.add(new ArrayList<Integer>(curList));
        }


        return rows;
    }
