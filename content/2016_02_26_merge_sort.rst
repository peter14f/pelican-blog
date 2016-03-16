merge_sort
##########

:date: 2016-2-26 15:00
:tags: Merge Sort, Sorting
:category:
:slug: merge_sort

`Merge Sort Java Implementation Discussion Link
<http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/7-Sort/merge-sort4.html>`_

While solving 315-count_of_smaller_number_after_self, I realized I was very unfamiliar the usual way of implementing
merge sort in Java. So I am going to show 3 different versions here and the last one is the *usual* way to
do it in Java.

Version 1 (Most naive and easiest to remember)

Each time you split the input array in halves, you allocate two arrays.
This is the most straightforward way since the ``merge()`` method takes
3 different arrays. We're trying to merge array ``left`` with array ``right``,
the merged result is stored by into ``nums``.

.. code-block:: java

    // this is the naive recursive top-down mergesort implementation
    // that makes many memory allocation calls (i.e., new int[])
    private static void mergeSort(int[] nums) {
        int n = nums.length;

        if (n==1) {
            // already sorted
            return;
        }

        int leftSize = n/2;
        int rightSize = n - leftSize;

        int[] left = new int[leftSize];
        int[] right = new int[rightSize];

        int k=0;

        for (int i=0; i < leftSize; i++) {
            left[i] = nums[k];
            k++;
        }

        for (int i=0; i < rightSize; i++) {
            right[i] = nums[k];
            k++;
        }

        mergeSort(left);
        mergeSort(right);
        merge(left, right, nums);
    }

    private static void merge(int[] left, int[] right, int[] nums) {
        int i=0, j=0, k=0;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                nums[k] = left[i];
                i++;
                k++;
            }
            else {
                nums[k] = right[j];
                j++;
                k++;
            }
        }

        while (i < left.length) {
            nums[k] = left[i];
            i++;
            k++;
        }

        while (j < right.length) {
            nums[k] = right[j];
            j++;
            k++;
        }
    }

Version 2 (Specify the range of the input arrays to sort)

A temporary array ``tmp`` is allocated each time ``merge()`` is called.
This version is actually fine if we can free the memory allocated for
``tmp`` right at the end of ``merge()`` (Say we implemeted this in C, for exmaple)

In Java, this is not good.

.. code-block:: java

    public void mergeSort(int[] nums) {
        mergeSort(nums, 0, nums.length-1);
    }

    private void mergeSort(int[] nums, int start, int end) {
        if (start == end) {
            // single element is already sorted
            return;
        }

        int middle = start + (end-start) / 2;

        mergeSort(nums, start, middle);
        mergeSort(nums, middle+1, end);

        merge(nums, start, middle+1, end);
    }

    private void merge(int[] nums, int leftBegin, int rightBegin, int rightEnd) {

        // nums[leftBegin], ..., nums[rightBegin-1] is sorted
        // nums[rightBeing], ...,  nums[rightEnd] is sorted

        int[] tmp = new int[nums.length];

        int i=leftBegin, j=rightBegin, k=leftBegin;

        // fill in tmp from leftBegin all the way to rightEnd

        while (i <= rightBegin-1 && j <= rightEnd) {
            if (nums[i] <= nums[j]) {
                tmp[k] = nums[i];
                i++;
                k++;
            }
            else {
                tmp[k] = nums[j];
                j++;
                k++;
            }
        }

        while (i <= rightBegin-1) {
            tmp[k] = nums[i];
            i++;
            k++;
        }

        while (j <= rightEnd) {
            tmp[k] = nums[j];
            j++;
            k++;
        }

        for (int x=leftBegin; x<=rightEnd; x++) {
            nums[x] = tmp[x];
        }
    }


Version 3. Allocate ``tmp`` once only.

Man just remember this version by heart, and you will be good.

.. code-block:: java

    public void mergeSort(int[] nums) {
        int[] tmp = new int[nums.length];
        mergeSort(nums, tmp, 0, tmp.length-1);
    }

    private void mergeSort(int[] nums, int[] tmp, int begin, int end) {

        if (begin == end) {
            // single element is already sorted
            return;
        }

        int middle = begin + (end-begin)/2;

        mergeSort(nums, tmp, begin, middle);
        mergeSort(nums, tmp, middle+1, end);
        merge(nums, tmp, begin, middle+1, end);
    }

    private void merge(int[] nums, int[] tmp, int leftBegin, int rightBegin, int rightEnd) {

        int i=leftBegin, j=rightBegin, k=leftBegin;

        while (i<=rightBegin-1 && j<=rightEnd) {
            if (nums[i] <= nums[j]) {
                tmp[k] = nums[i];
                i++;
                k++;
            }
            else {
                tmp[k] = nums[j];
                j++;
                k++;
            }
        }

        while (i<=rightBegin-1) {
            tmp[k] = nums[i];
            i++;
            k++;
        }

        while (j<=rightEnd) {
            tmp[k] = nums[j];
            j++;
            k++;
        }

        for (int z=leftBegin; z<=rightEnd; z++) {
            nums[z] = tmp[z];
        }
    }


