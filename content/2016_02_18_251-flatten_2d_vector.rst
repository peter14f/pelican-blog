251-flatten_2d_vector
#####################

:date: 2016-2-18 0:18
:tags: Iterator
:category: LeetCode
:slug: 251-flatten_2d_vector

`LeetCode Problem Link <https://leetcode.com/problems/flatten-2d-vector/>`_

Just note that that there could be consecutive empty rows before a non-empty shows up.

.. code-block:: java

    public class Vector2D {
        List<List<Integer>> l;
        int row, col, m;

        public Vector2DB(List<List<Integer>> vec2d) {
            l = vec2d;
            m = l.size();
            row = 0;
            col = 0;
        }

        public int next() {
            int toReturn = l.get(row).get(col);
            col++;
            return toReturn;
        }

        public boolean hasNext() {
            while (row < m) {
                if (col < l.get(row).size())
                    return true;
                col=0;
                row++;
            }

            return false;
        }

