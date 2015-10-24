044_wildcard_matching
#####################

:date: 2015-10-1 19:10
:tags: Dynamic Programming, String Matching
:category: LeetCode
:slug: 044_wildcard_matching

`LeetCode Problem Link <https://leetcode.com/problems/wildcard-matching/>`_

The notation ``s(1:i)`` refers to the substring of string ``s`` that starts with the ``1st`` character of ``s`` and
ends with the ``ith`` character of ``s``.

For example, if s = "abc" s(1:2) refers to the substring "ab"

The notation ``s(i)`` refers to the ``ith`` character of string ``s``.

For example, if s = "abc" s(1) refers to the 1st character 'c'

Given the String ``s`` (of length ``i``) and the pattern (also a String) ``p`` (of length ``j``),
can we solve the problem based on a subproblem whose inputs are s(1:i-1) and p(1:j-1)?

Case 1:

If ``p(j) == '?'`` or ``p(j) == s(i)``, then we know it's a match if ``s(1:i-1)`` matches with ``p(1:j-1)``.

Case 2:

If ``p(j) == '*'``, then we know it's a match if at least one of the following is true

  if dp[i][j-1] is true

  if dp[i-1][j] is true

  if dp[i-1][j-1] is true

.. code-block:: java

    public boolean isMatch(String s, String p) {

        char[] s_arr = s.toCharArray();
        char[] p_arr = p.toCharArray();

        boolean[][] dp = new boolean[s_arr.length+1][p_arr.length+1];

        dp[0][0] = true;

        // first column - empty patter - default is false

        // first row
        // empty string
        for (int j=1; j<=p_arr.length; j++) {
            if (p_arr[j-1] == '*') {
                dp[0][j] = dp[0][j-1];
            }
            // else default value is false
        }

        for (int i=1; i<=s_arr.length; i++) {
            for (int j=1; j<=p_arr.length; j++) {

                if (p_arr[j-1] != '*') {
                    if (p_arr[j-1] == '?' || s_arr[i-1] == p_arr[j-1]) {
                        dp[i][j] = dp[i-1][j-1];
                    }
                    // else default value is false
                }
                else {

                    boolean matchNone = dp[i][j-1];
                    boolean matchOne = dp[i-1][j-1];
                    boolean matchMany = dp[i-1][j];

                    dp[i][j] = matchNone || matchOne || matchMany;
                }
            }
        }

        return dp[s_arr.length][p_arr.length];
    }