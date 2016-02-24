300-longest_increasing_subsequence
##################################

:date: 2016-2-23 12:47
:tags: Subsequence, Dynamic Programming, Memoization
:category: LeetCode
:slug: 300-longest_increasing_subsequence

`LeetCode Problem Link <https://leetcode.com/problems/longest-increasing-subsequence/>`_

Input array is not sorted. We need to return the length of the longest subsequence.

Got to remember that the definition of a subsequence is the remaining numbers in the array when some elements of
the array is taken out.

At the beginning, I thought the straightforward solution is to start looking for a increasing subsequence from each
element. But this won't actually be O(n \ :superscript:`2`) time. Since ith element could either be in the subsequence
or not be in the subsequence. This is exponential time. One way would be to generate all possible subsequence and check
each of them is the elements are strictly increasing.

But we can achieve O(n \ :superscript:`2`) time using dynamic programming. Let's define a int array of size ``n+1``
called ``lenSubseqEnding``.

``lenSubseqEnding[i]`` is the length of th longest subsequence ending with the ith number.

::

    i=1 the 1st number in ``nums`` (nums[0])
    i=2 the 2nd number in ``nums`` (nums[1])
    ...

So how do fill out ``lenSubseqEnding[i]`` given that the entries at index smaller than ``i`` are all filled out?

we have to check the longest length of subsequence ending at all characters j < i and if the ith number is greater than
the jth number, then ``lenSubseqEnding[j] + 1`` could be potentially the longest length of subsequence ending at ith
character because we can append ith character to the subsequence ending at jth character.

.. code-block:: java

    public int lengthOfLIS(int[] nums) {
        int n = nums.length;

        if (n==0)
            return 0;

        /* here ith character
         *
         * i=1 -> 1st number -> nums[0]
         * i=2 -> 2nd number -> nums[1]
         *
         * length of the longest subsequence ending with ith character
         *
         */
        int[] lenSubseqEnding = new int[n+1];

        lenSubseqEnding[0] = 0;
        lenSubseqEnding[1] = 1;

        for (int i=2; i<=n; i++) {
            // initialize to 1 since in the worst case the subsequence
            // contains the ith character only
            lenSubseqEnding[i] = 1;

            for (int j=1; j<i; j++) {
                if (nums[i-1] > nums[j-1]) {
                    lenSubseqEnding[i] = Math.max(lenSubseqEnding[i], lenSubseqEnding[j] + 1);
                }
                // else ith number not larger than jth number,
                // cannot append ith num to this subsequence
            }
        }

        int ans = 0;

        for (int i=1; i<=n; i++) {
            ans = Math.max(ans, lenSubseqEnding[i]);
        }

        return ans;
    }
