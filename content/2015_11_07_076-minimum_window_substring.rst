076-minimum_window_substring
############################

:date: 2015-11-7 9:57
:tags: Two Pointers
:category: LeetCode
:slug: 076-minimum_window_substring

`LeetCode Problem Link <https://leetcode.com/problems/minimum-window-substring/>`_

In my first attempt, I was decrementing the count in the HashMap<Character, Integer> and then checking if the HashMap
is empty. Using this approach makes it impossible to solve this problem correctly.

Instead we should increment as we as see a character in ``t``. In the meantime, we need to keep track of the meaningful
length.

First we need a record of how many times each character in ``t`` appears in ``t``. And then we advance the ``end``
pointer until we've seen all this character that many times.

Let the length of ``s`` be ``n``. In the worst case, ``t`` only contains 1 character and it appears only once in ``s``
and is the last character of ``s``. ``end`` goes from ``0`` to ``n-1``, then ``start`` goes from ``0`` to ``n-1`` as
well. Therefore this takes O(n) time.

.. code-block:: java

    public String minWindow(String s, String t) {

        char[] arrT = t.toCharArray();
        char[] arrS = s.toCharArray();

        HashMap<Character, Integer> cnt = new HashMap<Character, Integer>();

        // how many times each character in t appears in t
        for (int i=0; i<arrT.length; i++) {
            if (cnt.containsKey(arrT[i])) {
                cnt.put(arrT[i], cnt.get(arrT[i])+1);
            }
            else {
                cnt.put(arrT[i], 1);
            }
        }

        // check if we've seen all characters in t
        HashMap<Character, Integer> curCnt = new HashMap<Character, Integer>();

        int end = 0;
        int numCharSeen = 0;
        int start = 0;
        int minLength = Integer.MAX_VALUE;
        int minStart = -1;

        while (end < arrS.length) {

            char c = arrS[end];

            if (cnt.containsKey(c)) {

                if (curCnt.containsKey(c)) {
                    if (curCnt.get(c) < cnt.get(c))
                        numCharSeen++;

                    curCnt.put(c, curCnt.get(c) + 1);
                }
                else {
                    curCnt.put(c, 1);
                    numCharSeen++;
                }
            }

            if (numCharSeen == arrT.length) {
                char startC = arrS[start];
                while (!cnt.containsKey(startC) || curCnt.get(startC) > cnt.get(startC)) {

                    if (cnt.containsKey(startC)) {
                        // moving start forward means the window has one fewer character
                        curCnt.put(startC, curCnt.get(startC) - 1);
                    }

                    start++;
                    startC = arrS[start];
                }

                int length = end-start+1;
                if (length < minLength) {
                    minLength = length;
                    minStart = start;
                }
            }

            end++;
        }

        if (minStart == -1)
            return "";
        else
            return new String(arrS, minStart, minLength);
    }
    