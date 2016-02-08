228-summary_ranges
##################

:date: 2016-2-8 23:35
:tags:
:category: LeetCode
:slug: 228-summary_ranges

`LeetCode Problem Link <https://leetcode.com/problems/summary-ranges/>`_

.. code-block:: java

    public List<String> summaryRanges(int[] nums) {
        List<String> ans = new ArrayList<String>();

        if (nums.length == 0)
            return ans;

        StringBuffer sb = new StringBuffer();
        int begin = nums[0];
        int prev = begin;
        sb.append(prev);

        for (int i=1; i<nums.length; i++) {
            if (nums[i] > prev + 1) {
                if (prev != begin) {
                    sb.append("->");
                    sb.append(prev);
                    ans.add(sb.toString());
                    sb.setLength(0);
                }
                else {
                    ans.add(sb.toString());
                    sb.setLength(0);
                }
                begin = nums[i];
                prev = begin;
                sb.append(prev);
            }
            else
                prev = nums[i];
        }

        if (sb.length() > 0) {
            if (prev != begin) {
                sb.append("->");
                sb.append(prev);
            }
            ans.add(sb.toString());
        }

        return ans;
    }
