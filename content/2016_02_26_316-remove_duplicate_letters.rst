316-remove_duplicate_letters
############################

:date: 2016-2-26 15:22
:tags: Strings
:category: LeetCode
:slug: 316-remove_duplicate_letters

`LeetCode Problem Link <https://leetcode.com/problems/remove-duplicate-letters/>`_

In the first pass, get the frequency count of each character in the input string ``s``.

That we can know how many times each duplicated character shall be deleted.

I'm thinking of using recursion and DFS to find all versions of the deleted string and then sort
the list.


.. code-block:: java

    public String removeDuplicateLetters(String s) {

        HashMap<Character, Integer> remain = new HashMap<Character, Integer>();
        HashMap<Character, Integer> toDelete = new HashMap<Character, Integer>();

        int n = s.length();

        for (int i=0; i<n; i++) {
            char c = s.charAt(i);

            if (!remain.containsKey(c))
                remain.put(c, 1);
            else
                remain.put(c, remain.get(c) + 1);
        }

        for (char c: remain.keySet()) {
            if (remain.get(c) > 1)
                toDelete.put(c, remain.get(c)-1);
        }

        List<String> list = new ArrayList<String>();

        int i=0;
        while (i < n && !toDelete.containsKey(s.charAt(i))) {
            i++;
        }

        getAllDeletedStrings(new StringBuffer(s), i, remain, toDelete, list);

        //System.out.println(list);

        Collections.sort(list);

        return list.get(0);
    }

    private void getAllDeletedStrings(StringBuffer sb, int i,
            HashMap<Character, Integer> remain,
            HashMap<Character, Integer> toDelete,
            List<String> list) {

        int n = sb.length();

        if (i>=n) {

            if (toDelete.isEmpty()) {
                list.add(sb.toString());
            }

            return;
        }

        char c = sb.charAt(i);
        int oldTD = toDelete.get(c);
        int oldR = remain.get(c);


        if (remain.get(c) > toDelete.get(c)) {
            // can choose to delete or not

            // choice 1: choose not to delete
            remain.put(c, oldR-1);

            int j=i+1;
            while (j < n && !toDelete.containsKey(sb.charAt(j)))
                j++;

            getAllDeletedStrings(sb, j, remain, toDelete, list);

            remain.put(c, oldR);

            // choice 2: choose to delete
        }

        // deleting
        sb.deleteCharAt(i);

        remain.put(c, oldR - 1);
        if (oldR-1 == 0)
            remain.remove(c);

        toDelete.put(c, oldTD - 1);
        if (oldTD-1 == 0)
            toDelete.remove(c);

        int j=i;

        n = sb.length();
        while (j < n && !toDelete.containsKey(sb.charAt(j))) {
            j++;
        }

        getAllDeletedStrings(sb, j, remain, toDelete, list);

        sb.insert(i, c);
        toDelete.put(c, oldTD);
        remain.put(c, oldR);

    }

You guessed it! TLE on large Test Case.

::

    Submission Result: Time Limit Exceeded More Details
    Last executed input:
    "rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws"


Have to decide each character in the answer one at a time. Time Complexity is O(kn) where ``k`` is the
number of distinct characters in ``s`` and ``n`` is the length of ``s``.

The inner loop check goes all the way till lastInsertedIndex + 1.

.. code-block:: java

    public int TOCHECK = 0;
    public int CHECKED = -1;
    public int INSERTED = 1;

    public String removeDuplicateLetters(String s){

        int n = s.length();

        if(n == 0)
            return s;

        int numDistinct = 0;

        int[] states = new int['z'+1];

        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);

            if (states[c] == TOCHECK) {
                numDistinct++;
                states[c] = CHECKED;
            }
        }

        //System.out.println("numDistinct=" + numDistinct);
        StringBuffer sb = new StringBuffer();

        // no character inserted into sb yet
        int lastInsertedIndex = -1;

        // the answer will have numDistinct characters
        // we will be choosing each character one at a time
        for (int i=numDistinct; i>0; i--) {

            char minCh = 'z'+1;
            int tmpIndex = -1;
            numDistinct = 0;

            // reset states except chars already INSERTED into sb
            for (char c='a'; c<='z'; c++) {
                if (states[c] == CHECKED)
                    states[c] = TOCHECK;
            }

            for (int j=n-1; j>lastInsertedIndex; j--) {
                char c = s.charAt(j);

                if (states[c] == INSERTED)
                    continue;

                if (states[c] == TOCHECK) {
                    numDistinct++;
                }

                if (numDistinct == i) {
                    // means c is potential candidate to be inserted into sb
                    // note the EQUAL sign here: if we have two candidates of the same value
                    // the left most one is chosen to be inserted
                    if (c <= minCh) {
                        minCh = c;
                        tmpIndex  = j;
                    }
                }

                states[c] = CHECKED;
            }

            sb.append(minCh);
            states[minCh] = INSERTED;
            lastInsertedIndex = tmpIndex;

        } // for each character to be inserted into sb

        return sb.toString();
    }

