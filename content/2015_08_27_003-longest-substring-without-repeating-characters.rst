003 Longest Substring Without Repeating Characters
##################################################

:date: 2015-8-27 18:35
:tags: String, Moving Window
:category: LeetCode
:slug: 003-longest-substring-without-repeating-characters

`LeetCode Problem Link <https://leetcode.com/problems/longest-substring-without-repeating-characters/>`_

Let ``s`` be the input string.

Here is the straightforward solution:


 | ``i`` is the starting index of the current substring.
 | ``j`` marks the end of the current substring.

This approach takes O(n\ :superscript:`2`) time complexity and O(n) space complexity.
Here is the code:

.. code-block:: java

    public int lengthOfLongestSubstring1(String s) {
        char[] sArr = s.toCharArray();

        int maxSubstringLen = 0;

        for (int i=0; i < sArr.length; i++) {
            HashSet<Character> hashtable = new HashSet<Character>();
            hashtable.add(sArr[i]);

            for (int j=i+1; j <= sArr.length; j++) {

                if (j==sArr.length || hashtable.contains(sArr[j])) {
                    String substring = s.substring(i, j);
                    if (substring.length() > maxSubstringLen) {
                        maxSubstringLen = substring.length();
                    }
                    break; // must stop extending the substring starting at index i
                }
                else {
                    hashtable.add(sArr[j]);
                }
            }

        }

        return maxSubstringLen;
    }

This solution passed the online judge system back in 2013, but not anymore.
You will get a "Time Limit Exceeded"

**How can we solve this problem in O(n) time???**

We will have to maintain a moving window. ``i`` marks the start of the window and ``j`` marks the end of window.
We use a **HashMap** to track the last occured index for a particular character. The moving window is expanded by
incrementing ``j``. If ``j`` turns out to be a repeating character for the current substring, we know how to adjust
``i``. We set ``i`` to the last occured index for character at index ``j`` ``+ 1``.

Here is the code:

.. code-block:: java

    public int lengthOfLongestSubstring2(String s) {
        int max = 0;

        HashMap<Character, Integer> lastOccured = new HashMap<Character, Integer>();
        char[] sArr = s.toCharArray();

        lastOccured.put(sArr[0], 0);

        int i=0;

        for (int j=1; j<sArr.length; j++) {

            if (lastOccured.containsKey(sArr[j]) && lastOccured.get(sArr[j]) >=i) {
                i = lastOccured.get(sArr[j]) + 1;
            }

            lastOccured.put(sArr[j], j);
            if (j-i+1 > max) {
                max = j-i+1;
            }
        }

        return max;

    }


**Why is this O(n) time complexity?**

In each iteration either ``i`` or ``j`` is advanced. ``i`` can never go pass ``j`` and the algorithm terminates when
``j`` reaches the last character in ``s``.

In the worst case, ``j`` increments per iteration but stops right before the last character, and then ``i`` increments
per iteration until it reaches ``j-1``, in the last iteration ``j`` increments again and reaches the last character.
This is O(n) + O(n) = O(2n) = O(n).




