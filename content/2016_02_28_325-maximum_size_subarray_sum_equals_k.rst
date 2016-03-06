325-maximum_size_subarray_sum_equals_k
######################################

:date: 2016-2-28 7:32
:tags: Range Sum
:category: LeetCode
:slug: 325-maximum_size_subarray_sum_equals_k

`LeetCode Problem Link <https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/>`_

The straightforward solution is to use two nested for loops to find the sums of all subarrays.

.. code-block:: java

    public int maxSubArrayLen(int[] nums, int k) {
        int n = nums.length;
        int maxSize = 0;

        for (int i=0; i<n; i++) {
            int sum = nums[i];

            if (sum == k && 1 > maxSize)
                maxSize = 1;

            for (int j=i+1; j<n; j++) {
                sum = sum + nums[j];

                if (sum == k && (j-i+1) > maxSize) {
                    maxSize = j-i+1;
                }

            }
        }

        return maxSize;
    }

The followup wants us to do this in O(n) time.

After looking at the solution online, I just realized that any problem dealing with **Range Sum** probably
has something to do with prefix sum.

::

    rangeSum(i, j) = prefixSum[j] - prefixSum[i-1]

    think of prefixSum[-1] = 0

    we are looking for all i's that satisfy

    k = prefixSum[j] - prefixSum[i-1]

    and we will return the biggest (j-i+1) found

We can use a HashMap<Integer, List<Integer>> where the key is prefixSum[i-1] and the values are the (i-1)

.. code-block:: java

    public int maxSubArrayLen(int[] nums, int k) {
        int[] prefixSum = new int[nums.length];
        HashMap<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>();
        int maxSize = 0;

        for (int i=0; i<prefixSum.length; i++) {
            if (i==0)
                prefixSum[i] = nums[i];
            else
                prefixSum[i] = prefixSum[i-1] + nums[i];

            if (!map.containsKey(prefixSum[i]))
                map.put(prefixSum[i], new ArrayList<Integer>());

            map.get(prefixSum[i]).add(i);
        }

        //System.out.println(map);

        for (int j=0; j<nums.length; j++) {

            int target = prefixSum[j] - k;

            if (target==0) {
                if (j + 1 > maxSize)
                    maxSize = j+1;
            }

            //System.out.println("j=" + j + " t=" + target);

            if (map.containsKey(target)) {
                List<Integer> prevI = map.get(target);

                for (int iMinusOne: prevI) {

                    //System.out.println(" iMinus1=" + iMinusOne + " i=" + (iMinusOne+1));

                    int i = iMinusOne + 1;
                    if (i > j)
                        continue;

                    if (j-i+1 > maxSize)
                        maxSize = j-i+1;
                }
            }
        }

        return maxSize;
    }

So this is the O(n) time and O(n) space solution.