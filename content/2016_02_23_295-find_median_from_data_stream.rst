295-find_median_from_data_stream
################################

:date: 2016-2-23 0:06
:tags: Median, Priority Queues
:category: LeetCode
:slug: 295-find_median_from_data_stream

`LeetCode Problem Link <https://leetcode.com/problems/flip-game-ii/>`_

If we could maintain two heaps, a max heap and a min heap, such that their size differs by one at most. Then finding
the median would be doable.

We must be aware that at the end of each add, while(maxHeap.peek() > minHeap.peek()), we swap the extreme elements.

.. code-block:: java

    public class MedianFinder {

        PriorityQueue<Integer> minHeap;
        PriorityQueue<Integer> maxHeap;

        public MedianFinder() {
            minHeap = new PriorityQueue<Integer>();
            maxHeap = new PriorityQueue<Integer>(Collections.reverseOrder());
        }

        // Adds a number into the data structure.
        public void addNum(int num) {

            if (maxHeap.size() == minHeap.size()) {
                maxHeap.offer(num);
            }
            else {
                // size off by 1, insert to smaller heap
                if (minHeap.size() < maxHeap.size()) {
                    minHeap.offer(num);
                }
                else {
                    maxHeap.offer(num);
                }
            }

            while (!minHeap.isEmpty() && maxHeap.peek() > minHeap.peek()) {
                maxHeap.offer(minHeap.poll());
                minHeap.offer(maxHeap.poll());
            }

            //System.out.println("minHeao=" + minHeap);
            //System.out.println("maxHeao=" + maxHeap);
        }

        // Returns the median of current data stream
        public double findMedian() {

            if (minHeap.size() > maxHeap.size())
                return minHeap.peek();
            else if (maxHeap.size() > minHeap.size())
                return maxHeap.peek();
            else
                return (double)(minHeap.peek() + maxHeap.peek())/2;
        }
    }