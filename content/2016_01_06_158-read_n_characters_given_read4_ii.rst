158-read_n_characters_given_read4_ii
####################################

:date: 2016-1-6 21:58
:tags: read4
:category: LeetCode
:slug: 158-read_n_characters_given_read4_ii

`LeetCode Problem Link <https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/>`_



.. code-block:: java

    /* The read4 API is defined in the parent class Reader4.
          int read4(char[] buf); */

    public class Solution extends Reader4 {

        char[] buffer;
        int cnt;

        public Solution() {
            buffer = new char[4];
            cnt = 0;
        }
        /**
         * @param buf Destination buffer
         * @param n   Maximum number of characters to read
         * @return    The number of characters read
         */
        public int read(char[] buf, int n) {
            int numLeft = n;
            int tot = 0;
            boolean done = false;
            int z=0;

            while (numLeft > 0) {
                if (cnt==0) {
                    cnt = read4(this.buffer);
                    if (cnt < 4)
                        done = true;
                }

                if (cnt > numLeft) {
                    int i=0;
                    int k = numLeft;
                    for (; i<k; i++) {
                        buf[z] = buffer[i];
                        tot++;
                        numLeft--;
                        cnt--;
                        z++;
                    }

                    if (i < 4) {
                        for (int j=0; j<cnt; j++) {
                            buffer[j] = buffer[i];
                            i++;
                        }
                    }
                }
                else {
                    int k = cnt;
                    for (int i=0; i<k; i++) {
                        buf[z] = buffer[i];
                        tot++;
                        numLeft--;
                        cnt--;
                        z++;
                    }
                }
                if (done)
                    break;
            }

            return tot;
        }
    }