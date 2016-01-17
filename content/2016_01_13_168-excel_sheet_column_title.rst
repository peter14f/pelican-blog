168-excel_sheet_column_title
############################

:date: 2016-1-13 23:13
:tags: Excel
:category: LeetCode
:slug: 168-excel_sheet_column_title

`LeetCode Problem Link <https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/>`_

We are turning a base-10 number into a base-26 number. Modding by 26 will generate an integer in the range [0, 25].

This can be genaralized to converting a base-10 number into any base-x number.

.. code-block:: java

    public String convertToTitle(int n) {
        StringBuffer sb = new StringBuffer();

        while (n > 0) {
            n--;
            int num = n%26;
            n = n / 26;
            sb.append((char)('A' + num));
        }

        sb.reverse();
        return sb.toString();
    }

