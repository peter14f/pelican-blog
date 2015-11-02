070-climbing_stairs
###################

:date: 2015-11-2 13:08
:tags: Dynamic Programming
:category: LeetCode
:slug: 070-climbing_stairs

`LeetCode Problem Link <https://leetcode.com/problems/climbing-stairs/>`_

Create an int array of size ``n+1`` and call it ``waysToStep``.

| ``waysToStep[0]`` refers to the number of ways to reach the ground level.
| ``waysToStep[1]`` refers to the number of ways to reach the step 1.
| ...
| ``waysToStep[n]`` refers to the number of ways to reach the step n.

.. code-block:: java

    public int climbStairs(int n) {

        int[] waysToReachStep = new int[n+1];

        if (n < 1)
            throw new IllegalArgumentException();

        waysToReachStep[0] = 1; // ground
        waysToReachStep[1] = 1; // take one step from ground
        // [2]: take 2 steps from ground
        //      take 1 step to Step 1, take 1 step to Step 2

        for (int i=2; i<=n; i++) {
            waysToReachStep[i] = waysToReachStep[i-1] + waysToReachStep[i-2];
        }

        return waysToReachStep[n];
    }