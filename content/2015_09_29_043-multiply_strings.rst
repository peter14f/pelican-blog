043-multiply_strings
####################

:date: 2015-9-29 22:30
:tags: multiplication
:category: LeetCode
:slug: 043-multiply_strings

`LeetCode Problem Link <https://leetcode.com/problems/multiply-strings/>`_

I couldn't get the large input test case to pass because I didn't solve the problem
the right way.

Here's the key observation

(First digit refers to the least significant digit, second digit refers to the 2nd least significant digit, and so on)

The 1st digit of the product is
(the product of the 1st digit of num1 and the 1st digit of num2).


The 2nd digit of the product is
(product of the 1st digit of num2 and the 2nd digit of num1) +
(prodcut of the 2nd digit if num1 and the 1st digit of num2)


The 3rd digit of the product is
(product of the 1st digit of num1 and the 3rd digit of num2) +
(product of the 2nd digit of num1 and the 2nd digit of num2) +
(product of the 3rd digit of num1 and the 1st digit of num2)


Let ``number1`` be a String of the reversed version of ``num1`` and ``number2`` be a String of the reversed version of
``num1``. We know the multiplication result will have at most num1.length() + num2.length() digits. Hence we allocate an int array
``result`` of that size. Note that in Java, the array elements will be initialized to zero.




Let ``i`` be the index traversing ``number1`` starting from ``0``

  Let ``j`` be the index traversing ``number2`` starting from ``0``

    ``result[i+j] += number1.charAt(i) * number2.charAt(j)``


.. code-block:: java

    public String multiply(String num1, String num2) {

        int[] result = new int[num1.length() + num2.length()];

        StringBuffer number1 = new StringBuffer(num1);
        StringBuffer number2 = new StringBuffer(num2);

        number1.reverse();
        number2.reverse();

        for (int i=0; i<number1.length(); i++) {
            for (int j=0; j<number2.length(); j++) {
                int a = number1.charAt(i) - '0';
                int b = number2.charAt(j) - '0';

                result[i+j] += a*b;
            }
        }

        int carry = 0;
        for (int i=0; i<result.length; i++) {

            if (carry > 0) {
                result[i] += carry;
                carry = 0;
            }

            if (result[i] > 9) {
                carry = result[i] / 10;
                result[i] = result[i] % 10;
            }
        }

        StringBuffer sb = new StringBuffer();
        boolean firstNonZeroFound = false;

        for (int i=result.length - 1; i>=0; i--) {
            if (firstNonZeroFound) {
                sb.append(result[i]);
            }
            else {
                if (result[i] > 0) {
                    firstNonZeroFound = true;
                    sb.append(result[i]);
                }
            }
        }

        if (!firstNonZeroFound)
            sb.append(0);

        return sb.toString();
    }

This implementation takes O(n\ :superscript:`2`) time.