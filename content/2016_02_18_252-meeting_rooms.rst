252-meeting_rooms
#################

:date: 2016-2-18 0:24
:tags: Checking Interval Overlaps
:category: LeetCode
:slug: 252-meeting_rooms

`LeetCode Problem Link <https://leetcode.com/problems/meeting-rooms/>`_

Reminds me of 218-the_skyline_problem because we need to check if intervals overlap at any location.

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


