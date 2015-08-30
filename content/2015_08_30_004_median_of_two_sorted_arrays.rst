004 Median of Two Sorted Arrays
###############################

:date: 2015-8-30 13:58
:tags: Sorted Arrays
:category: LeetCode
:slug: 004_median_of_two_sorted_arrays


`LeetCode Problem Link <https://leetcode.com/problems/median-of-two-sorted-arrays/>`_

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



