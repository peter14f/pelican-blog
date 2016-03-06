330-patching_array
##################

:date: 2016-2-28 14:55
:tags: Greedy
:category: LeetCode
:slug: 330-patching_array

`LeetCode Problem Link <https://leetcode.com/problems/patching-array/>`_

Let ``[0, miss)`` be the range of integers that's currently covered. Then ``miss`` should be
initialized to ``1``.

If the next number in the input array ``nums[i]`` is ``<= miss``, then no patch is needed, and we
can increase ``miss`` to ``miss + nums[i]``.

Else, we must cover ``miss`` by adding ``1 patch``. We should be greedy and choose ``miss`` as the
added number and that will expand the range covered to ``[0, miss+miss)``.

.. code-block:: java

    public int minPatches(int[] nums, int n) {

        // integers in range [0, miss) is covered
        long miss = 1;

        int i = 0;
        int numPatches = 0;

        while (miss <= n) {
            if (i < nums.length && nums[i]<=miss) {
                miss += nums[i];
                i++;
            }
            else {
                miss = miss + miss;
                numPatches++;
            }
        }

        return numPatches;
    }

Note that ``miss`` is of type **long** to avoid overflow.