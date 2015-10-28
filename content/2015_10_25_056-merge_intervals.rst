056-merge_intervals
###################

:date: 2015-10-25 22:40
:tags:  Custom Comparators
:category: LeetCode
:slug: 056-merge_intervals

`LeetCode Problem Link <https://leetcode.com/problems/merge-intervals/>`_

We need to write our own Comparator class for Intervals. If the start is smaller, the Interval is considered smaller.
If the start is the same, then if the end is smaller, the Interval is considered smaller.

We sort the input list of Interval. And the merging becomes easy.

.. code-block:: java

    class IntervalComp implements Comparator<Interval> {

        @Override
        public int compare(Interval o1, Interval o2) {

            if (o1.start < o2.start) {
                return -1;
            }
            else if (o1.start > o2.start) {
                return 1;
            }
            else {
                if (o1.end < o2.end)
                    return -1;
                else if (o1.end > o2.end)
                    return 1;
                else
                    return 0;
            }
        }

    }

    public List<Interval> merge(List<Interval> intervals) {
        Collections.sort(intervals, new IntervalComp());

        List<Interval> ans = new ArrayList<Interval>();
        Interval top = null;
        for (int i=0; i<intervals.size(); i++) {
            Interval cur = intervals.get(i);

            if (top==null) {
                ans.add(cur);
                top = cur;
            }
            else {
                if (top.end >= cur.start) {
                    top.end = Math.max(top.end, cur.end);
                }
                else {
                    // cannot be merged
                    ans.add(cur);
                    top = cur;
                }
            }
        }

        return ans;
    }