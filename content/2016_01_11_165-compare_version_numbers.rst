165-compare_version_numbers
###########################

:date: 2016-1-11 17:39
:tags:
:category:
:slug: 165-compare_version_numbers

`LeetCode Problem Link <https://leetcode.com/problems/compare-version-numbers/>`_

Use two pointers ``i`` and ``j``, one to traverse ``version1`` and the other to traverse ``version2``.

If the the index has reached the end of the string, use zero as the subversion number.

This takes O(n) time where ``n`` is the length of the longer input string.

.. code-block:: java

    public int compareVersion(String version1, String version2) {
        int i=0;
        int j=0;

        while (i < version1.length() || j < version2.length()) {

            int v1 = 0;

            while (i < version1.length()) {
                char c = version1.charAt(i);
                i++;

                if (c == '.')
                    break;

                v1 = v1*10 + (int)(c-'0');
            }

            int v2 = 0;

            while (j < version2.length()) {
                char c = version2.charAt(j);
                j++;

                if (c == '.')
                    break;

                v2 = v2*10 + (int)(c-'0');
            }

            if (v1 > v2)
                return 1;
            else if (v2 > v1)
                return -1;
        }

        return 0;
    }