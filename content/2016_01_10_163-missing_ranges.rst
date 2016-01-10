163-missing_ranges
##################

:date: 2016-1-10 9:12
:tags:
:category: LeetCode
:slug: 163-missing_ranges

`LeetCode Problem Link <https://leetcode.com/problems/find-peak-element/>`_

This takes O(n) time.

.. code-block:: java

    public List<String> findMissingRanges(int[] nums, int lower, int upper) {

        int l = lower;
        List<String> ranges = new ArrayList<String>();

        for (int i=0; i<nums.length; i++) {
            if (nums[i] == l) {
                l++;
            }
            else if (nums[i] > l) {
                insertRanges(l, Math.min(nums[i], upper)-1, ranges);
                l = nums[i]+1;
            }
        }

        if (l <= upper)
            insertRanges(l, upper, ranges);

        return ranges;
    }

    private void insertRanges(int a, int b, List<String> ranges) {
        StringBuffer sb = new StringBuffer();

        sb.append(a);

        if (a < b) {
            sb.append("->");
            sb.append(b);
        }

        ranges.add(sb.toString());
    }


