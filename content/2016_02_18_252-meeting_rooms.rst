252-meeting_rooms
#################

:date: 2016-2-18 0:24
:tags: Checking Interval Overlaps, Custom Comparators
:category: LeetCode
:slug: 252-meeting_rooms

`LeetCode Problem Link <https://leetcode.com/problems/meeting-rooms/>`_

**056-merge_intervals**
**057-insert_intervals**

Reminds me of **218-the_skyline_problem** because we need to check if intervals overlap at any location.

As discussed in that blog post, the most straightforward way to check for interval overlaps is to use
two nested for loops which takes O(n\ :superscript:`2`) time.

If an overlap is found we can immediately return ``false`` as we are sure that it's impossible to attend
all the meetings. Note that if two meetings start at the same time, it is also impossible to attend both meetings.

.. code-block:: java

    public boolean canAttendMeetings(Interval[] intervals) {

        for (int i=0; i<intervals.length; i++) {

            for (int j=0; j<intervals.length; j++) {
                if (i==j)
                    continue;

                if (intervals[i].start >= intervals[j].start &&
                        intervals[i].start < intervals[j].end) {
                    return false;
                }
            }

        }

        return true;
    }

We can do better than O(n\ :superscript:`2`) time if we sort the intervals. How do we sort? We sort based on the
start time of each interval.

.. code-block:: java

    class IntervalComparator implements Comparator<Interval> {

        @Override
        public int compare(Interval o1, Interval o2) {
            return o1.start - o2.start;
        }
    }

Once the input array of Intervals is sorted, we only need to compare the ith interval with the (i+1)th interval.
If the ith end is greater than the (i+1)th start, then there is an overlap.

.. code-block:: java

    public boolean canAttendMeetings(Interval[] intervals) {
        Arrays.sort(intervals, new IntervalComparator());

        for (int i=0; i<intervals.length - 1; i++) {
            Interval cur = intervals[i];
            Interval next = intervals[i+1];

            if (cur.end > next.start) {
                return false;
            }
        }

        return true;
    }

This takes O(nlogn) time instead of O(n\ :superscript:`2`) time.