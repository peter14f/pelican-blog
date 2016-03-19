338-counting_bits
#################

:date: 2016-3-17 10:49
:tags: Memoization
:category: LeetCode
:slug: 338-counting_bits

`LeetCode Problem Link <https://leetcode.com/problems/counting-bits/>`_

Read the first two hints and was able to solve this problem.

::

    int[] bitCount = new int[num+1]

``bitCount`` is the output array.

Fill in ``bitCount[0]`` and ``bitCount[1]`` first.

let the ``msb`` be 2 first. How many numbers have the 2nd bit set?
Two numbers - 2 and 3.

Then we left shift ``msb``, ``msb`` is now 4. How many numbers have the 3rd bit set?
Four numbers - 4, 5, 6, 7.

Then we left shift ``msb``, ``msb`` is now 8. How many numbers have the 4th bit set?
Eight numbers - 8, 9, 10, 11, 12, 13, 14, 15

Note that the number of numbers have bit ``msb`` set is precisely ``msb``.

.. code-block:: java

    public int[] countBits(int num) {

        int[] bitCount = new int[num+1];

        if (num==0)
            return bitCount;

        bitCount[1] = 1;

        if (num==1)
            return bitCount;

        int i = 2;
        int msb = 2;
        int count = msb;

        while (i <= num) {
            if (count > 0) {
                // prevI is i with msb cleared
                int prevI = i & (msb-1);
                bitCount[i] = 1 + bitCount[prevI];
                count--;

                i++;
            }
            else {
                msb = msb << 1;
                count = msb;
            }
        }

        return bitCount;
    }

The time complexity is O(n). The space complexity is O(n) as well. But the output array needs to be allocated anyways.
