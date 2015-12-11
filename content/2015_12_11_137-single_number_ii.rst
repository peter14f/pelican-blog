137-single_number_ii
####################

:date: 2015-12-11 21:01
:tags: Bit Manipulation
:category: LeetCode
:slug: 137-single_number_ii

`LeetCode Problem Link <https://leetcode.com/problems/single-number-ii/>`_

We can use an int array to store the 32 bits.


.. code-block:: java

    public int singleNumber(int[] nums) {
       int[] bits = new int[32];
       int result = 0;

       for (int i=0; i<nums.length; i++) {
           for (int shift=0; shift<32; shift++) {
               bits[shift] += (nums[i] >> shift) & 1;
               if (bits[shift] == 3)
                   bits[shift] = 0;
           }
       }

       for (int shift=0; shift<32; shift++) {
           result = result | (bits[shift] << shift);
       }

       return result;
    }

This solution uses extra memory though. The following the solution that uses 3 int variables. 

.. code-block:: java

    public int singleNumber(int[] nums) {

        int ones = 0, twos = 0, threes = 0;

        for (int i=0; i<nums.length; i++) {
            threes = twos & nums[i]; // bits that have already seen twice,
            twos = twos | (ones & nums[i]); // bits that have already occurred twice | bits that have already occured twice
            ones = ones | nums[i];

            twos = twos & ~threes; // clear bits that have just been seen three times
            ones = ones & ~threes; // clear bits that have just been seen three times
        }

        return ones;
    }
