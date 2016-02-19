264-ugly_number_ii
##################

:date: 2016-2-19 8:57
:tags: Ugly Number
:category: LeetCode
:slug: 264-ugly_number_ii

`LeetCode Problem Link <https://leetcode.com/problems/ugly-number-ii/>`_

Use the current ugly number to expand the numbers for 3 lists: L1, L2, L3.

Use three pointers ``i``, ``j``, ``k``. The next ugly number is min(L1[i], L2[j], L3[k]).


.. code-block:: java

    public int nthUglyNumber(int n) {

        List<Integer> l1 = new ArrayList<Integer>();
        List<Integer> l2 = new ArrayList<Integer>();
        List<Integer> l3 = new ArrayList<Integer>();

        int num = 1;
        int index = 1;

        int i=0;
        int j=0;
        int k=0;

        while (index < n) {
            expandLists(l1, l2, l3, num);

            num = Math.min(l1.get(i), Math.min(l2.get(j), l3.get(k)));
            index++;

            if (num == l1.get(i))
                i++;
            if (num == l2.get(j))
                j++;
            if (num == l3.get(k))
                k++;
        }

        return num;
    }

    private void expandLists(List<Integer> l1, List<Integer> l2, List<Integer> l3, int num) {
        l1.add(num * 2);
        l2.add(num * 3);
        l3.add(num * 5);
    }

Actually, you can do this with just one list as well.

.. code-block:: java

    public int nthUglyNumber(int n) {

        int index = 1;
        int ugly = 1;

        List<Integer> l = new ArrayList<Integer>();

        int i = 0;
        int j = 0;
        int k = 0;

        while (index < n) {

            l.add(ugly*2);
            l.add(ugly*3);
            l.add(ugly*5);

            ugly = Math.min(l.get(3*i),
                           Math.min(l.get(3*j+1),
                                    l.get(3*k+2)));

            index++;

            if (ugly == l.get(3*i))
                i++;
            if (ugly == l.get(3*j+1))
                j++;
            if (ugly == l.get(3*k+2))
                k++;

        }

        return ugly;
    }
