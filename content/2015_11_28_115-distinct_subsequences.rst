115-distinct_subsequences
#########################

:date: 2015-11-28 20:49
:tags: Subsequences
:category: LeetCode
:slug: 115-distinct_subsequences

`LeetCode Problem Link <https://leetcode.com/problems/distinct-subsequences/>`_

The first way is to use recursion. This won't pass the big test cases on OJ.

.. code-block:: java

    public int numDistinct(String s, String t) {
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        int[] num = {0};

        numDistinct(sArr, 0, tArr, 0, num);

        return num[0];
    }

    private void numDistinct(char[] sArr, int i, char[] tArr, int j, int[] num) {

        if (i==sArr.length || j==tArr.length)
            return;

        if (sArr[i] == tArr[j]) {
            if (j == tArr.length - 1) {
                num[0]++;
            }

            numDistinct(sArr, i+1, tArr, j+1, num);
            numDistinct(sArr, i+1, tArr, j, num);

        }
        else {
            numDistinct(sArr, i+1, tArr, j, num);
        }
    }

The second way is store all the indices that appear in string ``s``  in an array list.

.. code-block:: java

    // count the number of distinct subsequences of t in s
    public int numDistinct(String s, String t) {
        char[] tArr = t.toCharArray();
        char[] sArr = s.toCharArray();

        List<List<Integer>> indices = new ArrayList<List<Integer>>();

        HashMap<Character, List<Integer>> map = new HashMap<Character, List<Integer>>();
        HashSet<Character> tChars = new HashSet<Character>();

        for (int i=0; i<tArr.length; i++) {
            tChars.add(tArr[i]);
        }

        for (int i=0; i<sArr.length; i++) {
            char c = sArr[i];

            if (tChars.contains(c)) {
                if (map.containsKey(c)) {
                    List<Integer> index = map.get(c);
                    index.add(i);
                }
                else {
                    List<Integer> index = new ArrayList<Integer>();
                    index.add(i);
                    map.put(c, index);
                }
            }
        }

        for (int i=0; i<tArr.length; i++) {
            char c = tArr[i];
            if (!map.containsKey(c))
                return 0;

            indices.add(map.get(c));
        }

        System.out.println(indices);

        int[] ans = {0};
        countNumDistinctSubsequences(indices, 0, new ArrayList<Integer>(), ans);
        return ans[0];
    }

    private void countNumDistinctSubsequences(List<List<Integer>> indices, int i, List<Integer> curList, int[] ans) {

        List<Integer> numbers = indices.get(i);

        if (numbers.isEmpty())
            return;

        for (int j=0; j<numbers.size(); j++) {
            int num = numbers.get(j);

            if (curList.isEmpty() || num > curList.get(curList.size() - 1)) {
                curList.add(num);

                if (curList.size() == indices.size()) {
                    ans[0]++;
                }
                else {
                    countNumDistinctSubsequences(indices, i+1, curList, ans);
                }

                curList.remove(curList.size() - 1);
            }
        }

    }

Lastly, it's the DP solution. num[i][j] is the number of distinct subsequences of t(1, j) can be found in s(1, j).
The first column is filled with 1s because deleting all characters results in the empty string. And that's the only way
you can find the empty subsequence. The first row besides the first column in first row is filled with 0 because
you cannot find a non-empty subsequence from a empty string.

What about the other cells in the table? if s[i] == t[j], then num[i][j] = num[i-1][j] + num[i-1][j-1]. The former is
when we do delete the character at index j. The later is when we don't.

if s[i] != t[j], then num[i][j] = num[i-1][j-1].

.. code-block:: java

    public int numDistinct(String s, String t) {
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        int[][] num = new int[sArr.length + 1][tArr.length + 1];

        /* first column, if you just delete all characters in s, you get
         * an empty string
         */
        for (int row=0; row<=sArr.length; row++) {
            num[row][0] = 1;
        }

        /* first row, no way to get to a non-empty string from
         * an empty string
         */
        for (int col=1; col<=tArr.length; col++) {
            num[0][col] = 0;
        }

        for (int row=1; row<=sArr.length; row++) {
            for (int col=1; col<=tArr.length; col++) {
                if (sArr[row-1] == tArr[col-1]) {
                    num[row][col] = num[row-1][col] +  // delete 'row'th charater in s
                                    num[row-1][col-1]; // do not delete 'row'th character in s
                }
                else {
                    num[row][col] = num[row-1][col];
                }
            }
        }

        return num[sArr.length][tArr.length];
    }