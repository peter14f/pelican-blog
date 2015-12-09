132-palindrome_partitioning_ii
##############################

:date: 2015-12-9 13:11
:tags: Dynamic Programming, Palindromes
:category: LeetCode
:slug: 132-palindrome_partitioning_ii

`LeetCode Problem Link <https://leetcode.com/problems/palindrome-partitioning-ii/>`_

First, build the 2D boolean array as we did in the previous problem, 131-palindrome_partitioning.

Let ``n`` be the length of the input string. Allocate a boolean array of size ``n`` and call it ``minCuts``.

``minCuts[i]`` is the minimum number of ways to cut the substring starting at index ``i``

We will fill in the elements of this array from right to left and finally return ``minCuts[0]`` as the answer
since we are looking for the minimum number of cuts needed to partition the input string ``s`` into palindromes.

We will first initialize all elements to the length of the substring - 1. All all non-empty strings, the most number
of cuts to partition the string into palindromes is always the length - 1.

If ``isPalindrome[i][n-1]`` is true, then it's clear that ``minCuts[i]`` is 0 and we don't need to attempt to find
a smaller number of cuts.

.. code-block:: java

    public int minCut(String s) {
        char[] sArr =  s.toCharArray();
        int n = sArr.length;

        boolean[][] isPalindrome = new boolean[n][n];

        for (int row=0; row<n; row++) {
            isPalindrome[row][row] = true;

            if (row + 1 < n) {
                if (sArr[row] == sArr[row+1]) {
                    isPalindrome[row][row+1] = true;
                }
            }
        }

        int dist = 2;

        while (dist < n) {
            for (int row=0; row<n; row++) {
                if (row + dist < n) {
                    if (isPalindrome[row+1][row+dist-1] && sArr[row] == sArr[row+dist]) {
                        isPalindrome[row][row+dist] = true;
                    }
                }
            }
            dist++;
        }

        int[] minCut = new int[n];

        for (int start = n-1; start>=0; start--) {
            minCut[start] = n-1-start; // chop into single characters
                                       // this is the maximum number of cuts needed

            if (isPalindrome[start][n-1]) {
                // no need to look for a smaller number of cuts needed
                minCut[start] = 0;
            }
            else {
                for (int cut=start; cut<=n-1; cut++) {
                    if (isPalindrome[start][cut]) {
                        minCut[start] = Math.min(1 + minCut[cut+1], minCut[start]);
                    }
                }
            }
        }

        return minCut[0];
    }
