152-maximum_product_subarray
############################

:date: 2016-1-3 12:30
:tags: Subarray, Memoization
:category: LeetCode
:slug: 152-maximum_product_subarray

`LeetCode Problem Link <https://leetcode.com/problems/maximum-product-subarray/>`_

The straightforward solution takes O(n :superscript:`2`) time, but will get you TLE on large
test case.

.. code-block:: java

    public int maxProduct(int[] nums) {

        int n = nums.length;
        int max = nums[0];

        for (int i=0; i<n; i++) {
            int product = nums[i];
            max = Math.max(max, product);

            for (int j=i+1; j<n; j++) {
                product = product * nums[j];
                max = Math.max(max, product);
            }
        }

        return max;
    }

We will use two arrays of size ``n`` called ``minProduct`` and ``maxProduct``.

``minProduct[i]`` is the smallest product some contiguous elements from element ``0`` to element ``i`` can form with
the ith element included.
``maxProduct`` is the largest product some contiguous elements from element ``0`` to element ``i`` can form with the
ith element included.

Initialize ``minProduct[0]`` and ``maxProduct[0]`` to ``nums[0]``.  Try to fill both arrays starting from index 1.
``minProduct[i] = min(minProduct[i-1]*nums[i], nums[i], maxProduct[i-1]*nums[i])`` and
``maxProduct[i] = max(minProduct[i-1]*nums[i], nums[i], maxProduct[i-1]*nums[i])``.

The largest element in ``maxProduct`` is the answer.

.. code-block:: java

    /* the array may contain 0
     * the array may contain negative numbers
     */
    public int maxProduct(int[] nums) {
        if (nums==null || nums.length < 1)
            return 0;

        int max = nums[0];


        int[] maxProduct = new int[nums.length];
        int[] minProduct = new int[nums.length];

        /* maxProduct[i] is the largest product of some contiguous elements from [0, i]
         * with the ith element included.
         *
         * minProduct[i] is the smallest product of some contiguous elements from [0, i]
         * with the ith element included.
         */

        maxProduct[0] = nums[0];
        minProduct[0] = nums[0];

        for (int i=1; i<nums.length; i++) {
            maxProduct[i] = Math.max(nums[i], Math.max(maxProduct[i-1]*nums[i], minProduct[i-1]*nums[i]));
            minProduct[i] = Math.min(nums[i], Math.min(maxProduct[i-1]*nums[i], minProduct[i-1]*nums[i]));

            if (maxProduct[i] > max)
                max = maxProduct[i];
        }

        return max;
    }