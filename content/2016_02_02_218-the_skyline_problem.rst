218-the_skyline_problem
#######################

:date: 2016-2-1 15:50
:tags: Checking Inteverval Overlaps
:category: LeetCode
:slug: 218-the_skyline_problem

`LeetCode Problem Link <https://leetcode.com/problems/the-skyline-problem/>`_

If we're seeing an increase in height, the head of the rectangle should be stored in ``skyline``.
If we're seeing a decrease in height, the tail of the rectangle should be stored in ``skyline``.

Let ``n`` be the number of total buildings.

*Dumb Solution # 1*

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

*Dumb Solution #2*

How many critical points are there given that there are ``n`` rectangles? There are ``2n`` critical points!
Each rectangle has two critical points, its left edge and its right edge.

So instead allocating an int array of size ``nm``, we can just allocate an int array of size ``2n``.

But what is the height at each of these critical points? We need two nested for loops to figure this out.
Basically for each critical point ``c`` in rectangle ``i``, we must check if it's between the two
edges of all other rectangles.

This will take O(n\ :superscript:`2`) time.

*Solution #3*

We sort the edges using a custom comparator. And the use a max heap whose key is the height.

.. code-block:: java

    class Edge {
        int x;
        int h;
        boolean isLeft;

        public Edge(int x, int y, boolean left) {
            this.x = x;
            this.h = y;
            this.isLeft = left;
        }
    }

    class EdgeComparator implements Comparator<Edge> {

        @Override
        public int compare(Edge o1, Edge o2) {
            if (o1.x != o2.x) {
                return o1.x - o2.x;
            }
            else {
                if (o1.isLeft && !o2.isLeft)
                    return -1;
                else if (!o1.isLeft && o2.isLeft)
                    return 1;
                else {
                    if (o1.isLeft)
                        return o2.h - o1.h;
                    else
                        return o1.h - o2.h;
                }
            }
        }
    }

    public List<int[]> getSkyline(int[][] buildings) {
        List<int[]> skyline = new ArrayList<int[]>();

        if (buildings.length == 0)
            return skyline;

        List<Edge> edges = new ArrayList<Edge>();

        for (int i=0; i<buildings.length; i++) {
            Edge eLeft = new Edge(buildings[i][0], buildings[i][2], true);
            Edge eRight = new Edge(buildings[i][1], buildings[i][2], false);

            edges.add(eLeft);
            edges.add(eRight);
        }

        Collections.sort(edges, new EdgeComparator());

        // we need a max heap
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());

        for (int i=0; i<edges.size(); i++) {
            Edge e = edges.get(i);

            if (e.isLeft) {

                if (pq.isEmpty() || e.h > pq.peek()) {
                    int[] d = {e.x, e.h};
                    skyline.add(d);
                }

                pq.offer(e.h);
            }
            else {
                pq.remove(e.h);

                if (pq.isEmpty()) {
                    int[] d = {e.x, 0};
                    skyline.add(d);
                }
                else if (e.h > pq.peek()) {
                    int[] d = {e.x, pq.peek()};
                    skyline.add(d);
                }
            }
        }

        return skyline;
    }

