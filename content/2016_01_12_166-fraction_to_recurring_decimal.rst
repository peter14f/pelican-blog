166-fraction_to_recurring_decimal
#################################

:date: 2016-1-12 18:20
:tags: Division
:category: LeetCode
:slug: 166-fraction_to_recurring_decimal

`LeetCode Problem Link <https://leetcode.com/problems/fraction-to-recurring-decimal/>`_

The key is use a HashMap where the key is the remainder and the value is the decimal position in which the remainder is
generated.

And every time we are dealing with division, we always need to take of overflowing and the sign of the result.

.. code-block:: java

    public String fractionToDecimal(int numerator, int denominator) {
        StringBuffer sb = new StringBuffer();

        long remainder = numerator;
        long denom = denominator;
        boolean negative = false;
        boolean empty = true;
        boolean recurring = false;
        HashMap<Long, Integer> dict = new HashMap<Long, Integer>();
        StringBuffer decimalNum = new StringBuffer();
        int position = 0;

        if (remainder < 0 && denom > 0) {
            negative = true;
            remainder = -remainder;
        }
        else if (remainder > 0 && denom < 0) {
            negative = true;
            denom = -denom;
        }
        else if (remainder < 0 && denom < 0) {
            denom = -denom;
            remainder = -remainder;
        }

        do {
            long q = remainder / denom;
            remainder = remainder % denom;

            if (empty) {
                if (negative)
                    sb.append("-");

                sb.append(q);

                if (remainder == 0)
                    break;

                sb.append(".");
                empty = false;
            }
            else {
                decimalNum.append(q);
            }

            remainder = remainder * 10;
            position++;

            if (!dict.containsKey(remainder)) {
                dict.put(remainder, position);
            }
            else {
                position = dict.get(remainder);
                recurring = true;
                break;
            }

        } while (remainder > 0);

        if (!recurring)
            sb.append(decimalNum);
        else {
            for (int i=1; i<=decimalNum.length(); i++) {
                if (i == position) {
                    sb.append("(");
                }
                sb.append(decimalNum.charAt(i-1));
            }
            sb.append(")");
        }

        return sb.toString();
    }

