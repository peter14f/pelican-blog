012-integer_to_roman
####################

:date: 2015-09-07 20:14
:tags: Roman Numerals
:category: LeetCode
:slug: 012-integer_to_roman

`LeetCode Problem Link <https://leetcode.com/problems/integer-to-roman/>`_

Do problem ``013-roman_to_integer`` before this problem.

One thing the remember is that digits larger than five (but not nine) should
be have the Roman Numeral for 5 inserted first.

.. code-block:: java

    public String intToRoman(int num) {

        int divisor = 1000;
        StringBuffer sb = new StringBuffer();

        for (int i=4; i>=1; i--) {

            int digit = num / divisor;

            if (digit==4) {
                appendForFour(sb, divisor);
            }
            else if (digit==9) {
                appendForNine(sb, divisor);
            }
            else if (digit >= 5) {
                appendForFive(sb, divisor);
                append(sb, divisor, digit-5);
            }
            else if (digit==1) {
                appendForOne(sb, divisor);
            }
            else if (digit > 0){
                append(sb, divisor, digit);
            }

            num = num - digit*divisor;
            divisor = divisor / 10;
        }

        return sb.toString();
    }

    private void appendForFour(StringBuffer sb, int divisor) {
        switch (divisor) {
            /* L=50 C=100 D=500*/
            case 100:
                sb.append('C');
                sb.append('D');
                break;
            case 10:
                sb.append('X');
                sb.append('L');
                break;
            case 1:
                sb.append('I');
                sb.append('V');
                break;
        }
    }

    private void appendForNine(StringBuffer sb, int divisor) {
        switch (divisor) {
            // L=50 C=100 D=500 M=1000
            case 100:
                sb.append('C');
                sb.append('M');
                break;
            case 10:
                sb.append('X');
                sb.append('C');
                break;
            case 1:
                sb.append('I');
                sb.append('X');
                break;
        }
    }

    private void appendForFive(StringBuffer sb, int divisor) {
        char toAppend = 'D';
        switch (divisor) {

            case 100:
                toAppend = 'D';
                break;
            case 10:
                toAppend = 'L';
                break;
            case 1:
                toAppend = 'V';
                break;
        }
        sb.append(toAppend);
    }

    private void appendForOne(StringBuffer sb, int divisor) {
        char toAppend = 'M';
        switch (divisor) {
            case 1000:
                toAppend = 'M';
                break;
            case 100:
                toAppend = 'C';
                break;
            case 10:
                toAppend = 'X';
                break;
            case 1:
                toAppend = 'I';
                break;
        }
        sb.append(toAppend);
    }

    private void append(StringBuffer sb, int divisor, int digit) {
        char toAppend = 'M';
        switch (divisor) {
            case 1000:
                toAppend = 'M';
                break;
            case 100:
                toAppend = 'C';
                break;
            case 10:
                toAppend = 'X';
                break;
            case 1:
                toAppend = 'I';
                break;
        }

        for (int i=0; i<digit; i++) {
            sb.append(toAppend);
        }
    }
