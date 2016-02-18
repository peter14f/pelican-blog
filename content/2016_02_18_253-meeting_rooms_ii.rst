253-meeting_rooms_ii
####################

:date: 2016-2-18 0:46
:tags: Checking Interval Overlaps, Detect Maximum Number of Overlaps, Custom Comparator
:category: LeetCode
:slug: 253-meeting_rooms_ii

`LeetCode Problem Link <https://leetcode.com/problems/meeting-rooms-ii/>`_

Again, this is very similar to the problem 218-the_skyline_problem.

The most number of intervals that overlap at any given time is the minimum number of meeting rooms required.

What did we do in 218-the_skyline_problem? We defined an Edge class that has a field that denotes whether
it is the left edge of an interval or the right edge of an interval.

The intervals in this problem does not contain a height like in 218-the_skyline_problem.
But we still need a custom comparator so that we could sort the edges.

In my solution, I use a Stack<Edge> to keep track the current number of overlaps. When we see a start edge, we
push is onto the stack, when we see a end edge, we pop() one start edge from the stack.

The overall time complexity is still O(nlogn). Notice that in the custom comparator, if two edges are at the same
time, the left edge is considered smaller than the right edge. This is make sure that intervals like [1, 2] and [2, 3]
won't be considered overlapping.

.. code-block:: java

    class Edge {
        int time;
        boolean isStart;

        public Edge(int t, boolean start) {
            time = t;
            isStart = start;
        }
    }

    class EdgeComparator implements Comparator<Edge> {

        @Override
        public int compare(Edge o1, Edge o2) {
            if (o1.time < o2.time)
                return -1;
            else if (o1.time > o2.time)
                return 1;
            else {
                if (o1.isStart && !o2.isStart)
                    return 1;
                else if (!o1.isStart && o2.isStart)
                    return -1;
                else
                    return 0;
            }
        }
    }

    public int minMeetingRooms(Interval[] intervals) {
        List<Edge> edges = new ArrayList<Edge>();

        for (int i=0; i<intervals.length; i++) {
            Edge e1 = new Edge(intervals[i].start, true);
            Edge e2 = new Edge(intervals[i].end, false);
            edges.add(e1);
            edges.add(e2);
        }

        Collections.sort(edges, new EdgeComparator());

        int maxRoomNeeded = 0;

        Stack<Edge> rooms = new Stack<Edge>();

        for (int i=0; i<edges.size(); i++) {
            Edge cur = edges.get(i);

            if (cur.isStart) {
                rooms.push(cur);
                if (rooms.size() > maxRoomNeeded)
                    maxRoomNeeded = rooms.size();
            }
            else {
                rooms.pop();
            }
        }

        return maxRoomNeeded;
    }

Found another solution online where we don't have to create a Edge class. Instead, we simply store the start times
in one list and the end times in another. Both lists need to be sorted, and then we use two pointers ``i`` and ``j`` to
traverse the two lists and to decide the number of overlaps. We also don't need a custom comparator in this case since
we are just sorting Integers.

.. code-block:: java

    public int minMeetingRooms(Interval[] intervals) {

        List<Integer> startTimes = new ArrayList<Integer>();
        List<Integer> endTimes = new ArrayList<Integer>();

        for (int i=0; i<intervals.length; i++) {
            startTimes.add(intervals[i].start);
            endTimes.add(intervals[i].end);
        }

        Collections.sort(startTimes);
        Collections.sort(endTimes);

        int i=0;
        int j=0;

        int maxRoomsNeeded = 0;
        int curRoomsNeeded = 0;

        while (i<startTimes.size() && j < endTimes.size()) {
            if (startTimes.get(i) < endTimes.get(j)) {
                curRoomsNeeded++;

                if (curRoomsNeeded > maxRoomsNeeded)
                    maxRoomsNeeded = curRoomsNeeded;

                i++;
            }
            else {
                curRoomsNeeded--;
                j++;
            }
        }

        return maxRoomsNeeded;
    }
