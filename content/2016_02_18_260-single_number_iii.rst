260-single_number_iii
#####################

:date: 2016-2-18 20:43
:tags: Single Number, Bit Manipulation
:category: LeetCode
:slug: 260-single_number_iii

`LeetCode Problem Link <https://leetcode.com/problems/add-digits/>`_

If we use a HashMap<Integer, Integer> to keep track the occurrence of each element, we can do this problem in
one pass. But we're asked to solve this using O(1) space.

If we just XOR all the elements in the array, we will get ``a ^ b``. How can we extract ``a`` and ``b`` from
``a ^ b``?

``x = a ^ b``

Well, we know that ``a`` and ``b`` are two numbers, so some bit in ``x`` must be set.

Let find that bit, call it bit ``k``.

And then we can put the numbers in the input array into two different groups. Group 1 has all numbers whose bit ``k``
is set. Group 2 has all number whose bit ``k`` is not set.

XORing all numbers in group 1 will give us ``a``.
XORing all numbers in group 2 will give us ``b``.

.. code-block:: java

    public int[] singleNumber(int[] nums) {
        int x = 0;

        for (int i=0; i<nums.length; i++) {
            x = x ^ nums[i];
        }

        /*  x = a ^ b
         *
         *  a and b are different numbers so x must have some bit that's set
         */

        int mask = 1;
        while ((x & mask) == 0) {
            mask = mask << 1;
        }

        // mask now contains the bit where a and b are different

        int a = 0; // the number whose kth bit is not set
        int b = 0; // the number whose kth bit is set

        // find the first number in the array whose bit k is not set
        for (int i=0; i<nums.length; i++) {
            if ((nums[i] & mask) == 0) {
                a = a ^ nums[i];
            }
            else {
                b = b ^ nums[i];
            }
        }

        int[] ans = {a, b};
        return ans;
    }
