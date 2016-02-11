233-number_of_digit_one
#######################

:date: 2016-2-11 19:36
:tags: Math
:category: LeetCode
:slug: 233-number_of_digit_one

This problem is asking how many 1s are seen in non-negative integer <= ``n``.

Here is the simplest solution that will get you TLE for a large ``n``.

.. code-block:: java

    private int countOnes(int n) {
        int num = 0;

        while (n > 0) {
            if ((n % 10) == 1)
                num++;
            n = n / 10;
        }

        return num;
    }

    public int countDigitOne(int n) {
        int sum = 0;

        while (n > 0) {
            int num = countOnes(n);
            sum += num;
            n--;
        }

        return sum;
    }

In the following solution, I am counting the number of non-negative integers less than or equal to ``n`` that
has a 1 at each digit. We are starting from the least significant (right-most) digit and working our way to the
most significant (left-most) digit.

Consider the number **67294** and let's say we are at the 3rd digit. We are trying to figure out how many numbers
less than or equal to 67294 have a 1 at the 3rd digit. xx100 ~ xx199 would qualify where xx ranges from 0 to 67.
So 68 x 100 numbers have a 1 at the 3rd digit.

Now let's consider the number **67194** and we're again at the 3rd digit. xx100 ~ xx199 would qualify where xx
ranges from 0 to 66. 67100 ~ 67194 would also qulalify. So 67 x 100 + 95 numbers have a 1 at the 3rd digit.

Now let's consider the number **67094** and we're again at the 3rd digit. xx100 ~ xx199 would qualify where xx
ranges from 0 to 66. So 67 x 100 numbers have a 1 at the 3rd digit.

We need to figure out what the number at the current digit is. Let's call it ``d`` and then we will have 3 different
cases depending on the value of ``d``. Case 1 (d == 0). Case 2 (d == 1). Case 3 (2 <= d <= 9).

.. code-block:: java

    public int countDigitOne(int n) {
        int count = 0;

        if (n<=0)
            return 0;

        for (long digit=1; ((long)n/digit) > 0; digit = digit*10) {
            long left = n / digit;
            long right = n % digit;
            int d = (int) (left % 10); // the single digit number at the current digit
            left = left / 10;

            if (d >= 2) {
                // 2-9
                count += (left + 1) * digit;

            }
            else if (d == 1) {
                // one
                count += left * digit;
                count += right + 1;
            }
            else {
                // zero
                count += left * digit;
            }
        }

        return count;
    }
