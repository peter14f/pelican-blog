241-different_ways_to_add_parentheses
#####################################

:date: 2016-2-16 22:39
:tags: Parentheses
:category: LeetCode
:slug: 241-different_ways_to_add_parentheses

`LeetCode Problem Link <https://leetcode.com/problems/different-ways-to-add-parentheses/>`_

The solution to this problem turns out to be very similar to the recursive solution to
095-unique_binary_search_tree_ii.

Note that the current test cases seems to assume that the integers in the string are all single digit integers.

.. code-block:: java

    // the test cases assumes that the numbers are all one-digit itegers
    public List<Integer> diffWaysToCompute(String input) {

        List<Integer> result = new ArrayList<Integer>();

        if (input == null || input.length() == 0)
            return result;

        for (int i=0; i<input.length(); i++) {
            char c = input.charAt(i);

            if (c != '+' && c != '-' && c != '*')
                continue;

            List<Integer> leftResults = diffWaysToCompute(input.substring(0, i));
            List<Integer> rightResults = diffWaysToCompute(input.substring(i+1));

            for (int m: leftResults) {
                for (int n: rightResults) {
                    if (c == '+') {
                        result.add(m+n);
                    }
                    else if (c == '-') {
                        result.add(m-n);
                    }
                    else if (c == '*') {
                        result.add(m*n);
                    }
                }
            }
        } // for

        if (result.isEmpty()) {
            result.add(Integer.parseInt(input));
        }

        return result;
    }

