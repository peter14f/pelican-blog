088-merge_sorted_array
######################

:date: 2015-11-15 17:49
:tags:
:category: LeetCode
:slug: 088-merge_sorted_array

`LeetCode Problem Link <https://leetcode.com/problems/merge-sorted-array/>`_

``num1`` actually has ``n`` slots after the first ``m`` elements. We must insert from the end, so that we
don't lose the elements in ``num1``.

.. code-block:: java

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m-1;
        int p2 = n-1;
        int i = m+n-1;

        while (p1 >= 0 && p2 >= 0) {

            if (nums1[p1] >= nums2[p2]) {
                nums1[i] = nums1[p1];
                p1--;
            }
            else {
                nums1[i] = nums2[p2];
                p2--;
            }
            i--;
        }

        // done inserting elements from array2
        if (p1 >= 0)
            return;

        // done inserting elements from array1
        while (i >= 0) {
            nums1[i] = nums2[p2];
            p2--;
            i--;
        }
    }
