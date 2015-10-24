017-letter_combinations_of_a_phone_number
#########################################

:date: 2015-09-07 20:19
:tags:
:category: LeetCode
:slug: 017-letter_combinations_of_a_phone_number

`LeetCode Problem Link <https://leetcode.com/problems/letter-combinations-of-a-phone-number/>`_

We start from the first digit toward the last. StringBuffer only supports append.

.. code-block:: java

    public static final char[][] table =
        {{},
         {},
         {'a', 'b', 'c'},      // 2
         {'d', 'e', 'f'},      // 3
         {'g', 'h', 'i'},      // 4
         {'j', 'k', 'l'},      // 5
         {'m', 'n', 'o'},      // 6
         {'p', 'q', 'r', 's'}, // 7
         {'t', 'u', 'v'},      // 8
         {'w', 'x', 'y', 'z'}  // 9
        };

    public List<String> letterCombinations(String digits) {

        char[] arr = digits.toCharArray();
        List<String> ans = new ArrayList<String>();
        if (arr.length > 0) {
            addStrings(arr, 0, ans);
        }
        return ans;
    }

    private void addStrings(char[] arr, int i, List<String> ans) {
        if (i >= arr.length)
            return;

        char[] chars = table[arr[i] - '0'];
        int oldSize = ans.size();

        if (oldSize == 0) {
            for (int k=0; k<chars.length; k++) {
                ans.add(Character.toString(chars[k]));
            }
        }
        else {
            for (int j=0; j<oldSize; j++) {
                for (int k=0; k<chars.length; k++) {
                    StringBuffer newSb = new StringBuffer(ans.get(j));
                    newSb.append(chars[k]);
                    ans.add(newSb.toString());
                }
            }

            for (int j=0; j<oldSize; j++) {
                ans.remove(0);
            }
        }

        addStrings(arr, i+1, ans);
    }
