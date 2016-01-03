150-evaluate_reverse_polish_notation
####################################

:date: 2015-12-28 20:15
:tags:
:category: LeetCode
:slug: 150-evaluate_reverse_polish_notation

`LeetCode Problem Link <https://leetcode.com/problems/evaluate-reverse-polish-notation/>`_

The pattern is clear. When you see an operator, the first popped element is the second operand and the
second popped element is the first operand. Once the operation is performed, the result needs to be pushed
back onto the stack. When you see a non operator, simply push the integer on the stack.

.. code-block:: java

    private int isOperator(String s) {
        if (s.length() != 1)
            return 0;

        char op = s.toCharArray()[0];
        int operator = 0;

        switch(op) {
            case '+':
                operator = 1;
                break;
            case '-':
                operator = 2;
                break;
            case '*':
                operator = 3;
                break;
            case '/':
                operator = 4;
                break;
            default:
                operator=0;
        }

        return operator;
    }

    public int evalRPN(String[] tokens) {
        Stack<Integer> stk = new Stack<Integer>();

        for (int i=0; i<tokens.length; i++) {
            String s = tokens[i];

            int op = isOperator(s);

            if (op > 0) {
                if (stk.size() < 2)
                    throw new IllegalArgumentException();

                int b = stk.pop();
                int a = stk.pop();

                int result = performOp(op, a, b);
                stk.push(result);
            }
            else {
                stk.push(Integer.parseInt(s));
            }
        }

        return stk.peek();
    }

    private int performOp(int op, int a, int b) {

        if (op==1)
            return a+b;
        else if (op==2)
            return a-b;
        else if (op==3)
            return a*b;
        else
            return a/b;
    }
