005-longest_palindromic_substring
#################################

:date: 2015-9-2 18:56
:tags: Palindrome, Dynamic Programming, String
:category: LeetCode
:slug: 005-longest_palindromic_substring

`LeetCode Problem Link <https://leetcode.com/problems/longest-palindromic-substring/>`_

Find the longest palindromic substring given the input string ``s`` with length ``n``.

The naive solution is to examine all possible substrings of ``s``:

  Let ``i`` be the starting index of the substring (``i`` goes from ``0`` to ``n-1``)

   Let ``j`` be the ending index of the substring (``j`` goes from ``i`` to ``n-1``)

     Check if the substring starting at index ``i`` and ending at index ``j`` is a palindrome

This approach will take O(n\ :superscript:`3`) time and it won't pass the Online Judge.

|
|

Here is a solution using Dynamic Programming, which takes O(n\ :superscript:`2`) time and O(n\ :superscript:`2`) space.


We make the following observation:

#. all substrings of length *1* is a palindrome
#. all substrings of length *2* is a palindrome if it consists of only 1 character.
#. all substrings of length *greater than 2* is a palindrome if its first character is the same as its last character **AND** that its substring not containing the first and last character is a palindrome

| The array ``palindrom`` is a 2-dimensional boolean array.
| ``palindrome[i][j]`` denote whether the substring starting at index ``i`` and ending at index ``j`` is a palindrome.
|

.. code-block:: java

    public String longestPalindrome(String s) {
        boolean[][] palindrome = new boolean[s.length()][s.length()];

        char[] s_arr = s.toCharArray();
        int max = 1;
        int start = 0;

        for (int offset=0; offset < s_arr.length; offset++) {
            for (int row=0; row < s_arr.length; row++) {
                if (offset == 0) {
                    palindrome[row][row+offset] = true;
                }
                else if (offset == 1) {
                    if (row+offset < s_arr.length &&
                        s_arr[row] == s_arr[row+offset]) {
                        palindrome[row][row+offset] = true;

                        if (offset+1 > max) {
                            max = offset + 1;
                            start = row;
                        }
                    }
                }
                else {
                    if (row+offset < s_arr.length &&
                          palindrome[row+1][row+offset-1] &&
                          s_arr[row] == s_arr[row+offset]) {

                        palindrome[row][row+offset] = true;

                        if (offset+1 > max) {
                            max = offset + 1;
                            start = row;
                        }
                    }
                }
            }
        }

        return s.substring(start, start + max);
    }

Here is another solution that takes O(n\ :superscript:`2`) time but constant space:

  Let ``i`` be all the possible **center** (``i`` takes 2*n different values - center of a palindromic substring can be between two characters)

    Let ``j`` be the number characters there are on each side of the palindromic substring (``j`` goes from ``1`` to ``n/2``)

    As ``j`` is expanded, check if the two newly added characters at the head and tail are the same

.. code-block:: java

    public String longestPalindrome2(String s) {
        char[] s_arr = s.toCharArray();
        int max = 1;
        int center = 0;

        for (int c=0; c < s.length(); c++) {
            // center at index c
            int left = c-1;
            int right = c+1;

            int length = 1;
            while (left >=0 && right < s.length()) {
                if (s_arr[left] == s_arr[right]) {
                    length += 2;
                }
                else {
                    break;
                }

                left--;
                right++;
            }

            if (length > max) {
                max = length;
                center = c;
            }

            // center between index c and index (c + 1)
            left = c;
            right = c+1;
            length = 0;

            while (left >=0 && right < s.length()) {
                if (s_arr[left] == s_arr[right]) {
                    length += 2;
                }
                else {
                    break;
                }

                left--;
                right++;
            }

            if (length > max) {
                max = length;
                center = c;
            }
        }

        //         01
        // max = 2 aa
        //         0123 c=1
        // max = 4 baab
        if (max % 2 == 0) {
            int left_one = center;
            int start = left_one - (max/2 - 1);
            return s.substring(start, start+max);
        }
        else {
            int start = center - (max-1)/2;
            return s.substring(start, start+max);
        }
    }

And finally there is the Manacher's algorithm which takes O(n) time. (links will be added later)