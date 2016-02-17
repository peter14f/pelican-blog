246-strobogrammatic_number
##########################

:date: 2016-2-17 9:47
:tags: Strobogrammatic Numbers
:category: LeetCode
:slug: 246-strobogrammatic_number

`LeetCode Problem Link <https://leetcode.com/problems/strobogrammatic-number/>`_

'0', '1', '6', '8', '9' are the strobogrammatic characters. Use two poineters. It takes O(n) time.

.. code-block:: java

    public boolean isStrobogrammatic(String num) {
        int l=0, h=num.length() - 1;

        while (l<=h) {
            char left = num.charAt(l);
            char right = num.charAt(h);

            if (!stroboChar(left) || ! stroboChar(right))
                return false;

            if (left == '1') {
                if (right != '1')
                    return false;
            }
            else if (left == '8') {
                if (right != '8')
                    return false;
            }
            else if (left == '6') {
                if (right != '9')
                    return false;
            }
            else if (left == '9') {
                if (right != '6')
                    return false;
            }
            else if (left == '0') {
                if (right != '0')
                    return false;
            }

            l++;
            h--;
        }

        return true;
    }

    private boolean stroboChar(char c) {
        return (c=='0' || c=='1' || c=='8' || c=='6' || c=='9');
    }


