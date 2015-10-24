022-generate_parentheses
########################

:date: 2015-09-07 20:24
:tags: Parentheses, DFS, NP
:category: LeetCode
:slug: 022-generate_parentheses

`LeetCode Problem Link <https://leetcode.com/problems/generate-parentheses/>`_

We keep track of the number of opens and number of closes left in variables ``numOpen`` and ``numClose`` respectively.
We use recursion. And one thing to note is that if inserting one more close symbol causes the number of open symbols
left to be less than the number of closes left, then we should **NOT** consider inserting more close symbols.

.. code-block:: java

    public List<String> generateParenthesis(int n) {

        int numOpen = n;
        int numClose = n;

        List<String> ans = new ArrayList<String>();

        StringBuffer sb = new StringBuffer();

        sb.append('(');
        numOpen--;

        generateParentheses(sb, ans, numOpen, numClose);

        return ans;
    }

    private void generateParentheses(StringBuffer sb,
                                    List<String> ans,
                                    int numOpen,
                                    int numClose) {

        if (numOpen <=0 && numClose <= 0) {
            ans.add(sb.toString());
            return;
        }

        if (numOpen > 0) {
            sb.append('(');
            int newSize = sb.length();
            generateParentheses(sb, ans, numOpen-1, numClose);
            sb.deleteCharAt(newSize - 1);
        }

        if (numClose > 0 && numClose - 1 >= numOpen) {
            sb.append(')');
            int newSize = sb.length();
            generateParentheses(sb, ans, numOpen, numClose-1);
            sb.deleteCharAt(newSize - 1);
        }
    }
