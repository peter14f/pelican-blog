014-longest_common_prefix
#########################

:date: 2015-09-07 20:16
:tags: Common Prefix
:category: LeetCode
:slug: 014-longest_common_prefix

`LeetCode Problem Link <https://leetcode.com/problems/longest-common-prefix/>`_

Find the shortest string in ``strs`` first.

.. code-block:: java

    public String longestCommonPrefix(String[] strs) {

        if (strs==null || strs.length==0) {
            return "";
        }

        int minLength = strs[0].length();
        int minLengthIndex = 0;

        for (int i=1; i<strs.length; i++) {
            if (strs[i].length() < minLength) {
                minLength = strs[i].length();
                minLengthIndex = i;
            }
        }

        char[] shortest = strs[minLengthIndex].toCharArray();
        boolean done = false;
        int i;
        for (i=0; i<minLength; i++) {
            for (int j=0; j<strs.length; j++) {

                if (j==minLengthIndex)
                    continue;

                if (strs[j].charAt(i) != shortest[i]) {
                    done = true;
                    break;
                }
            }
            if (done)
                break;
        }

        return strs[minLengthIndex].substring(0, i);
    }