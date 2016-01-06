157-read_n_characters_given_read4
#################################

:date: 2016-1-6 21:49
:tags: read4
:category: LeetCode
:slug: 157-read_n_characters_given_read4

`LeetCode Problem Link <https://leetcode.com/problems/read-n-characters-given-read4/>`_

Since in each test ``read()`` is called only once, we don't have to keep states.

.. code-block:: java

    public int read(char[] buf, int n) {
        int numWritten = 0; // number of chars written into buffer
        char[] temp = new char[4];

        while (numWritten < n) {
            int r = read4(temp);

            for (int i=0; i<r; i++) {
                if (numWritten >= n)
                    break;

                buf[numWritten] = temp[i];
                numWritten++;
            }

            if (r < 4) {
                break;
            }
        }

        return numWritten;
    }