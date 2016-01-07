158-read_n_characters_given_read4_ii
####################################

:date: 2016-1-6 21:58
:tags: read4
:category: LeetCode
:slug: 158-read_n_characters_given_read4_ii

`LeetCode Problem Link <https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/>`_

Use a queue to store store the characters read using ``read4``.

.. code-block:: java

    public class Solution extends Reader4 {
        Queue<Character> q;

        public Solution() {
            this.q = new LinkedList<Character>();
        }
        /**
         * @param buf Destination buffer
         * @param n   Maximum number of characters to read
         * @return    The number of characters read
         */
        public int read(char[] buf, int n) {
            char[] temp = new char[4];
            int numWritten = 0; // number of chars written into buf
            boolean done = false;

            while (numWritten < n) {
                if (q.isEmpty()) {
                    int k = read4(temp);

                    if (k < 4)
                        done = true;

                    for (int i=0; i<k; i++) {
                        this.q.offer(temp[i]);
                    }
                }

                while (numWritten < n && !q.isEmpty()) {
                    buf[numWritten] = q.poll();
                    numWritten++;
                }

                if (done)
                    break;
            }

            return numWritten;
        }
    }