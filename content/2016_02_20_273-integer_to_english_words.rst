273-integer_to_english_words
############################

:date: 2016-2-20 18:02
:tags: Recursion
:category: LeetCode
:slug: 273-integer_to_english_words

`LeetCode Problem Link <https://leetcode.com/problems/integer-to-english-words/>`_

The problem is not difficult and can be broken into smaller problems.

The first task is chop the number into 3-digit pieces and push them onto the stack.

.. code-block:: java

    // num is a non-negative integer
    public String numberToWords(int num) {
        if (num <= 999)
            return smallNumToWords(num);

        Stack<Integer> stk = new Stack<Integer>();

        while (num > 0) {
            int a = num % 1000;
            stk.push(a);
            num = num / 1000;
        }

        String[] strs = {
                " Billion",
                " Million",
                " Thousand",
                ""
        };

        int index = 0;
        if (stk.size() == 1)
            index = 3;
        else if (stk.size() == 2)
            index = 2;
        else if (stk.size() == 3)
            index = 1;
        else if (stk.size() == 4)
            index = 0;

        StringBuffer sb = new StringBuffer();

        //System.out.println("list size=" + list.size() + list);

        while (!stk.isEmpty()) {
            // 0 < n <= 999
            int n = stk.pop();
            String s = smallNumToWords(n);
            sb.append(s);
            sb.append(strs[index]);
            index++;

            while (!stk.isEmpty() && stk.peek()==0) {
                stk.pop();
                index++;
            }

            if (!stk.isEmpty())
                sb.append(" ");
        }
        return sb.toString();
    }

    private String smallNumToWords(int num) {
        if (num == 0)
            return "Zero";

        Stack<Integer> stk = new Stack<Integer>();

        while (num > 0) {
            int a = num % 10;
            stk.push(a);
            num = num / 10;
        }

        StringBuffer sb = new StringBuffer();

        while (!stk.isEmpty()) {
            int a = stk.pop();

            if (stk.size() == 2) {
                sb.append(singleDigitNumToWord(a));
                sb.append(" Hundred");

                if (stk.peek() != 0)
                    sb.append(" ");
            }
            else if (stk.size() == 1) {
                if (a == 1) {
                    a = a * 10 + stk.pop();

                    sb.append(doubleDigitNumToWord(a));
                }
                else {
                    sb.append(singleDigitTensNumToWord(a));

                    if (stk.peek()==0)
                        stk.pop();
                    else
                        sb.append(" ");
                }
            }
            else if (stk.size() == 0){
                sb.append(singleDigitNumToWord(a));
            }
        }

        return sb.toString();
    }

    // 10 <= num <= 19
    private String doubleDigitNumToWord(int num) {
        switch (num) {
            case 10:
                return "Ten";
            case 11:
                return "Eleven";
            case 12:
                return "Twelve";
            case 13:
                return "Thirteen";
            case 14:
                return "Fourteen";
            case 15:
                return "Fifteen";
            case 16:
                return "Sixteen";
            case 17:
                return "Seventeen";
            case 18:
                return "Eighteen";
            case 19:
                return "Nineteen";
        }
        return "";
    }

    // 1 < num <= 9
    private String singleDigitTensNumToWord(int num) {
        switch (num) {
            case 2:
                return "Twenty";
            case 3:
                return "Thirty";
            case 4:
                return "Forty";
            case 5:
                return "Fifty";
            case 6:
                return "Sixty";
            case 7:
                return "Seventy";
            case 8:
                return "Eighty";
            case 9:
                return "Ninety";
        }
        return "";
    }

    private String singleDigitNumToWord(int num) {
        switch (num) {
            case 0:
                return "Zero";
            case 1:
                return "One";
            case 2:
                return "Two";
            case 3:
                return "Three";
            case 4:
                return "Four";
            case 5:
                return "Five";
            case 6:
                return "Six";
            case 7:
                return "Seven";
            case 8:
                return "Eight";
            case 9:
                return "Nine";
        }

        return "";
    }

