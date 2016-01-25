201-bitwise_and_of_numbers_range
################################

:date: 2016-1-25 13:59
:tags: AND, ANDing Consecutive Numbers
:category: LeetCode
:slug: 201-bitwise_and_of_numbers_range

`LeetCode Problem Link <https://leetcode.com/problems/bitwise-and-of-numbers-range/>`_

The straightforward linear time approach will give you TLE. Here is a very clever solution based on the observation
that ANDing consecutive non-negative integers will wipe out the lower bits and keep only the bits that are set both in
``m`` and ``n``.

.. code-block:: java

    public int rangeBitwiseAnd(int m, int n) {
        int cnt = 0;

        while (m != n) {
            m = m >> 1;
            n = n >> 1;
            cnt++;
        }

        return (m <<cnt);
    }

