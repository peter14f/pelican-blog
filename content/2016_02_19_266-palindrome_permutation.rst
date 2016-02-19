266-palindrome_permutation
##########################

:date: 2016-2-19 10:29
:tags: Palindrome Permutation
:category: LeetCode
:slug: 266-palindrome_permutation

`LeetCode Problem Link <https://leetcode.com/problems/palindrome-permutation/>`_

Palindromes with even lengths - each character appears an even number of times.

Palindromes with odd lengths - all characters appears an even number of time.
One character appears an odd number of time.

So we must count the number of times each character appears. Use a HashMap<Character, Integer>.

I simply remove the character from the HashMap when the count reaches two.

.. code-block:: java

    public boolean canPermutePalindrome(String s) {
        HashMap<Character, Integer> frequency = new HashMap<Character, Integer>();

        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);

            if (frequency.containsKey(c)) {
                frequency.put(c, frequency.get(c) + 1);

                if (frequency.get(c) == 2) {
                    frequency.remove(c);
                }
            }
            else {
                frequency.put(c, 1);
            }
        }

        return (frequency.isEmpty() || frequency.size() == 1);
    }

