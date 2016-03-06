327-count_of_range_sum
######################

:date: 2016-2-28 9:46
:tags: Merge Sort, Divide And Conquer
:category: LeetCode
:slug: 327-count_of_range_sum

`LeetCode Problem Link <https://leetcode.com/problems/maximum-product-subarray/>`_

.. code-block:: java

    public int countRangeSum(int[] nums, int lower, int upper) {
        int n = nums.length;

        int count = 0;

        for (int i=0; i<n; i++) {
            int curSum = nums[i];

            if (curSum >= lower && curSum <= upper)
                count++;

            for (int j=i+1; j<n; j++) {
                curSum += nums[j];

                if (curSum >= lower && curSum <= upper)
                    count++;
            }
        }

        return count;
    }

This is the trivial O(n :superscript:`2`) time solution that does not check for overflow

Here is the divide and conquer count in the merge step or merge sort.

It takes O(nlogn) time.

.. code-block:: java

    class Entry {
        long val;
        int cnt;

        public Entry(int val) {
            this.val = val;
            this.cnt = 0;
        }

        public String toString() {
            return Long.toString(this.val) + "(" + Integer.toString(this.cnt) + ")";
        }
    }

    public int countRangeSum(int[] nums, int lower, int upper) {
        int n = nums.length;

        if (n==0)
            return 0;

        Entry[] prefixSum = new Entry[n];

        for (int i=0; i<n; i++) {
            prefixSum[i] = new Entry(nums[i]);

            if (i > 0) {
                prefixSum[i].val += prefixSum[i-1].val;
            }

            if (prefixSum[i].val >= lower && prefixSum[i].val <= upper)
                prefixSum[i].cnt = 1;
        }

        mergeSort(prefixSum, lower, upper);

        int cnt = 0;

        for (int i=0; i<n; i++) {
            cnt += prefixSum[i].cnt;
        }

        return cnt;
    }

    private void mergeSort(Entry[] prefixSum, int lower, int upper) {
        int n = prefixSum.length;
        Entry[] tmp = new Entry[n];

        mergeSort(prefixSum, 0, n-1, tmp, lower, upper);
    }

    private void mergeSort(Entry[] prefixSum, int begin, int end, Entry[] tmp, int lower, int upper) {
        if (begin == end) {
            return;
        }

        int middle = begin + (end - begin)/2;

        mergeSort(prefixSum, begin, middle, tmp, lower, upper);
        mergeSort(prefixSum, middle+1, end, tmp, lower, upper);

        //first half is sorted and second half is sorted too

        // for each left, see how many right in the 2nd half satisfy
        // lower <= prefixSum[right]-prefixSum[left] <= upper
        int i=middle+1;
        int j=middle+1;

        // note that i and j only increments
        // so the nested loop takes only O(n) time
        for (int left=begin; left<=middle; left++) {
            while (i <= end &&
                    prefixSum[i].val - prefixSum[left].val < lower) {
                i++;
            }

            while (j <= end &&
                    prefixSum[j].val - prefixSum[left].val <= upper) {
                j++;
            }

            prefixSum[left].cnt += j-i;
        }


        merge(prefixSum, begin, middle, end, tmp);
    }

    private void merge(Entry[] prefixSum, int aBegin, int aEnd, int bEnd, Entry[] tmp) {

        int i=aBegin;
        int j=aEnd+1;
        int k=aBegin;

        while (i<=aEnd && j<=bEnd) {
            if (prefixSum[i].val <= prefixSum[j].val) {
                tmp[k] = prefixSum[i];
                i++;
                k++;
            }
            else {
                tmp[k] = prefixSum[j];
                j++;
                k++;
            }
        }

        while (i <= aEnd) {
            tmp[k] = prefixSum[i];
            i++;
            k++;
        }

        while (j <= bEnd) {
            tmp[k] = prefixSum[j];
            j++;
            k++;
        }

        for (int z=aBegin; z<=bEnd; z++) {
            prefixSum[z] = tmp[z];
        }
    }