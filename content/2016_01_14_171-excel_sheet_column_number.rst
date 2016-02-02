171-excel_sheet_column_number
#############################

:date: 2016-1-14 21:43
:tags: Excel
:category: LeetCode
:slug: 171-excel_sheet_column_number

`LeetCode Problem Link <https://leetcode.com/problems/excel-sheet-column-number/>`_

Much easier than 168-excel_sheet_column_title. Go through each letter from the least significant
digit, find the number that the letter corresponds to and then multiply it by the number of
the digit.

.. code-block:: java

    public int titleToNumber(String s) {
        int sum = 0;
        int digit = 0;

        for (int i=s.length()-1; i>=0; i--) {
            int d = (int)Math.pow(26, digit);
            int num = s.charAt(i) - 'A' + 1;

            sum += num*d;

            digit++;
        }

        return sum;
    }

This takes O(n) where ``n`` is the length the string ``s``.