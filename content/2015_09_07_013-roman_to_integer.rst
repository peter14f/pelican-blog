013-romain_to_integer
#####################

:date: 2015-09-07 20:15
:tags: Roman Numerals
:category: LeetCode
:slug: 013-roman_to_integer

`LeetCode Problem Link <https://leetcode.com/problems/trapping-rain-water/>`_

| I - 1
| V - 5
| X - 10
| L - 50
| C - 100
| D - 500
| M - 1000

You should know the numbers for ``I``,  ``V``,  ``X``. And ``L``, ``C``, ``D`` follow (LCD should be easy to remember).
The last letter is ``M``.

.. code-block:: java

    public int romanToInt(String s) {
        char[] s_arr = s.toCharArray();

        /* I -    1
         * V -    5
         * X -   10
         * L -   50
         * C -  100
         * D -  500
         * M - 1000
         *
         * 4 and 9
         */

        int sum = 0;

        for (int i=0; i<s_arr.length; i++) {

            int combo = nextCanBeSubtracted(s_arr, i);

            if (combo == 0) {
                sum += romanCharToInt(s_arr[i]);
            }
            else {
                sum += combo;
                i++;
            }
        }

        return sum;
    }

    private int nextCanBeSubtracted(char[] s_arr, int index) {

        int ans = 0;

        if (index + 1 < s_arr.length) {
            char next = s_arr[index+1];
            char cur = s_arr[index];

            switch (next) {
                case 'V': // 5
                    if (cur=='I')
                        ans = 4;
                    break;
                case 'X': // 10
                    if (cur=='I')
                        ans = 9;
                    break;
                case 'L': // 50
                    if (cur=='X')
                        ans = 40;
                    break;
                case 'C': // 100
                    if (cur=='X')
                        ans = 90;
                    break;
                case 'D': // 500
                    if (cur=='C')
                        ans = 400;
                    break;
                case 'M': // 1000
                    if (cur=='C')
                        ans = 900;
                    break;
                default:
                    ans = 0;
            }
        }

        return ans;
    }

    private int romanCharToInt(char c) {
        int num = 0;
        switch (c) {
            case 'I':
                num = 1;
                break;
            case 'V':
                num = 5;
                break;
            case 'X':
                num = 10;
                break;
            case 'L':
                num = 50;
                break;
            case 'C':
                num = 100;
                break;
            case 'D':
                num = 500;
                break;
            case 'M':
                num = 1000;
                break;
            default:
                num = 0;
        }

        return num;
    }
