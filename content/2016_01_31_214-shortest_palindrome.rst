214-shortest_palindrome
#######################

:date: 2016-1-31 18:18
:tags: Palindromes
:category: LeetCode
:slug: 214-shortest_palindrome

`LeetCode Problem Link <https://leetcode.com/problems/shortest-palindrome/>`_

Remember ``i``, ``j``, and ``end`` and StringBuffer's ``reverse()`` method.

.. code-block:: java

    public String shortestPalindrome(String s) {
        char[] chs = s.toCharArray();
        int i = 0;
        int end = chs.length-1;
        int j = end;

        while (i < j) {
            if (chs[i] == chs[j]) {
                i++;
                j--;
            }
            else {
                end--;
                j=end;
                i=0;
            }
        }

        StringBuffer sb = new StringBuffer(s.substring(end+1));
        sb.reverse();
        return sb.toString() + s;
    }

The best case runtime complexity is obviously O(n). The worst case runtime complexity is O(n\ :superscript:`2`).
