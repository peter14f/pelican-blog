125-valid_palindrome
####################

:date: 2015-12-2 22:53
:tags: Palindrome
:category: LeetCode
:slug: 125-valid_palindrome

`LeetCode Problem Link <https://leetcode.com/problems/valid-palindrome/>`_

Non-alphanumeric characters are skipped. Keep two poienters ``i`` and ``j``, one that starts at
index ``0`` and the other starts at index ``n-1``.

It takes O(n) time.

    public boolean isPalindrome(String s) {
        if (s.isEmpty())
            return true;

        s = s.toLowerCase().trim();

        char[] sArr = s.toCharArray();

        int i=0;
        int j=sArr.length-1;

        while (i<sArr.length) {

            if (!isAlphaNumeric(sArr[i])) {
                i++;
                continue;
            }

            if (j < 0) {
                return false;
            }

            if (!isAlphaNumeric(sArr[j])) {
                j--;
                continue;
            }

            if (sArr[i] != sArr[j]) {
                return false;
            }

            i++;
            j--;
        }

        return true;
    }

    private boolean isAlphaNumeric(char c) {

        if ((c >= '0' && c <= '9') || (c >='a' && c <= 'z')) {
            return true;
        }

        return false;
    }