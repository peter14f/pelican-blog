087-scramble_string
###################

:date: 2015-11-13 15:34
:tags: Recursion, Dynamic Programming, String Partitions, 3D space DP
:category: LeetCode
:slug: 087-scramble_string

`LeetCode Problem Link <https://leetcode.com/problems/scramble-string/>`_

If ``s2`` is a scrambled version of ``s1``, there must exist a way to partition s1 and s2 such that
(isScramble(s11, s21) is True and isScramble(s12, s22) is True) OR (isScramble(s11, s22) is True and
is Scramble(s12, s21) is True).

The check is therefore recursive. The base case is when both input strings are of length 1. In the base case,
we simply check if the one character in s1 matches the one character in s2.

When taking this recursive approach, we must add checks to prevent the unneeded recursive calls. The checks we have is

    1. if the lengths don't match, return false
    2. if the lengths match, the characters must appear the same number of times in ``s1`` as they do in ``s2``

.. code-block:: java

    public boolean isScramble(String s1, String s2) {

        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();

        return isScramble(arr1, 0, arr1.length - 1,
                          arr2, 0, arr2.length - 1);
    }

    private boolean isScramble(char[] arr1, int start1, int end1,
                               char[] arr2, int start2, int end2) {

        int len1 = end1 - start1 + 1;
        int len2 = end2 - start2 + 1;

        if (len1 != len2)
            return false;

        if (len1 == 1) {
            return arr1[start1] == arr2[start2];
        }

        boolean charactersMatch = true;
        HashMap<Character, Integer> cnt = new HashMap<Character, Integer>();
        for (int i=start1; i<=end1; i++) {
            if (cnt.containsKey(arr1[i]))
                cnt.put(arr1[i], cnt.get(arr1[i]) + 1);
            else
                cnt.put(arr1[i], 1);
        }

        for (int i=start2; i<=end2; i++) {
            if (!cnt.containsKey(arr2[i])) {
                charactersMatch = false;
                break;
            }
            else {
                if (cnt.get(arr2[i])==1)
                    cnt.remove(arr2[i]);
                else
                    cnt.put(arr2[i], cnt.get(arr2[i])-1);
            }
        }

        if (!cnt.isEmpty())
            charactersMatch = false;

        if (!charactersMatch)
            return false;

        for (int cut1=start1; cut1 < end1; cut1++) {
            int s11Len = cut1 - start1 + 1;

            for (int cut2=start2; cut2 < end2; cut2++) {
                int s21Len = cut2 - start2 + 1;
                int s22Len = end2 - cut2;

                boolean check1 = false;
                if (s11Len == s21Len) {
                    check1 = isScramble(arr1, start1, cut1, arr2, start2, cut2) &&
                             isScramble(arr1, cut1+1, end1, arr2, cut2+1, end2);
                }
                if (check1)
                    return true;

                boolean check2 = false;

                if (s11Len == s22Len) {
                    check2 = isScramble(arr1, start1, cut1, arr2, cut2+1, end2) &&
                             isScramble(arr1, cut1+1, end1, arr2, start2, cut2);
                }

                if (check2)
                    return true;
            }
        }

        return false;
    }

There is also a DP solution. We will use a 3D boolean array called ``result``.
result[a][b][c] is true if the substrings of length ``a`` starting at index ``b`` in ``s1`` and starting at
index ``c`` in ``s2`` are scrambes of one another.

Let ``L`` be the length of ``s1`` and ``s2``. ``results`` is initialized with size ``L+1``, ``L``, and ``L``.
We will fill ``result[1][i][j]`` for i and j first. Note that substrings of length 1 can only be scrambles of
one another if the two strings have the same character.

And then we will fill each plane from k=2 to k=L. Finally we return ``result[L][0][0]``.

In the most inner loop, ``m`` is simply the length of the left partitioned substring. ``k-m`` would then
be the length of the right partitioned substring.

.. code-block:: java

    public boolean isScramble(String s1, String s2) {

        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();

        if (arr1.length != arr2.length)
            return false;

        int L = arr1.length;
        boolean result[][][] = new boolean[L+1][L][L];

        // k=1 strings of length 1
        for (int i=L-1; i >=0; i--) {
            for (int j=L-1; j>=0; j--) {
                if (arr1[i] == arr2[j])
                    result[1][i][j] = true;
            }
        }

        // work from strings of length 2 all the way to strings of length L
        for (int k=2; k<=L; k++) {

            for (int i=L-k; i>=0; i--) {
                for (int j=L-k; j>=0; j--) {

                    boolean r = false;
                    // k is the length of the whole substring in question
                    // m is the length of the left partitioned string
                    // k-m is the length of the right partitioned string
                    for (int m=1; m<k; m++) {

                        r = (result[m][i][j] && result[k-m][i+m][j+m]) ||
                            (result[m][i][j+k-m] && result[k-m][i+k-m][j]);

                        if (r) {
                            // already found one way to partition the substrings of length k
                            // such that they are scrambles of one another
                            result[k][i][j] = r;
                            break;
                        }
                    }

                }
            }
        }

        return result[L][0][0];
    }

The time complexity is O(n\ :superscript:`4`). The space complexity is O(n\ :superscript:`3`).