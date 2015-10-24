029-divide_two_integers
#######################

:date: 2015-09-27 10:41
:tags: Division, More Practice, Math
:category: LeetCode
:slug: 029-divide_two_integers

`LeetCode Problem Link <https://leetcode.com/problems/divide-two-integers/>`_

My first thought was to use subtraction. But this will be too slow for OJ.


The trick is use shifting. But we are not only dividing by two.


Find the largest power of 2 that the divisor can mulitply with without exceeding the dividend.
One quick example: dividend is 100 and divisor is 20. 4 is the largest power of 2 that the divisor can multiply with
without exceeding the dividend. 20 * 4 is 80 which is still less than the dividend.

We add 4 to the quotient. And the process can be continued with the 80 being subtracted from the dividend.
This time the largest power of two that the divisor can multiply with without exceeding the current dividend is
1 (2\ :superscript:`0` = 1). We then add 1 to the quotient. Subtracting 20 from the current dividend give us 0.
The loop stops here because the current dividend is 0 which is no longer bigger than the divisor.

A word on overflow. -2147483648 / -1 is the test case when overflow occurs.

We use long because the absolute value or the negative of -2147483648 is still -2147483648.

.. code-block:: java

    public int divide(int dividend, int divisor) {

        if (divisor == 0)
            throw new IllegalArgumentException("cannot divide by zero");
        if (dividend == 0)
            return 0;
        if (divisor == 1)
            return dividend;

        boolean negative = false;
        boolean overflow = false;
        long dividendL = dividend;
        long divisorL = divisor;

        if (dividend < 0 && divisor > 0) {
            negative = true;
            dividendL = -dividendL;
        }
        else if (divisor < 0 && dividend > 0) {
            negative = true;
            divisorL = -divisorL;
        }
        else if (divisor < 0 && dividend < 0) {
            dividendL = -dividendL;
            divisorL = -divisorL;
        }

        int quotient = 0;
        long div = divisorL;

        while (dividendL >= div) {
            int mult = 1;

            if (dividendL > div) {
                while (dividendL > div) {
                    div = div << 1;
                    mult = mult << 1;
                }

                mult = mult >> 1;
                div = div >> 1;
            }

            quotient += mult;

            if (quotient==0)
                overflow = true;

            dividendL = dividendL - div;
            div = divisorL;
        }

        if (negative) {
            if (overflow)
                return Integer.MIN_VALUE;
            return -quotient;
        }else {
            if (overflow)
                return Integer.MAX_VALUE;
            return quotient;
        }
    }







