159-longest_substring_with_at_most_two_distinct_characters
##########################################################

:date: 2016-1-7 23:15
:tags: Substrings
:category: LeetCode
:slug: 159-longest_substring_with_at_most_two_distinct_characters

`LeetCode Problem Link <https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/>`_

The O(n) time solution is quite hard. We will use a HashMap<Character, Integer> to store the two distinct characters
closest to the current index ``i``.

If the current index ``i`` is a new character, i.e., a character different from the character at index ``first`` and
the character at index ``second``, we should immediately discard the information on the character at index ``first``
and update ``second`` to the current index ``i`` since it's the newest character seen as of now. We also update
``first`` to be the old value of ``second`` since the last other older character seen.

.. code-block:: java

    public int lengthOfLongestSubstringTwoDistinct(String s) {
        if (s.length() <= 2)
            return s.length();

        int max = 0;

        HashMap<Character, Integer> cnt = new HashMap<Character, Integer>();
        int first = 0;
        int second = -1;
        cnt.put(s.charAt(0), 1);

        for (int i=1; i<s.length(); i++) {
            char c = s.charAt(i);

            if (cnt.containsKey(c))
                cnt.put(c, cnt.get(c)+1);
            else {
                if (cnt.size() == 1) {
                    cnt.put(c, 1);
                    second = i;
                    continue;
                }
                else {
                    int t = 0;
                    for (char ch: cnt.keySet())
                        t += cnt.get(ch);

                    if (t > max)
                        max = t;

                    cnt.remove(s.charAt(first));
                    cnt.put(s.charAt(second), i-second);
                    cnt.put(c, 1);
                }
            }

            if (s.charAt(i) != s.charAt(i-1)) {
                first = second;
                second = i;
            }
        }

        int t = 0;
        for (char ch: cnt.keySet())
            t += cnt.get(ch);

        if (t > max)
            max = t;

        return max;
    }

Note that the HashMap has at most two entries. So this solution is O(1) space complexity.

