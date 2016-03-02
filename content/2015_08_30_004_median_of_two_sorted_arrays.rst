004 Median of Two Sorted Arrays
###############################

:date: 2015-8-30 13:58
:tags: Sorted Arrays, Merge Sort
:category: LeetCode
:slug: 004_median_of_two_sorted_arrays


`LeetCode Problem Link <https://leetcode.com/problems/median-of-two-sorted-arrays/>`_

Let's forget about the time constraint here. How would you approach the problem?

We can use a similar approach when we're doing a merge sort. Use two pointers ``i`` and ``j``.

``(i+j)`` is the number of times the pointers have been incremented.

And min(nums1[i], num2[j]) is the (i+j+1)th element.

::

    i=0, j=0 1st element is min(nums[i], nums[j])

.. code-block:: java

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        int n = nums1.length + nums2.length;

        // remember that k is 1-based number

        if (n%2 == 0) {
            // even
            int k = n/2;
            int[] nums = findKandKPlusOneElement(nums1, nums2, k);


            return (double)(nums[0]+nums[1])/2;
        }
        else {
            // odd
            return findKthElement(nums1, nums2, (n/2)+1);
        }
    }

    private int findKthElement(int[] nums1, int[] nums2, int k) {
        // k=1 the first element

        if (k < 1 || k > nums1.length + nums2.length)
            throw new IllegalArgumentException();

        int i=0, j=0;

        // (i + j) is the number of these counters have been incremented

        while (i+j < k-1) {
            if (i >= nums1.length) {
                j++;
            }
            else if (j >= nums2.length) {
                i++;
            }
            else {
                if (nums1[i] < nums2[j]) {
                    i++;
                }
                else {
                    j++;
                }
            }
        }

        // the smaller value gives you the (i+j)th element
        if (i >= nums1.length)
            return nums2[j];
        else if (j >= nums2.length)
            return nums1[i];
        else {
            if (nums1[i] <= nums2[j])
                return nums1[i];
            else
                return nums2[j];
        }
    }

    private int[] findKandKPlusOneElement(int[] nums1, int[] nums2, int k) {

        int[] ans = {0, 0};

        if (k+1 > nums1.length + nums2.length)
            throw new IllegalArgumentException();

        int i=0, j=0;

        // min(nums1[i], nums2[j]) is the (i+j+1)th number

        while (i+j < k-1) {
            if (i >= nums1.length)
                j++;
            else if (j >= nums2.hashCode())
                i++;
            else {
                if (nums1[i] <= nums2[j])
                    i++;
                else
                    j++;
            }
        }

        ans[0] = Math.min(nums1[i], nums2[j]);

        while (i+j < k) {
            if (i >= nums1.length)
                j++;
            else if (j >= nums2.hashCode())
                i++;
            else {
                if (nums1[i] <= nums2[j])
                    i++;
                else
                    j++;
            }
        }

        ans[1] = Math.min(nums1[i], nums2[j]);

        return ans;
    }

This is the O(k) solution.


We are asked to do this in O(log(``m+n``)) time where ``m`` is the size of the first
sorted array and ``n`` is the size of the second sorted array.

If ``(m+n)`` is odd, we need to find the ``(m+n)/2 + 1`` :superscript:`th` smallest
element.

Otherwise, we need to find ``(m+n)/2`` :superscript:`th` smallest element
and ``(m+n)/2 + 1`` :superscript:`th` smallest element and then take the mean.


Here is how we can get the ``K`` :superscript:`th` element of the union of two sorted arrays ``A`` and ``B``:

 Suppose we choose the a :superscript:`th` smallest element of array ``A``, **A[a-1]**,

 and the b :superscript:`th` smallest element of array ``B``, **B[b-1]**,
 such that ``a+b = K``.

 If ``A[a-1] == B[b-1]``, then A[a-1] is the ``K`` :superscript:`th` smallest element of the union of ``A`` and ``B``.

   We're done!

 If ``A[a-1] < B[b-1]``, then A[a-1] is the ``a`` :superscript:`th` smallest element of the union of ``A`` and ``B``.

   Numbers in A with a index <= ``a-1`` can be discarded

   Numbers in B with a index > ``b`` can also be discard

   We won't find the ``K`` :superscript:`th` smallest element here in these two regions

 If ``A[a-1] > B[b-1]``, then B[b-1] is the ``b`` :superscript:`th` smallest element of the union of ``A`` and ``B``.

   Number is A with a index > ``a`` can be discarded

   Numbers in B with a index <= ``b-1`` can be discarded

   We won't find the ``K`` :superscript:`th` smallest element here in these two regions


The problem is how we choose ``a`` and ``b``.

Here's one way we could do it, try to cover the small array while making sure the the other array
has at least 1 element covered.


::


        if (aSize <= bSize) {
            a = aSize;
            b = k - a;

            if (b==0) {
                b++;
                a--;
            }
        }
        else {
            b = bSize;
            a = k-b;

            if (a==0) {
                a++;
                b--;
            }
        }


