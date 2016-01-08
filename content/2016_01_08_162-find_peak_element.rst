162-find_peak_element
#####################

:date: 2016-1-8 23:03
:tags:
:category: LeetCode
:slug: 162-find_peak_element

`LeetCode Problem Link <https://leetcode.com/problems/find-peak-element/>`_

We can do this in O(n) time.

.. code-block:: java

    public int findPeakElement(int[] nums) {
        int peakIndex = -1;

        for (int i=0; i<nums.length; i++) {
            boolean left = false;
            boolean right = false;

            if (i==0 || nums[i] > nums[i-1])
                left = true;

            if (i==nums.length-1 || nums[i] > nums[i+1])
                right = true;

            if (left && right) {
                peakIndex = i;
            }
        }

        return peakIndex;
    }
