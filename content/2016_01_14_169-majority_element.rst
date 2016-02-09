169-majority_element
####################

:date: 2016-1-14 13:03
:tags: Histograms, Hash Tables, Majority Vote Algorithm
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

Here is a clever majority vote algorithm.

We are looking for the element who appears more than floor(n/2) times. Let's refer to this element as the **majority
element**. This means that the number of times it appears in the array is more than the number of times any other
number appear in the array. Since the problem states that the input array always contains the a majority element.
We can do this in one pass trying to find the element that appear the most number of times. We just need two variables
``c`` and ``count``.

.. code-block:: java

    public int majorityElement(int[] nums) {

        int c = nums[0];
        int count = 1;

        for (int i=1; i<nums.length; i++) {
            if (nums[i] == c) {
                count++;
            }
            else {
                count--;

                if (count == 0) {
                    c = nums[i];
                    count = 1;
                }
            }
        }

        return c;
    }
