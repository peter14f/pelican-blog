218-the_skyline_problem
#######################

:date: 2016-2-1 15:50
:tags:
:category: LeetCode
:slug: 218-the_skyline_problem

`LeetCode Problem Link <https://leetcode.com/problems/the-skyline-problem/>`_

If we're seeing an increase in height, the head of the rectangle should be stored in ``skyline``.
If we're seeing a decrease in height, the tail of the rectangle should be stored in ``skyline``.

Let ``n`` be the number of total buildings.

The straightforward solution stores all the heights at each x coordinate. This requires two nested for loops.
Assume that ``m`` is the average width of the ``n`` buildings. This would take O(nm) time. Not only is this
not time efficient. This also requires a lot of memory. In the worst case, it can take O(nm) space as well.
This will not pass OJ.

.. code-block:: java

    public List<int[]> getSkyline(int[][] buildings) {

        List<int[]> skyline = new ArrayList<int[]>();

        if (buildings.length==0)
            return skyline;

        int xMin = buildings[0][0];
        int xMax = buildings[buildings.length-1][1];
        int width = xMax - xMin + 1;

        int[] heights = new int[width];

        for (int i=0; i<buildings.length; i++) {
            int h = buildings[i][2];
            for (int j=buildings[i][0]; j<=buildings[i][1]; j++) {
                int x = j - xMin;
                if (h > heights[x]) {
                    heights[x] = h;
                }
            }
        }

        int h = 0;
        int i = 0;
        for (; i<heights.length; i++) {
            if (heights[i] != h) {
                if (heights[i] > h) {
                    // going up, we pick the head
                    int[] d = {xMin + i, heights[i]};
                    skyline.add(d);
                }
                else {
                    // going down, we pick the tail
                    int[] d = {xMin + i - 1, heights[i]};
                    skyline.add(d);
                }

                h = heights[i];
            }
        }

        // going down, we pick the tail
        int[] d = {xMin + i - 1, 0};
        skyline.add(d);

        return skyline;
    }


