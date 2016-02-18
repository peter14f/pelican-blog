247-strobogrammatic_number_ii
#############################

:date: 2016-2-17 14:58
:tags: Strobogrammatic Numbers, Recursion, Buttom-Up, Memoization
:category: LeetCode
:slug: 247-strobogrammatic_number_ii

`LeetCode Problem Link <https://leetcode.com/problems/strobogrammatic-number-ii/>`_

The tests does not allow leading zeros. So we must distinguish the cases where leading zeros are allowed
and the cases where leading zeros are not allowed.

.. code-block:: java

    public List<String> findStrobogrammatic(int n) {
        return findStrobogrammatic(n, false);
    }

    private List<String> findStrobogrammatic(int n, boolean leadingZero) {

        List<String> ans = new ArrayList<String>();

        if (n <= 0)
            return ans;

        if (n==1) {
            // single digit strobogrammatic characters are '0', '1', '8'
            ans.add("0");
            ans.add("1");
            ans.add("8");
            return ans;
        }

        if (n==2) {
            if (leadingZero)
                ans.add("00");

            ans.add("11");
            ans.add("69");
            ans.add("88");
            ans.add("96");
        }

        List<String> strs = findStrobogrammatic(n-2, true);
        List<Character> left = new ArrayList<Character>();
        List<Character> right = new ArrayList<Character>();

        if (leadingZero) {
            left.add('0');
            right.add('0');
        }

        left.add('1');
        right.add('1');
        left.add('6');
        right.add('9');
        left.add('8');
        right.add('8');
        left.add('9');
        right.add('6');

        for (String s: strs) {
            for (int i=0; i<left.size(); i++) {
                StringBuffer sb = new StringBuffer();
                sb.append(left.get(i));
                sb.append(s);
                sb.append(right.get(i));
                ans.add(sb.toString());
            }
        }

        return ans;
    }

We can also solve this using the buttom-up approach with memoization. There is no clear advange in doing it this way
for this problem. But you will see when you have to in 248-strobogrammatic_number_iii get the list for two different
values of ``n``, avoiding recomputation helps tremendously.



