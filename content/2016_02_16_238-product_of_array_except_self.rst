238-product_of_array_except_self
################################

:date: 2016-2-16 0:01
:tags: Math
:category: LeetCode
:slug: 238-product_of_array_except_self

`LeetCode Problem Link <https://leetcode.com/problems/product-of-array-except-self/>`_

Here is the straightforward O(n\ :superscript:`2`) time solution. Well, the problem statement already asks us
to do it in O(n) time, so this obviously will get us TLE.

.. code-block:: java

    public int[] productExceptSelf(int[] nums) {
        if (nums.length == 0)
            return nums;

        int[] output = new int[nums.length];

        for (int i=0; i<output.length; i++) {
            int p = 1;
            for (int j=0; j<nums.length; j++) {
                if (i==j)
                    continue;
                p = p*nums[j];
            }
            output[i] = p;
        }

        return output;
    }

The O(n) solution involves allocating two more int[] of the same size named ``forward`` and ``backward``. Let's look at the example where the input
array ``nums`` has 4 elements: ``[a1, a2, a3, a4]``.

``forward = [1, a1, a1 x a2, a1 x a2 x a3]``
``backward = [a2 x a3 x a4, a3 x a4, a4, 1]``
``output = [a2 x a3 x a4, a1 x a3 x a4, a1 x a2 x a4, a1 x a2 x a3]``

Multiplying forward[i] with backward[i] will get us output[i].

This is the O(n) time and O(n) space solution.

.. code-block:: java

    public int[] productExceptSelf(int[] nums) {
        if (nums.length == 0)
            return nums;
        int n = nums.length;
        // output array does not count toward memory constraint
        int[] output = new int[n];

        int[] forward = new int[n];
        int[] backward = new int[n];

        forward[0] = 1;
        backward[n-1] = 1;

        for (int i=1; i<n; i++) {
            forward[i] = forward[i-1] * nums[i-1];
            backward[n-1-i] = backward[n-i] * nums[n-i];
        }

        for (int i=0; i<n; i++) {
            output[i] = forward[i] * backward[i];
        }

        return output;
    }

The follow-up problem is do this in O(1) space and O(n) time.
Let's utilize the ``output`` array that does not count toward the memory constraint and a int variable ``p``.

.. code-block:: java

    public int[] productExceptSelf(int[] nums) {
        if (nums.length == 0)
            return nums;
        int n = nums.length;
        // output array does not count toward memory constraint
        int[] output = new int[n];

        output[0] = 1;
        // going forward
        for (int i=1; i<n; i++) {
            output[i] = output[i-1] * nums[i-1];
        }

        int p = 1;
        output[n-1] = p * output[n-1];

        for (int i=n-2; i>=0; i--) {
            p = p*nums[i+1];
            output[i] = p * output[i];
        }

        return output;
    }

This is finally O(n) time and O(1) space!
