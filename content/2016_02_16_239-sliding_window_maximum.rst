239-sliding_window_maximum
##########################

:date: 2016-2-16 10:58
:tags: Sliding Windows, Heap
:category: LeetCode
:slug: 239-sliding_window_maximum

`LeetCode Problem Link <https://leetcode.com/problems/sliding-window-maximum/>`_

The most straightforward solution take O(nk) time which simply uses two nested for loops to try to
look for the max element in the current sliding window.

.. code-block:: java

    // can assume k to be valid
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0)
            return nums;

        int[] output = new int[nums.length-k+1];

        for (int i=0; i+k-1 < nums.length; i++) {
            int max = nums[i];
            for (int j=1; j<k; j++) {
                if (nums[i+j] > max)
                    max = nums[i+j];
            }
            output[i] = max;
        }

        return output;
    }

The problem reminds me of 218-the_skyline_problem. We could maintain a max heap of size ``k`` so that getting the
maximum element within the sliding windows always takes O(logk) time. As the sliding windows gets moved forward one
slot, we need to remove one element from the heap and then insert one element into the heap. Such heap operations
were done in 218-the_skyline_problem.

This is the O(nlogk) time solution.

.. code-block:: java

    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0)
            return nums;

        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        int[] output = new int[nums.length-k+1];

        for (int i=0; i<k; i++) {
            pq.offer(nums[i]);
        }
        output[0] = pq.peek();

        for (int i=k; i<nums.length; i++) {
            int toRemove = nums[i-k];
            pq.remove(toRemove);
            pq.offer(nums[i]);
            output[i-k+1] = pq.peek();
        }

        return output;
    }

The follow-up question is the do this in O(n) time. The hint suggests using a deque (double-ended queue).
We use the dequeue to store the indices of elements in ``nums``.
The dequeue does not always contain ``k`` elements. We only store the useful indices.

.. code-block:: java

    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0)
            return nums;

        int[] output = new int[nums.length-k+1];

        LinkedList<Integer> dequeue = new LinkedList<Integer>();

        for (int i=0; i<k; i++) {
            while (!dequeue.isEmpty() && nums[i] >= nums[dequeue.getLast()]) {
                dequeue.removeLast();
            }

            dequeue.add(i);
        }

        output[0] = nums[dequeue.getFirst()];

        /* Notice that the dequeue size always store <= k indices */
        for (int i=k; i<nums.length; i++) {
            while (!dequeue.isEmpty() && nums[i] >= nums[dequeue.getLast()]) {
                dequeue.removeLast();
            }

            while (!dequeue.isEmpty() && dequeue.getFirst() <= i-k) {
                dequeue.removeFirst();
            }

            dequeue.add(i);
            output[i-k+1] = nums[dequeue.getFirst()];
        }

        return output;
    }

Each element's index is inserted and then removed at most once. So this algorithm takes O(n + n) = O(n) time.


We only store the index of **previous numbers bigger than the new number** in the dequeue. But we also get rid of
bigger numbers already that's too old to be in the current window.

::

    DEUQUEU only stores the index of older numbers that are > new number

    front <--------------   --------------> back
    the smaller the index   the bigger the index


    The front of the DEQUEUE always contains the max element in the window


