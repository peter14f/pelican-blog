172-factorial_trailing_zeroes
#############################

:date: 2016-1-17 15:53
:tags:
:category: LeetCode
:slug: 172-factorial_trailing_zeroes

`LeetCode Problem Link <https://leetcode.com/problems/factorial-trailing-zeroes/>`_

Use prime factorization. 2 x 5 = 10 so we can count how many factors of 5 are in ``n!``.
How many 5s are there in the prime factorization of ``20!`` ?
45 / 5 = 9 -> There are 4 5s in the prime factorization of 20!.
So there are 4 trailing zeros in 20!.

Since the there will be way more 2s in the prime factorization of any factorial, counting
the number of 5s will be enough.

How many trailing zeroes are there in ``25!`` ?

25 / 5 = 5
25 / 25 = 1

So not only do we need to count the number of 5s in the prime factorization, we also need to
count the number of 25s, 125s, ... in the prime factorization.

The factor we are looking may overflow.

.. code-block:: java

    public int trailingZeroes(int n) {
        int sum = 0;

        long num = n;
        long d = 5;

        while (true) {
            long m = num / d;

            if (m < 1)
                break;

            sum += m;
            d = d * 5;
        }

        return sum;
    }
