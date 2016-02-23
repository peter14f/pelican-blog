282-expresseion_add_operators
#############################

:date: 2016-2-21 22:06
:tags: DFS
:category: LeetCode
:slug: 282-expresseion_add_operators

`LeetCode Problem Link <https://leetcode.com/problems/expression-add-operators/>`_

This problem asks us to find all possible ways to insert binary operators +, -, * into the string such that
the result is ``target``.

Please note that not inserting anything is one way as well.

Let's solve an easier problem first, say the binary operators are only '+' and '-'.

.. code-block:: java

    public List<String> addOperators(String num, int target) {

        List<String> result = new ArrayList<String>();

        dfsAddToResult(num, 0, target,
                       0,
                       "",
                       result);

        return result;
    }

    private void dfsAddToResult(String num, int start, int target,
                                int curSum,
                                String curStr,
                                List<String> result) {

        if (start == num.length()) {
            if (curSum == target)
                result.add(curStr);
            return;
        }

        for (int end=start; end<num.length(); end++) {
            String aStr = num.substring(start, end+1);

            if (aStr.length() > 1 && num.charAt(start) == '0')
                break;

            int a = Integer.parseInt(aStr);

            if (curStr.isEmpty()) {
                dfsAddToResult(num, end+1, target,
                               curSum + a,
                               curStr + a,
                               result);
            }
            else {
                // put a '+'
                dfsAddToResult(num, end+1, target,
                               curSum + a,
                               curStr + '+' + a,
                               result);

                // put a '-'
                dfsAddToResult(num, end+1, target,
                               curSum - a,
                               curStr + "-" + a,
                               result);

            }
        }
    }


Now putting a '*' would not be as straightforward. What do we set ``curSum`` to if the current number is ``a``?

::

    curSum = curSum * a

wouldn't be correct. We need to the previous number and subtract that from curSum before we add ``prevNum*a``

::

    curSum = curSum - prevNum + (prevNum * a)

Now we also need to think about what ``prevNum`` should be set to when we are adding a '*'.

::

    // put a '*'
    dfsAddToResult(num, end+1, target,
                   curSum-prevNum + prevNum*a,
                   curStr + "*" + a,
                   prevNum*a,
                   result);

Here is what I got so far

.. code-block:: java

    public List<String> addOperators(String num, int target) {

        List<String> result = new ArrayList<String>();

        dfsAddToResult(num, 0, target,
                       0,
                       "",
                       0,
                       result);

        return result;
    }

    /* prevNum is needed when trying to add a '*' because the new sum won't be
     *
     * curSum * a
     *
     * Instead we need to know the prevNum and set curSum to
     *
     * curSum - prevNum + prevNum * a
     *
     */
    private void dfsAddToResult(String num, int start, int target,
                                int curSum,
                                String curStr,
                                int prevNum,
                                List<String> result) {

        if (start == num.length()) {
            if (curSum == target)
                result.add(curStr);
            return;
        }

        for (int end=start; end<num.length(); end++) {
            String aStr = num.substring(start, end+1);

            if (aStr.length() > 1 && num.charAt(start) == '0')
                break;

            int a = Integer.parseInt(aStr);

            if (curStr.isEmpty()) {
                dfsAddToResult(num, end+1, target,
                               curSum + a,
                               curStr + a,
                               a,
                               result);
            }
            else {
                // put a '+'
                dfsAddToResult(num, end+1, target,
                               curSum + a,
                               curStr + '+' + a,
                               a,
                               result);

                // put a '-'
                dfsAddToResult(num, end+1, target,
                               curSum - a,
                               curStr + "-" + a,
                               -a,
                               result);

                // put a '*'
                dfsAddToResult(num, end+1, target,
                               curSum-prevNum + prevNum*a,
                               curStr + "*" + a,
                               prevNum*a,
                               result);
            }
        } // for end
    }

::

    Runtime Error Message:
    Line 42: java.lang.NumberFormatException: For input string: "3456237490"
    Last executed input:
    "3456237490"
    9191

This is the error message I got, I see 3.4 billion number which is larger than what an int can store.

.. code-block:: java

    public List<String> addOperators(String num, int target) {

        List<String> result = new ArrayList<String>();

        dfsAddToResult(num, 0, target,
                       0,
                       "",
                       0,
                       result);

        return result;
    }

    /* prevNum is needed when trying to add a '*' because the new sum won't be
     *
     * curSum * a
     *
     * Instead we need to know the prevNum and set curSum to
     *
     * curSum - prevNum + prevNum * a
     *
     */
    private void dfsAddToResult(String num, int start, int target,
                                long curSum,
                                String curStr,
                                long prevNum,
                                List<String> result) {

        if (start == num.length()) {
            if (curSum == target)
                result.add(curStr);
            return;
        }

        for (int end=start; end<num.length(); end++) {
            String aStr = num.substring(start, end+1);

            if (aStr.length() > 1 && num.charAt(start) == '0')
                break;

            long a = Long.parseLong(aStr);

            if (curStr.isEmpty()) {
                dfsAddToResult(num, end+1, target,
                               curSum + a,
                               curStr + a,
                               a,
                               result);
            }
            else {
                // put a '+'
                dfsAddToResult(num, end+1, target,
                               curSum + a,
                               curStr + '+' + a,
                               a,
                               result);

                // put a '-'
                dfsAddToResult(num, end+1, target,
                               curSum - a,
                               curStr + "-" + a,
                               -a,
                               result);

                // put a '*'
                dfsAddToResult(num, end+1, target,
                               curSum-prevNum + prevNum*a,
                               curStr + "*" + a,
                               prevNum*a,
                               result);
            }
        } // for end
    }





