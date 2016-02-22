281-zigzag_iterator
###################

:date: 2016-2-21 16:39
:tags: Merge Sort
:category: LeetCode
:slug: 281-zigzag_iterator

`LeetCode Problem Link <https://leetcode.com/problems/zigzag-iterator/>`_

My implementation uses two pointers ``i``, and ``j`` that points to the next number to be spit out in ``l1`` and
``l2`` respectively. We also need a boolean field ``oneNext`` that keeps track of which list to use next.

.. code-block:: java

    public class ZigzagIterator {

    List<Integer> l1, l2;
    boolean oneNext;
    int i, j;

    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        l1 = v1;
        l2 = v2;
        oneNext = true;
        i=0;
        j=0;
    }

    public int next() {
        int toReturn = 0;
        if (i < l1.size() && j < l2.size()) {
            if (oneNext) {
                toReturn = l1.get(i);
                i++;
            }
            else {
                toReturn = l2.get(j);
                j++;
            }
            oneNext = !oneNext;
        }
        else if (i < l1.size()) {
            toReturn = l1.get(i);
            i++;
        }
        else if (j < l2.size()) {
            toReturn = l2.get(j);
            j++;
        }

        return toReturn;
    }

    public boolean hasNext() {
        return (i < l1.size() || j < l2.size()) ;
    }
}

The followup asks how to generalize this to k lists. Now instead of having two fields ``l1`` and ``l2``. What we
need is a List<List<Integer>> lists of size ``n``. Instead of having the boolean field ``oneNext``, what we need
is a int field called ``nextList`` who should be initialzed to ``0`` in the constructor. Pointers ``i`` and ``j``
will be replaced with a int[] ``pointers``.

.. code-block:: java

    public class ZigzagIteratorK {

        List<List<Integer>> lists;
        int nextList;
        int[] pointers;

        public ZigzagIteratorK(List<List<Integer>> lists) {
            this.lists = lists;
            nextList = 0;
            pointers = new int[lists.size()];
        }

        public boolean hasNext() {
            for (int i=0; i<pointers.length; i++) {
                if (pointers[i] < lists.get(i).size())
                    return true;
            }
            return false;
        }

        public int next() {
            int n = lists.size();

            while (pointers[nextList%n] >= lists.get(nextList%n).size()) {
                nextList++;
            }

            int toReturn =  lists.get(nextList%n).get(pointers[nextList%n]);
            pointers[nextList%n]++;
            nextList++;

            return toReturn;
        }
    }
