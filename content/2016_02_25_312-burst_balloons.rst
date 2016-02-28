312-burst_balloons
##################

:date: 2016-2-25 15:07
:tags:
:category: LeetCode
:slug: 312-burst_balloons

`LeetCode Problem Link <https://leetcode.com/problems/burst-balloons/>`_

pad a ``1`` in the front and back of ``nums``.

::

    int[] numbers = new int[n+2];

Now dp[left][right] is defined as the maximum coins when we burst all balloons
between ``left`` and ``right`` (but not including balloons at ``left`` and ``right``).

For example, if the input array is [3, 1, 5, 8], then
``numbers = [1, 3, 1, 5, 8, 1]``
and we want to return  ``dp[0][5]``.

dp[0][2] = numbers[0]*numbers[1]*numbers[2]
dp[1][3] = numbers[1]*numbers[2]*numbers[3]
dp[2][4] = numbers[2]*numbers[3]*numbers[4]
dp[3][5] = numbers[3]*numbers[4]*numbers[5]

Fill these entries first (when there is only one choice of balloon to burst)

then consider ``l=2`` (when there are two choices of balloons to burst)

The two choices are ``start`` and ``start+l-1``

``left = start-1``
``right = start+l``
and we will be filling in ``dp[left][right]``

You must consider the max coins if ``start`` is bursted last and the max coins if ``start+l-1`` is bursted last.

.. code-block:: java

    public static int maxCoins(int[] nums) {

        int[] numbers = new int[nums.length + 2];
        int n = numbers.length;
        numbers[0] = 1;
        numbers[n-1] = 1;

        for (int i=1; i<=nums.length; i++)
            numbers[i] = nums[i-1];

        int[][] dp = new int[n][n];

        // start is the leftmost choice when we consider 1 choice
        for (int start=1; start<=nums.length; start++) {
            dp[start-1][start+1] = numbers[start-1]*numbers[start]*numbers[start+1];
        }


        // think of l as the number of choices
        for (int l=2; l<=nums.length; l++) {

            // start is the leftmost choice when we consider l choicess
            for (int start=1; start<=nums.length; start++) {

                int left = start-1;
                int right = start+l;

                if (right >= n) {
                    // cannot write to dp[left][right]
                    continue;
                }

                int max = 0;

                // k is the last balloon to burst, again given l choices starting at start
                for (int k=start; k<start+l; k++) {

                    int lastBurstCredits = numbers[left]*numbers[k]*numbers[right];

                    int leftMostCredits = 0;

                    if (k-1 > left) {
                        leftMostCredits = dp[left][k];
                    }

                    int rightMostCredits = 0;

                    if (k+1 < right) {
                        rightMostCredits=dp[k][right];
                    }

                    int totalCredits = lastBurstCredits + leftMostCredits + rightMostCredits;

                    max = Math.max(max, totalCredits);
                }

                dp[left][right] = max;
            }

        }

        // System.out.println(Arrays.deepToString(dp));

        return dp[0][n-1];
    }

This is O(n \ :superscript:`3`) time solution where ``n`` is the length of the original input array, which is
also the number of balloons.
