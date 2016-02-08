227_basic_calculator_ii
#######################

:date: 2016-2-8 21:34
:tags: Calculators, Stacks
:category: LeetCode
:slug: 227_basic_calculator_ii

`LeetCode Problem Link <https://leetcode.com/problems/basic-calculator-ii/>`_

Here I present a solution using two stacks, a Stack<Integer> to store the numbers and a Stack<Character> to store
the operations.

Note that ``evaluateMultDiv()`` does not require temporary stacks because it is called right after we have one operator
and two operands. ``evaluateAddSubtract()`` on the other hand requires two temporary stacks since we need to evaluate
from left to right.

.. code-block:: java

    private void evaluateAddSubtract(Stack<Integer> nums, Stack<Character> ops) {
        Stack<Integer> numsReversed = new Stack<Integer>();

        while (!nums.isEmpty())
            numsReversed.push(nums.pop());


        Stack<Character> opsReversed = new Stack<Character>();

        while (!ops.isEmpty())
            opsReversed.push(ops.pop());

        int a = numsReversed.pop();
        while (!opsReversed.isEmpty()) {
            char op = opsReversed.pop();
            int b = numsReversed.pop();

            if (op == '+')
                a = a+b;
            else
                a = a-b;
        }

        nums.push(a);
    }

    private void evaluateMultDiv(Stack<Integer> nums, Stack<Character> ops) {
        int b = nums.pop();
        char op = ops.pop();
        int a = nums.pop();

        if (op == '*')
            nums.push(a*b);
        else
            nums.push(a/b);
    }

    private boolean isNum(char c) {
        return (c >= '0' && c <= '9');
    }

    private int calculateNoSpace(String s) {
        char[] sArr = s.toCharArray();

        if (sArr.length == 0)
            return 0;

        Stack<Integer> nums = new Stack<Integer>();
        Stack<Character> ops = new Stack<Character>();

        int num = 0;
        for (int i=0; i<sArr.length; i++) {
            if (isNum(sArr[i])) {
                if (i > 0 && isNum(sArr[i-1]))
                    num = num * 10 + (sArr[i] - '0');
                else
                    num = sArr[i] - '0';

                if (i == sArr.length - 1 || !isNum(sArr[i+1])) {
                    nums.push(num);
                    if (!ops.isEmpty() &&
                            (ops.peek() == '*' || ops.peek() == '/'))
                           evaluateMultDiv(nums, ops);
                }


            }
            else
                ops.push(sArr[i]);
        }

        if (!ops.isEmpty())
            evaluateAddSubtract(nums, ops);

        return nums.peek();
    }

    public int calculate(String s) {
        StringBuffer sb = new StringBuffer();

        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (c != ' ')
                sb.append(c);
        }

        return calculateNoSpace(sb.toString());
    }