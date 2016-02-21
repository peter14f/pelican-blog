277_find_the_celebrity
######################

:date: 2016-2-20 23:09
:tags: Graph, Directed Graphs
:category: LeetCode
:slug: 277_find_the_celebrity

`LeetCode Problem Link <https://leetcode.com/problems/find-the-celebrity/>`_

Original thought was to use a 2D matrix to save the result of knows(i, j).

Didn't realize that I was essentially building the adjacency matrix.

This take O(n \ :superscript:`2`) time and O(n \ :superscript:`2`) space and does pass OJ.

.. code-block:: java

    public int findCelebrity(int n) {

        // 0 = haven't asked
        // 1 = knows
        // 2 = don't know
        int[][] rowKnowsCol = new int[n][n];

        for (int i=0; i<n; i++) {
            // do people know i?

            int num = 0;

            for (int j=0; j<n; j++) {
                if (j==i)
                    continue;

                if (rowKnowsCol[j][i] == 0)
                    rowKnowsCol[j][i] = knows(j, i) ? 1: 2;

                if (rowKnowsCol[j][i] == 1)
                    num++;
                else
                    break;

            }

            if (num == n-1) {
                // i is potentially a celebrity - known by everyone else

                // number of people i knows
                int numPpl = 0;

                for (int j=0; j<n; j++) {
                    if (j==i)
                        continue;

                    if (rowKnowsCol[i][j] == 0)
                        rowKnowsCol[i][j] = (knows(i, j)) ? 1 : 2;

                    if (rowKnowsCol[i][j] == 1){
                        numPpl++;
                        break;
                    }
                }

                if (numPpl == 0)
                    return i;
            }
        }

        // return -1 if no celebrity found
        return -1;
    }

If you think of this problem as a graph problem. Then each person is a vertex. The celebrity will have
in-degree of ``n-1`` and an out-degree of ``0``. This is better than my 1st attempt because we just need
a list of size ``n`` for in-degrees and a list of size ``n`` for out-degrees.
That's O(n) space and O(n \ :superscript:`2`) time.

.. code-block:: java

   public int findCelebrity(int n) {

        int[] indegrees = new int[n];
        int[] outdegrees = new int[n];

        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {

                if (knows(i, j)) {
                    indegrees[j]++;
                    outdegrees[i]++;
                }

                if (knows(j, i)) {
                    indegrees[i]++;
                    outdegrees[j]++;
                }
            }
        }

        for (int i=0; i<n; i++) {
            if (outdegrees[i] == 0 && indegrees[i] == n-1)
                return i;
        }

        return -1;
    }

There is even a O(n) time and O(1) space solution.

.. code-block:: java

    public int findCelebrity(int n) {
        if (n <= 1) {
            return -1;
        }

        // step 1: find potential candidate
        int l = 0;
        int h = n - 1;

        while (l < h) {
            if (knows(l, h))
                l++;
            else
                h--;
        }

        // h and l are the same number now

        // step 2: verify the candidate is a celebrity

        for (int i=0; i<n; i++) {
            if (i==h)
                continue;

            if (!knows(i, h) || knows(h, i)) {
                // somebody doesn't know me OR
                // I know somebody
                return -1;
            }
        }

        return h;
    }

