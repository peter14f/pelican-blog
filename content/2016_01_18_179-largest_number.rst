179-largest_number
##################

:date: 2016-1-18 21:34
:tags: Custom Comparator
:category: LeetCode
:slug: 179-largest_number

`LeetCode Problem Link <https://leetcode.com/problems/largest-number/>`_

This one took me quite a well. The first idea that came up to my mind is sort the numbers lexically.
But this won't work for 3 and 30 for example. Trying to write a custom comparator character by
character was also very difficult. In the end simply think of what makes one string greater than
the aother string. If the integer ``a`` concatenated with ``b`` is larger than the interger ``b``
concatenated with ``a``, then ``a`` is considered larger than ``b``.

.. code-block:: java

    class MyComparator implements Comparator<String> {

        @Override
        public int compare(String o1, String o2) {
            long a = Long.parseLong(o1 + o2);
            long b = Long.parseLong(o2 + o1);

            if (a > b)
                return 1;
            else if (b > 1)
                return -1;
            else
                return 0;
        }
    }

    public String largestNumber(int[] nums) {
        if (nums.length == 0)
            return "";

        String[] arr = new String[nums.length];

        for (int i=0; i<nums.length; i++) {
            arr[i] = Integer.toString(nums[i]);
        }

        Arrays.sort(arr, new MyComparator());

        StringBuffer sb = new StringBuffer();

        boolean beenZero = true;

        for (int i=arr.length-1; i>=0; i--) {
            if (beenZero) {
                if (!arr[i].equals("0"))
                    beenZero = false;
                else
                    continue;
            }

            sb.append(arr[i]);

        }

        if (beenZero)
            sb.append(0);

        return sb.toString();
    }
