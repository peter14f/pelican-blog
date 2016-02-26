313-super_ugly_number
#####################

:date: 2016-2-25 23:32
:tags: Ugly Number
:category: LeetCode
:slug: 313-super_ugly_number

`LeetCode Problem Link <https://leetcode.com/problems/super-ugly-number/>`_

May be attempted to build ``k`` lists, one for each prime number. But that is actually not necessary.

It's better store all the ugly numbers in the list start with ``1`` and keep track of the index for
each prime number.

Remember that you will have the situation where two lists both yield the next super ugly number, make sure
the index for both prime numbers are advanced in that case.

.. code-block:: java

    public int nthSuperUglyNumber(int n, int[] primes) {

        List<Integer> results = new ArrayList<Integer>();
        int k = primes.length;

        // all indices initialized to zero
        int[] index = new int[k];

        results.add(1);

        while (results.size() < n) {

            int min = Integer.MAX_VALUE;

            for (int i=0; i<k; i++) {
                if (primes[i] * results.get(index[i]) < min) {
                    // saving minIndex in here would not catch multiple min indices
                    min = primes[i] * results.get(index[i]);
                }
            }

            results.add(min);

            // you may have to catch more than one list
            for (int i=0; i<k; i++) {
                if (primes[i] * results.get(index[i]) == min) {
                    index[i]++;
                }
            }
        }

        return results.get(n-1);
    }

