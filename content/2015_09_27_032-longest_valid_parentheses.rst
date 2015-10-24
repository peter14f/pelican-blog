032-longest_valid_parentheses
#############################

:date: 2015-09-27 10:44
:tags: Parentheses
:category: LeetCode
:slug: 032-longest_valid_parentheses

`LeetCode Problem Link <https://leetcode.com/problems/longest-valid-parentheses/>`_

We will use a stack to store the indices for opening parentheses. We want to pass the following input cases:

| (()
| (()()
| )))()

The trick is that after we pop the corresponding opening index from the stack, we need to check if the
stack is empty or not. If the stack is not empty, the top of the stack contains the index ``i``
of the previous opening parenthesis. ``i+1`` should be used when calculating the length.

.. code-block:: java

    public int longestValidParentheses(String s) {
        int maxLength = 0;
        char[] s_arr = s.toCharArray();

        Stack<Integer> stk = new Stack<Integer>();
        int start = -1;

        for (int i=0; i<s_arr.length; i++) {
            if (s_arr[i] == '(') {
                stk.push(i);
                if (start == -1)
                    start = i;
            }
            else {
                // must be '('

                if (!stk.isEmpty()) {
                    stk.pop();
                    int length = 0;

                    if (!stk.isEmpty())
                        length = i - stk.peek();
                    else
                        length = i - start + 1;

                    if (length > maxLength)
                        maxLength = length;
                }
                else {
                    // the continuance is broken
                    if (start != -1)
                        start = -1;
                }
            }
        }

        return maxLength;
    }