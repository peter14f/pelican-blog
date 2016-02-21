278-first_bad_version
#####################

:date: 2016-2-20 23:43
:tags: Binary Search
:category: LeetCode
:slug: 278-first_bad_version

`LeetCode Problem Link <https://leetcode.com/problems/first-bad-version/>`_

There are ``n`` versions labeled from ``1`` to ``n``.

O(n) solution would be to try call isBadVersion() for 0, 1, 2, ... .

The O(logn) solution uses binary search.

.. code-block:: java

    public int firstBadVersion(int n) {
        int l = 1;
        int h = n;

        int minFound = n;

        while (l <= h) {
            int m = l + (h-l)/2;

            boolean bad = isBadVersion(m);

            if (bad) {
                minFound = Math.min(minFound, m);
                // could have a lower bad version
                h = m - 1;
            }
            else {
                // could have a higher bad version
                l = m + 1;
            }
        }

        return minFound;
    }
