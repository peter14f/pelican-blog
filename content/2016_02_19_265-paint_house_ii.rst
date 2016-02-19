265-paint_house_ii
##################

:date: 2016-2-19 9:15
:tags: Paint House
:category: LeetCode
:slug: 265-paint_house_ii

`LeetCode Problem Link <https://leetcode.com/problems/paint-house-ii/>`_

The colors are not just Red, Green, and Blue anymore. This problem is a generalization of 256-paint_house.
The number colors is ``k``.

Given that we've done 256-paint_house. Getting the O(nk \ :superscript:`2`) time solution is pretty easy.

It actually passes OJ as well.

.. code-block:: java

    public int minCostII(int[][] costs) {
        int n = costs.length;

        if (n==0)
            return 0;

        int k = costs[0].length;

        if (k==0)
            return 0;

        /*  minCostWithColor[i][j] is the
         *    minimum total cost up to house i with the ith painted in color j
         *
         */
        int[][] minCostWithColor = new int[n][k];


        for (int j=0; j<k; j++) {
            minCostWithColor[0][j] = costs[0][j];
        }

        for (int i=1; i<n; i++) {
            for (int j=0; j<k; j++) {
                // you want to pain the ith house color j
                // then the previous house cannot be painted with color j
                int prevMin = Integer.MAX_VALUE;

                for (int p=0; p<k; p++) {
                    if (p==j)
                        continue;
                    if (minCostWithColor[i-1][p] < prevMin) {
                        prevMin = minCostWithColor[i-1][p];
                    }
                }

                minCostWithColor[i][j] = prevMin + costs[i][j];
            }
        }

        int minCost = Integer.MAX_VALUE;

        for (int j=0; j<k; j++) {
            if (minCostWithColor[n-1][j] < minCost) {
                minCost = minCostWithColor[n-1][j];
            }
        }

        return minCost;
    }


But we're asked if we could do in in ``O(nk)`` time. Notice that we need to get the minimum total cost up to
house ``(i-1)`` in a color that's different from the color we're using for house ``i``.

We can save the minimum cost as we fill out the array. But we also the 2nd minimum cost in the case when the
color is the same.

.. code-block:: java

                    int prevMin1 = Integer.MAX_VALUE;
                    int prevMin2 = Integer.MAX_VALUE;
                    int min1Index = -1;

                    if (costs[0][j] < prevMin1) {
                        prevMin2 = prevMin1;

                        prevMin1 = costs[0][j];
                        min1Index = j;
                    }
                    else if (costs[0][j] < prevMin2) {
                        prevMin2 = costs[0][j];
                    }


That we we don't need to loop for the costs up to the previous house each time we are trying to paint the current house.

.. code-block:: java

    public int minCostII(int[][] costs) {

        int n = costs.length;

        if (n==0)
            return 0;

        int k = costs[0].length;

        if (k==0)
            return 0;

        int[][] minCostWithColor = new int[n][k];

        int prevMin1 = Integer.MAX_VALUE;
        int prevMin2 = Integer.MAX_VALUE;

        int min1Index = -1;

        for (int j=0; j<k; j++) {
            minCostWithColor[0][j] = costs[0][j];

            if (costs[0][j] < prevMin1) {
                prevMin2 = prevMin1;

                prevMin1 = costs[0][j];
                min1Index = j;
            }
            else if (costs[0][j] < prevMin2) {
                prevMin2 = costs[0][j];
            }
        }

        for (int i=1; i<n; i++) {
            int newMin1 = Integer.MAX_VALUE;
            int newMin2 = Integer.MAX_VALUE;
            int newMin1Index = -1;

            for (int j=0; j<k; j++) {

                if (j!=min1Index) {
                    minCostWithColor[i][j] = prevMin1 + costs[i][j];
                }
                else {
                    minCostWithColor[i][j] = prevMin2 + costs[i][j];
                }

                if (minCostWithColor[i][j] < newMin1) {
                    newMin2 = newMin1;
                    newMin1 = minCostWithColor[i][j];
                    newMin1Index = j;
                }
                else if (minCostWithColor[i][j] < newMin2) {
                    newMin2 = minCostWithColor[i][j];
                }
            }

            prevMin1 = newMin1;
            prevMin2 = newMin2;
            min1Index = newMin1Index;
        }

        return prevMin1;
    }
