020-valid_parentheses
#####################

:date: 2015-09-07 20:22
:tags: Parentheses
:category: LeetCode
:slug: 020-valid_parentheses

`LeetCode Problem Link <https://leetcode.com/problems/valid-parentheses/>`_

This problem can be solved using a Stack of Characters. We scan the characters in the String ``s`` and push the opening
symbols '{', '(', and '[' onto the stack when we see them. When we encouter a closing symbol, we must very that the top
of the stack matches with the current closing symbol. By the time we are done scaning, the Stack must be empty.

.. code-block:: java

    public boolean isValid(String s) {

        char[] arr = s.toCharArray();
        Stack<Character> stk = new Stack<Character>();

        for (int i=0; i<arr.length; i++) {
            if (arr[i] == '{' ||
                arr[i] == '(' ||
                arr[i] == '[') {
                stk.push(arr[i]);
            }
            else {
                // must be '}' ')' or ']'

                if (stk.isEmpty())
                    return false;

                char opening = stk.pop();

                if (arr[i] == '}') {
                    if (opening != '{')
                        return false;
                }
                else if (arr[i] == ')') {
                    if (opening != '(')
                        return false;
                }
                else {
                    if (opening != '[')
                        return false;
                }
            }
        }

        return stk.isEmpty();
    }