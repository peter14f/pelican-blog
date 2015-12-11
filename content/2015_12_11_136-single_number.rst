136-single_number
#################

:date: 2015-12-11 19:52
:tags: XOR, Bit Manipulation
:category: LeetCode
:slug: 136-single_number

`LeetCode Problem Link <https://leetcode.com/problems/single-number/>`_

a XOR a = 0

.. code-block:: java

    /* asked to do a O(n) time solution that does not use extra space
     * every element appears twice except for one
     */
    public int singleNumber(int[] nums) {

        int single = 0;

        for (int i=0; i<nums.length; i++) {
            single = single ^ nums[i];
        }

        return single;
    }
