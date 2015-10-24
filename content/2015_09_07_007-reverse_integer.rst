007-reverse_integer
###################

:date: 2015-9-7 17:09
:tags:
:category: LeetCode
:slug: 007-reverse_integer


`LeetCode Problem Link <https://leetcode.com/problems/reverse-integer/>`_

Get each digit of the input number ``x`` from right to left.
Let ``ans`` store the revered result. Each time we get a new digit, we shift ``ans``
to the right by 1 digit and then add that digit to ``ans``. Finally make sure that ``ans``
has the same sign as ``x``.

We also need to take care of overflowing. OJ wants us to return ``0`` if the reversed
number is overflowed.

.. code-block:: java

    public int reverse(int x) {

        int ans = 0;

        boolean negative = false;

        if (x < 0) {
            negative = true;
            x = Math.abs(x);
        }

        do {
            int num = x % 10;
            int multiply = ans*10; // + num;

            if (ans != 0 && multiply/10 != ans) {
                return 0;
            }

            int new_ans = multiply + num;

            if (new_ans < ans) {
                return 0;
            }

            ans = new_ans;

            x = x / 10;
        } while (x > 0);

        if (negative) {
            ans = -ans;
        }

        return ans;
    }

