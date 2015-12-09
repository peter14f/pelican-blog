131-palindrome_partitioning
###########################

:date: 2015-12-8 19:05
:tags: DFS, Memoization, Palindromes
:category: LeetCode
:slug: 131-palindrome_partitioning

`LeetCode Problem Link <https://leetcode.com/problems/palindrome-partitioning/>`_

``isPalindrome`` is a 2D boolean array. ``isPalindrome[i][j]`` tells us if the substring s[i..j] is a palindrome.
Notice that we will only be filling in the upper right half of the 2D array. Once this is built, we can do a
dfs and obtain all the parlindrone partitions.

.. code-block:: java

    public List<List<String>> partition(String s) {

        List<List<String>> partitions = new ArrayList<List<String>>();
        if (s == null || s.length() == 0)
            return partitions;

        char[] sArr = s.toCharArray();
        int n = sArr.length;
        boolean[][] isPalindrome = new boolean[n][n];

        for (int row=0; row<n; row++) {
            isPalindrome[row][row] = true;
            if (row+1 < n) {
                if (sArr[row] == sArr[row+1]) {
                    isPalindrome[row][row+1] = true;
                }
            }
        }

        int dist = 2;

        while (dist < n) {
            for (int row=0; row < n; row++) {
                if (row + dist < n) {
                    if (isPalindrome[row+1][row+dist-1] && sArr[row] == sArr[row+dist]) {
                        isPalindrome[row][row+dist] = true;
                    }
                }
            }

            dist++;
        }

        dfs(sArr, isPalindrome, 0, new ArrayList<String>(), partitions);

        return partitions;
    }

    private void dfs(char[] sArr, boolean[][] isPalindrome, int start,
                     List<String> curList, List<List<String>> partitions) {

        int n = sArr.length;

        for (int col=start; col<n; col++) {
            if (isPalindrome[start][col]) {
                String str = new String(sArr, start, col-start+1);
                curList.add(str);

                if (col < n-1) {
                    dfs(sArr, isPalindrome, col+1, curList, partitions);
                }
                else {
                    partitions.add(new ArrayList<String>(curList));
                }

                curList.remove(curList.size() - 1);
            }
        }
    }
