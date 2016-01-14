169-majority_element
####################

:date: 2016-1-14 13:03
:tags: Histograms
:category: LeetCode
:slug: 169-majority_element

`LeetCode Problem Link <https://leetcode.com/problems/majority-element/>`_

.. code-block:: java

    public int majorityElement(int[] nums) {
        int threshold = nums.length/2;

        HashMap<Integer, Integer> histogram = new HashMap<Integer, Integer>();

        for (int i=0; i<nums.length; i++) {
            if (histogram.containsKey(nums[i])) {
                histogram.put(nums[i], histogram.get(nums[i])+1);
            }
            else {
                histogram.put(nums[i], 1);
            }

            if (histogram.get(nums[i]) > threshold)
                return nums[i];
        }

        return 0;
    }

This takes O(n) time and O(n) space.
