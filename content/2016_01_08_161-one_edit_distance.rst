161-one_edit_distance
#####################

:date: 2016-1-8 19:03
:tags: Edit Distance
:category: LeetCode
:slug: 161-one_edit_distance

`LeetCode Problem Link <https://leetcode.com/problems/one-edit-distance/>`_

We could just get the edit distance between ``s`` and ``t`` and see if the edit distance is 1. But this will take
O(mn) time where ``m`` is the length of string ``s`` and ``n`` is the length of string ``t``.

If the length difference is more than one, we could simply return ``false``.

Use two pointer ``i`` and ``j``, one to traverse the longer string and the other to traverse the shorter string.
Count the number of edit operation needed to make the shorter string become the longer string. (Note the lengths may
actually be the same)

This takes O(n) time where ``n`` is the length of the longer string.

.. code-block:: java

    public boolean isOneEditDistance(String s, String t) {
         int sMinusT = s.length() - t.length();
         String shortStr, longStr;

         if (sMinusT > 1 || sMinusT < -1)
             return false;

         if (sMinusT >= 1) {
             longStr = s;
             shortStr = t;
         }
         else {
             longStr = t;
             shortStr = s;
         }

         int i = 0; // to traverse longStr
         int j = 0; // to traverse shortStr
         int numOperation = 0;

         while (i < longStr.length()) {
             if (j == shortStr.length()) {
                 numOperation++;
                 break;
             }

             if (longStr.charAt(i) == shortStr.charAt(j)) {
                 i++;
                 j++;
             }
             else {
                 numOperation++;

                 if (numOperation > 1)
                     return false;

                 i++;

                 if (sMinusT == 0) {
                     j++;
                 }
             }
         }

         return numOperation == 1;
    }

