057-insert_interval
###################

:date: 2015-10-26 12:41
:tags:
:category: LeetCode
:slug: 057-insert_interval

`LeetCode Problem Link <https://leetcode.com/problems/insert-interval/>`_

As shown in the exmaple, the interval being inserted may overlap with multiple intervals.
Or the interval being inserted may NOT overlap with any existing interval in the list.

I use the pointers ``start`` and ``end`` to mark the first and last interval that overlap with the
interval being inserted.

And I wrote a overlaps helper method to determine if two intervals actually overlap.

.. code-block:: java

    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        Interval start = null;
        Interval end = null;
        for (int i=0; i<intervals.size(); i++) {
            Interval cur = intervals.get(i);
            if (overlaps(newInterval, cur)) {
                if (start == null) {
                    start = cur;
                }
                end = cur;
            }
        }

        List<Interval> ans = new ArrayList<Interval>();

        if (start == null) {
            boolean inserted = false;
            for (int i=0; i<intervals.size(); i++) {
                Interval cur = intervals.get(i);
                if (!inserted && cur.start >= newInterval.start) {
                    ans.add(newInterval);
                    inserted = true;
                }
                ans.add(cur);
            }
            if (!inserted) {
                ans.add(newInterval);
            }
        }
        else {
            Interval newStart = null;
            for (int i=0; i<intervals.size(); i++) {
                Interval cur = intervals.get(i);
                if (cur==start) {
                    newStart = new Interval(Math.min(cur.start, newInterval.start),
                                            Math.max(cur.end, newInterval.end));
                    ans.add(newStart);
                }

                if (cur==end) {
                    newStart.end = Math.max(newStart.end, cur.end);
                    newStart = null;
                }
                else if (newStart!=null) {
                    newStart.end = Math.max(newStart.end, cur.end);
                }
                else {
                    ans.add(cur);
                }
            }
        }

        return ans;
    }

    private boolean overlaps(Interval i1, Interval i2) {
        if (i1.start < i2.start) {
            if (i1.end < i2.start)
                return false;
            else
                return true;
        }
        else if (i2.start < i1.start) {
            if (i2.end < i1.start)
                return false;
            else
                return true;
        }
        else {
            return true;
        }
    }
