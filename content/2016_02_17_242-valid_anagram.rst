242-valid_anagram
#################

:date: 2016-2-17 0:58
:tags: Anagrams
:category: LeetCode
:slug: 242-valid_anagram

`LeetCode Problem Link <https://leetcode.com/problems/valid-anagram/>`_

Compare the sorted versions of ``s`` and ``t`` would do.

.. code-block:: java

    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length())
            return false;

        char[] sArr = s.toCharArray();
        Arrays.sort(sArr);
        char[] tArr = t.toCharArray();
        Arrays.sort(tArr);

        for (int i=0; i<sArr.length; i++) {
            if (sArr[i] != tArr[i])
                return false;
        }

        return true;
    }
