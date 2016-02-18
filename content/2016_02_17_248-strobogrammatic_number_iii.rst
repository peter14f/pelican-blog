248-strobogrammatic_number_iii
##############################

:date: 2016-2-17 19:43
:tags: Strobogrammatic Numbers, Bottom-Up, Memoization
:category: LeetCode
:slug: 248-strobogrammatic_number_iii

`LeetCode Problem Link <https://leetcode.com/problems/strobogrammatic-number-iii/>`_

One task that's repeated needed in this problem is check is string ``a`` is less than or equal to string ``b``.

.. code-block:: java

    // assume a and b do not have leading zeros
    private boolean aIsLessThanOrEqualToB(String a, String b) {

        int aN = a.length();
        int bN = b.length();

        if (aN < bN)
            return true;
        else if (aN > bN)
            return false;

        int i=0;
        // same length
        for (; i<aN; i++) {
            if (a.charAt(i) < b.charAt(i)) {
                return true;
            }
            else if (a.charAt(i) > b.charAt(i)) {
                break;
            }
            else {
                if (i==aN-1)
                    return true;
            }
        }

        return false;
    }

We first get the length of ``low`` and the length of ``high`` - ``lowN`` and ``highN``.
We pretty much need to get the list of strobogrammatic number for ``n`` values ranging from ``lowN`` to ``highN``
and then count those that's within the range [low, high].

.. code-block:: java

    public int strobogrammaticInRange(String low, String high) {
        int cnt = 0;

        if (low==null || high==null || high.charAt(0) == '-')
            return 0;
        if (low.charAt(0) == '-')
            low = "0";

        int lowN = low.length();
        int highN = high.length();

        List<String> prevPrev = new ArrayList<String>();

        prevPrev.add("0");
        prevPrev.add("1");
        prevPrev.add("8");

        if (lowN == 1) {
            int c = numInRange(prevPrev, low, high);
            cnt += c;
        }

        List<String> prev = new ArrayList<String>();

        prev.add("11");
        prev.add("69");
        prev.add("88");
        prev.add("96");

        if (lowN <= 2) {
            int c = numInRange(prev, low, high);
            cnt += c;
        }

        prev.add("00");

        int[] left =  {'0', '1', '6', '8', '9'};
        int[] right = {'0', '1', '9', '8', '6'};

        List<String> cur = null;
        for (int digit=3; digit <= highN; digit++) {
            cur = new ArrayList<String>();

            for (String s: prevPrev) {
                for (int j=(digit==highN)?1:0; j<left.length; j++) {
                    StringBuffer sb = new StringBuffer();
                    sb.append((char)left[j]);
                    sb.append(s);
                    sb.append((char)right[j]);
                    cur.add(sb.toString());
                }
            }

            int c = numInRange(cur, low, high);
            cnt += c;

            prevPrev = prev;
            prev = cur;
        }

        return cnt;
    }

    private int numInRange(List<String> list, String low, String high) {
        int cnt = 0;

        for (String num: list) {
            if (num.charAt(0) == '0' && num.length() > 1) {
                continue;
            }

            if (aIsLessThanOrEqualToB(low, num) && aIsLessThanOrEqualToB(num, high)) {
                cnt++;
            }
        }

        return cnt;
    }
