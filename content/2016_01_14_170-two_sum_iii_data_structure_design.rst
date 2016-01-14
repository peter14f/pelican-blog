170-two_sum_iii_data_structure_design
#####################################

:date: 2016-1-14 20:06
:tags: X-Sum
:category: LeetCode
:slug: 170-two_sum_iii_data_structure_design

`LeetCode Problem Link <https://leetcode.com/problems/two-sum-iii-data-structure-design/>`_

To make ``add()`` take O(1) time and ``find()`` take O(n) time, we will use a HashMap<Integer, Integer> where
the key the number stored and the value is number times the number is added.

This takes O(n) time.

.. code-block:: java

    public class TwoSum {

        // key is the number added, value is the number of times it has been added
        HashMap<Integer, Integer> cnt;

        public TwoSum() {
            cnt = new HashMap<Integer, Integer>();
        }

        public void add(int number) {
            if (cnt.containsKey(number))
                cnt.put(number, cnt.get(number)+1);
            else
                cnt.put(number, 1);
        }

        public boolean find(int value) {
            for (int num: cnt.keySet()) {
                int d = value - num;
                if (cnt.containsKey(d)) {
                    if (num == d) {
                        if (cnt.get(num) > 1) {
                            return true;
                        }
                    }
                    else {
                        return true;
                    }
                }
            }
            return false;
        }
    }
