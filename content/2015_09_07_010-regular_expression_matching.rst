010-regular_expression_matching
###############################

:date: 2015-09-07 18:29
:tags: Dynamic Programming, String Matching
:category: LeetCode
:slug: 010-regular_expression_matching

`LeetCode Problem Link <https://leetcode.com/problems/regular-expression-matching/>`_


The notation ``s(1:i)`` refers to the substring of string ``s`` that starts with the ``1st`` character of ``s`` and
ends with the ``ith`` character of ``s``.

For example, if s = "abc" s(1:2) refers to the substring "ab"

The notation ``s(i)`` refers to the ``ith`` character of string ``s``.

For example, if s = "abc" s(1) refers to the 1st character 'c'

Given the String ``s`` (of length ``i``) and the regular expression pattern (also a String) ``p`` (of length ``j``),
can we solve the problem based on a subproblem whose inputs are s(1:i-1) and p(1:j-1)?

Case 1:

If ``p(j) == '.'`` or ``p(j) == s(i)``, then we know it's a match if ``s(1:i-1)`` matches with ``p(1:j-1)``.


Case 2:

If ``p(j) == '*'`` and ( p(j-1) == '.' or p(j-1) == s(i) ), then it's a match if at least one of following is true

  if s(1:i-1) matches with p(1:j-2)

  if s(1:i-1) matches with p(1:j)

  if s(1:i) matches with p(1:j-2)


Case 3:

if ``p(j) == '*'`` and p(j-1) != '.' and p(j-1) != s(i), then it's a match ony if

  if s(1:i) matches with p(1:j-2)


We build a 2D boolean table ``dp``.

``boolean[][] dp = new boolean[s.length()][p.length()]``

``dp[i][j]`` is ``true`` <=> s(0:i) matches with p(0:j)

``dp[0][0]`` is always ``true`` because the empty string matches with the empty pattern.

The first column refers to matching with the empty pattern. Any nonempty string s cannot match with the empty pattern.

The first row refers to empty string matching with some pattern which can only be ``true`` if p(j) == '*' and
``dp[0]j-2]`` is ``true``


.. code-block:: java

    public boolean isMatch(String s, String p) {
        char[] s_arr = s.toCharArray();
        char[] p_arr = p.toCharArray();

        boolean[][] dp = new boolean[s_arr.length + 1][p_arr.length + 1];

        // empty string matches with empty pattern
        dp[0][0] = true;

        // first column - empty pattern => default value is false anyways

        // first row - empty string
        for (int j=1; j<=p_arr.length; j++) {
            if (p_arr[j-1] == '*') {
                dp[0][j] = dp[0][j-2];
            }
            // else default value is false anyways
        }

        for (int i=1; i<=s_arr.length; i++) {
            for (int j=1; j<=p_arr.length; j++) {

                if (p_arr[j-1] != '*') {

                    if (p_arr[j-1] == '.' || s_arr[i-1] == p_arr[j-1]) {
                        dp[i][j] = dp[i-1][j-1];
                    }

                }
                else {
                    if (j-2 >= 0 && (p_arr[j-2] == '.' || s_arr[i-1] == p_arr[j-2])) {
                        boolean matchOne = dp[i-1][j-2];
                        boolean matchMany = dp[i-1][j];

                        dp[i][j] = matchOne || matchMany;
                    }

                    boolean matchNone = dp[i][j-2];
                    dp[i][j] = dp[i][j] || matchNone;
                }
            }
        }

        return dp[s_arr.length][p_arr.length];
    }