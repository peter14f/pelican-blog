312-burst_balloons
##################

:date: 2016-2-25 15:07
:tags:
:category: LeetCode
:slug: 312-burst_balloons
:status: draft

`LeetCode Problem Link <https://leetcode.com/problems/burst-balloons/>`_

pad a ``1`` in the front and back of ``nums``.

::

    int[] numbers = new int[n+2];

Now dp[left][right] is defined as the maximum coins when we burst all balloons
between ``left`` and ``right`` (but not including balloons at ``left`` and ``right``).

For example, if the input array is [3, 1, 5, 8], then
``numbers = [1, 3, 1, 5, 8, 1]``
and we want to return  ``dp[0][5]``.




