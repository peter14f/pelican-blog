284-peeking_iterator
####################

:date: 2016-2-22 1:35
:tags: Iterators
:category: LeetCode
:slug: 284-peeking_iterator

`LeetCode Problem Link <https://leetcode.com/problems/peeking-iterator/>`_

I just use a field to cache what was returned by the next() call.

.. code-block:: java

    public class PeekingIterator implements Iterator<Integer> {

        Iterator<Integer> iterator;
        Integer val;

        public PeekingIterator(Iterator<Integer> iterator) {
            // initialize any member here.
            this.iterator = iterator;
            if (this.iterator.hasNext())
                val = iterator.next();
            else
                val = null;
        }

        // Returns the next element in the iteration without advancing the iterator.
        public Integer peek() {
            return val;
        }

        // hasNext() and next() should behave the same as in the Iterator interface.
        // Override them if needed.
        @Override
        public Integer next() {
            int toReturn = val;

            if (this.iterator.hasNext())
                val = iterator.next();
            else
                val = null;

            return toReturn;
        }

        @Override
        public boolean hasNext() {
            if (val == null)
                return false;
            else
                return true;
        }
    }
