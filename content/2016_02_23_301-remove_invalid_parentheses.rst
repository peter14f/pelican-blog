301-remove_invalid_parentheses
##############################

:date: 2016-2-23 15:43
:tags: BFS
:category: LeetCode
:slug: 301-remove_invalid_parentheses

`LeetCode Problem Link <https://leetcode.com/problems/remove-invalid-parentheses/>`_

1) Remove the **minimum number** of parentheses such that the result is valid.
2) Find the valid results when you remove **minimum number** of parentheses.


For step 1, I think using BFS, it's possible find the **minimum number** ``x``.

Once ``x`` is found, continue with BFS and stop addting strings if the number of characters removed has exceeded
``x``.

This should help us find all valid strings with ``x`` characters removed. The API expects us return a List<String>
so we have to be careful not to add duplicated strings there. What I did was to use a HashSet<String> to
prevent duplicates.

.. code-block:: java

    class Entry {
        StringBuffer str;
        int numRemoved;

        public Entry(StringBuffer sb, int num) {
            str = sb;
            numRemoved = num;
        }
    }

    public List<String> removeInvalidParentheses(String s) {

        Queue<Entry> q = new LinkedList<Entry>();
        q.offer(new Entry(new StringBuffer(s), 0));

        HashSet<String> ansSet = new HashSet<String>();
        List<String> ans = new ArrayList<String>();
        int minRemove = 0;

        while (!q.isEmpty()) {
            Entry ent = q.poll();

            /*
            System.out.println("str=" + ent.str +
                    " valid=" + isValid(ent.str) +
                    " num=" + ent.numRemoved);
            */

            if (isValid(ent.str)) {
                if (minRemove==0) {
                    if (ent.numRemoved == 0) {
                        ans.add(ent.str.toString());
                        return ans;
                    }
                    else {
                        minRemove = ent.numRemoved;
                        ansSet.add(ent.str.toString());
                    }
                }
                else {
                    if (ent.numRemoved == minRemove) {
                        String str = ent.str.toString();
                        if (!ansSet.contains(str))
                            ansSet.add(str);
                    }
                }
            }
            else {

                if (minRemove > 0 && ent.numRemoved >= minRemove) {
                    continue;
                }

                for (int i=0; i<ent.str.length(); i++) {

                    char cToDelete = ent.str.charAt(i);

                    if (cToDelete == '(' || cToDelete == ')') {
                        ent.str.deleteCharAt(i);
                        //System.out.println("  " + i + " removed -> " + ent.str);
                        Entry newEnt = new Entry(new StringBuffer(ent.str), ent.numRemoved + 1);
                        ent.str.insert(i, cToDelete);
                        //System.out.println("  " + i + " recovered -> " + ent.str);
                        q.offer(newEnt);
                    }
                }
            }
        }

        ans.addAll(ansSet);
        return ans;
    }

    private boolean isValid(StringBuffer sb) {
        if (sb.length() == 0)
            return true;

        Stack<Integer> openIndex = new Stack<Integer>();

        for (int i=0; i<sb.length(); i++) {
            char c = sb.charAt(i);
            if (c == '(')
                openIndex.push(i);
            else if (c == ')') {
                if (openIndex.isEmpty())
                    return false;
                openIndex.pop();
            }
        }

        return openIndex.isEmpty();
    }

Was hoping that would pass OJ. But got TLE.

::

    Submission Result: Time Limit Exceeded More Details

    Last executed input:
    ")()))())))"


The mistake here is something I often make while implementing a BFS search. We want to limit the number of items
put on the queue.

**An item should be put on the queue only if the has never been put on the queue before.**

So we can use a ``HashSet<String>`` called ``visited`` to record what has been put on the queue.

We check before we put an item on the queue if the item is in ``visited`` already. We only put the item into the
queue if it's not in ``visited``. And once we put the item on the queue, we need to immediately add the item into
``visited`` as well.

In other words, the code that checks for the existence in ``visited`` and the code to add item into ``visited`` should
be right next to each other.

.. code-block:: java

    class Entry {
        StringBuffer str;
        int numRemoved;

        public Entry(StringBuffer sb, int num) {
            str = sb;
            numRemoved = num;
        }
    }

    public List<String> removeInvalidParentheses(String s) {

        Queue<Entry> q = new LinkedList<Entry>();
        q.offer(new Entry(new StringBuffer(s), 0));

        HashSet<String> ansSet = new HashSet<String>();
        List<String> ans = new ArrayList<String>();
        int minRemove = 0;

        HashSet<String> visited = new HashSet<String>();

        while (!q.isEmpty()) {
            Entry ent = q.poll();

            /*
            System.out.println("str=" + ent.str +
                    " valid=" + isValid(ent.str) +
                    " num=" + ent.numRemoved);
            */

            if (isValid(ent.str)) {
                if (minRemove==0) {
                    if (ent.numRemoved == 0) {
                        ans.add(ent.str.toString());
                        return ans;
                    }
                    else {
                        minRemove = ent.numRemoved;
                        ansSet.add(ent.str.toString());
                    }
                }
                else {
                    if (ent.numRemoved == minRemove) {
                        String str = ent.str.toString();
                        if (!ansSet.contains(str))
                            ansSet.add(str);
                    }
                }
            }
            else {

                if (minRemove > 0 && ent.numRemoved >= minRemove) {
                    continue;
                }

                for (int i=0; i<ent.str.length(); i++) {

                    char cToDelete = ent.str.charAt(i);

                    if (cToDelete == '(' || cToDelete == ')') {
                        ent.str.deleteCharAt(i);
                        String temp = ent.str.toString();
                        if (!visited.contains(temp)) {
                            //System.out.println("  " + i + " removed -> " + ent.str);
                            Entry newEnt = new Entry(new StringBuffer(ent.str), ent.numRemoved + 1);
                            //System.out.println("  " + i + " recovered -> " + ent.str);
                            q.offer(newEnt);

                            visited.add(temp);
                        }

                        ent.str.insert(i, cToDelete);
                    }
                }
            }
        }

        ans.addAll(ansSet);
        return ans;
    }

    private boolean isValid(StringBuffer sb) {
        if (sb.length() == 0)
            return true;

        Stack<Integer> openIndex = new Stack<Integer>();

        for (int i=0; i<sb.length(); i++) {
            char c = sb.charAt(i);
            if (c == '(')
                openIndex.push(i);
            else if (c == ')') {
                if (openIndex.isEmpty())
                    return false;
                openIndex.pop();
            }
        }

        return openIndex.isEmpty();
    }

This will finally pass OJ. And the last thing to change is the method ``isValid``. A stack is actually not
necessary. Just use a counter variable to count how many open parentheses we have seen so far.

.. code-block:: java

    private boolean isValid(StringBuffer sb) {
        if (sb.length() == 0)
            return true;

        int openCnt = 0;

        for (int i=0; i<sb.length(); i++) {
            char c = sb.charAt(i);
            if (c == '(')
                openCnt++;
            else if (c == ')') {
                if (openCnt==0)
                    return false;
                openCnt--;
            }
        }

        return openCnt == 0;
    }
