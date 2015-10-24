023-merge_k_sorted_lists
########################

:date: 2015-09-07 20:25
:tags: Priority Queues
:category: LeetCode
:slug: 023-merge_k_sorted_lists

`LeetCode Problem Link <https://leetcode.com/problems/merge-k-sorted-lists/>`_

We have ``k`` lists. We use a PriorityQueue<ListNode> and a HashMap<ListNode, Integer>. At all times, we make sure
that each of these two data structures does not have more than ``k`` entries.

The HashMap is to lookup which list this ListNode came from.

Assuming the total number of nodes in these ``k`` lists is ``n``.

This should take n O(k) time.

Make sure to check for lists that are initially empty.

.. code-block:: java

    class ListNodeComparator implements Comparator<ListNode> {
        @Override
        public int compare(ListNode o1, ListNode o2) {
            if (o1.val < o2.val)
                return -1;
            else if (o1.val == o2.val)
                return 0;
            else
                return 1;
        }
    }


    // k lists
    // 1: 1 2 3
    // 2: 4 5 6
    // 3: 7 8 9
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(new ListNodeComparator());
        HashMap<ListNode, Integer> map = new HashMap<ListNode, Integer>();
        int k = lists.length;

        if (k==0)
            return null;

        for (int i=0; i<k; i++) {
            ListNode cur = lists[i];
            if (cur != null) {
                pq.offer(cur);
                map.put(cur, i);
            }
        }

        ListNode head = null;
        ListNode tail = null;

        while (!pq.isEmpty()) {
            ListNode pqNode = pq.poll();

            if (tail==null) {
                head = pqNode;
                tail = pqNode;
            }
            else {
                tail.next = pqNode;
                tail = pqNode;
            }

            int index = map.get(pqNode);
            map.remove(pqNode);

            lists[index] = pqNode.next;
            tail.next = null;

            if (lists[index] != null) {
                pq.offer(lists[index]);
                map.put(lists[index], index);
            }
        }

        return head;
    }