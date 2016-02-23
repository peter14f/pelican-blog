296-best_meeting_point
######################

:date: 2016-2-23 0:53
:tags: 2D Grid, Shorting Distance From Points
:category: LeetCode
:slug: 296-best_meeting_point

`LeetCode Problem Link <https://leetcode.com/problems/best-meeting-point/>`_

Let's first consider the 1 dimensional case. Say we have 3 points at 1, 2, and 4.

In the beginning, I thought the choice would be ``min + (min + max) / 2``. But this turns out to be wrong.

If we choose ``3.5`` to be the meeting point, 1 has to go 2.5, 2 has to go 0.5 and 4 has to go 1.5.

Notice that path for 1 and path for 2 will overlap. To get the minimum distance traveled, we must avoid
overlaps. And picking the middle starting point in the sorted list will achieve this.

.. code-block:: java

    public int minTotalDistance(int[][] grid) {

        int m = grid.length;

        if (m==0)
            return 0;

        int n = grid[0].length;

        List<Integer> rowIndex = new ArrayList<Integer>();
        List<Integer> colIndex = new ArrayList<Integer>();

        for (int row=0; row<m; row++) {
            for (int col=0; col<n; col++) {
                if (grid[row][col] == 1) {
                    rowIndex.add(row);
                    colIndex.add(col);
                }
            }
        }

        // note the rowIndex is already sorted
        Collections.sort(colIndex);

        int xMid = colIndex.get(colIndex.size()/2);
        int yMid = rowIndex.get(rowIndex.size()/2);

        int sum = 0;

        for (int row=0; row<m; row++) {
            for (int col=0; col<n; col++) {
                if (grid[row][col] == 1) {
                    sum += Math.abs(row - yMid);
                    sum += Math.abs(col - xMid);
                }
            }
        }

        return sum;
    }
