149-max_points_on_a_line
########################

:date: 2015-12-28 19:19
:tags:
:category: LeetCode
:slug: 149-max_points_on_a_line

`LeetCode Problem Link <https://leetcode.com/problems/max-points-on-a-line/>`_

The outer loop choose each point as the base point. For each base point, we will keep track how many
duplicated points there are and the number of the slopes that could be formed with other points in the list.

.. code-block:: java

    public int maxPoints(Point[] points) {

        if(points.length == 0||points == null)
            return 0;

        int n = points.length;

        if(n <= 2)
            return n;

        // the final max value, at least 2
        int ans = 2;

        for (int i=0; i<n; i++) {
            HashMap<Double, Integer> map = new HashMap<Double, Integer>();
            Point base = points[i];
            int dupCnt = 0;

            for (int j=0; j<n; j++) {
                if (i==j)
                    continue;

                Point a = points[j];

                if (a.x == base.x && a.y == base.y) {
                    dupCnt++;
                    continue;
                }

                double slope = 0;

                if (a.x == base.x) {
                    slope = Float.MAX_VALUE;
                }
                else {
                    slope = (a.y - base.y);
                    slope = slope / (a.x - base.x);
                }

                if (map.containsKey(slope)) {
                    map.put(slope, map.get(slope)+1);
                }
                else {
                    map.put(slope, 2);
                }
            }

            // base point itself
            // even if all points are duplicates of base, we will get the right ans
            int localMax = 1;

            for (double s: map.keySet()) {
                if (map.get(s) > localMax) {
                    localMax = map.get(s);
                }
            }

            // duplicated points
            localMax += dupCnt;

            if (localMax > ans)
                ans = localMax;
        } // base

        return ans;
    }

O(n\ :superscript:`2`) time is used and O(n) space is used.
