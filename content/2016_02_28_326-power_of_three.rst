326-power_of_three
##################

:date: 2016-2-28 8:30
:tags: Power
:category: LeetCode
:slug: 326-power_of_three

`LeetCode Problem Link <https://leetcode.com/problems/power-of-three/>`_

Power of 3

| 3 :superscript:`0` = 1
| 3 :superscript:`1` = 3
| 3 :superscript:`2` = 9
| 3 :superscript:`3` = 27
| 3 :superscript:`4` = 81
| 3 :superscript:`5` = 243

.. code-block:: java

    public boolean isPowerOfThree(int n) {
        if (n<1)
            return false;

        while (n % 3 == 0) {
            n = n / 3;
        }
        return n==1;
    }

And then the followup asks if we could do this without using a loop or recursion.

Well, let's write out the math

::

    3 ^ x = n
    log10(x) / log10 (3) = n


This is probably from my high school precalc class

.. code-block:: java

    public boolean isPowerOfThree(int n) {
        if (n < 1)
            return false;

        int x = (int) (Math.log10(n) / Math.log10(3));

        return (Math.pow(3, x) == n);
    }

