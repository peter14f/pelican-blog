058-length_of_last_word
#######################

:date: 2015-10-26 17:24
:tags:
:category: LeetCode
:slug: 058-length_of_last_word

`LeetCode Problem Link <https://leetcode.com/problems/length-of-last-word/>`_

Ignore the trailing spaces. This is how the ``split()`` String method works anyways.

It turns out that I only had to check for spaces, not tabs or other weird characters.

.. code-block:: java

    public int lengthOfLastWord(String s) {
        char[] s_arr = s.toCharArray();
        int cnt = 0;

        int i = s_arr.length - 1;

        if (s_arr.length==0)
            return cnt;

        while (s_arr[i] == ' ') {
            i--;
            if (i < 0)
                break;
        }

        while (i>=0) {
            if (s_arr[i]==' ') {
                break;
            }
            else {
                cnt++;
            }

            i--;
        }

        return cnt;
    }