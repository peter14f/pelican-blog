068-text_justification
######################

:date: 2015-10-30 23:18
:tags:
:category: LeetCode
:slug: 068-text_justification

`LeetCode Problem Link <https://leetcode.com/problems/text-justification/>`_

A tedious problem for sure. The last line doesn't require adding extra spaces at all. That's why I wrote two
different helper methods **justifyOneLine()** and **justifyLastLine()** one for all other lines, and the other
for the last line.

However, for the other lines, if we only have one word in the line, we are simply adding spaces at the
end of the word until the length reaches **maxWidth**. Therefore, for these cases, I'm also calling
**justifyLastLine()**.

.. code-block:: java

    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> ans = new ArrayList<String>();
        int curLength = -1;
        ArrayList<String> curList = new ArrayList<String>();

        for (int i=0; i<words.length; i++) {
            String s = words[i];
            if (curLength + 1 + s.length() <= maxWidth) {
                curLength += 1 + s.length();
                curList.add(s);
            }
            else {
                if (curList.size() > 1)
                    justifyOneLine(curList, maxWidth, curLength, ans);
                else
                    justifyLastLine(curList, maxWidth, ans);

                curLength = s.length();
                curList.clear();
                curList.add(s);
            }
        }

        if (!curList.isEmpty()) {
            justifyLastLine(curList, maxWidth, ans);
        }

        return ans;
    }

    private void justifyLastLine(ArrayList<String> curList, int maxWidth,
                                 List<String> ans) {

        StringBuffer sb = new StringBuffer();
        int n = curList.size();
        int i = 0;
        int length = 0;

        for (String s: curList) {
            sb.append(s);
            length += s.length();
            if (i < n-1) {
                sb.append(' ');
                length++;
            }
        }

        while (length < maxWidth) {
            sb.append(' ');
            length++;
        }

        ans.add(sb.toString());
    }

    private void justifyOneLine(ArrayList<String> curList, int maxWidth,
                                int curLength, List<String> ans) {
        int cnt = curList.size();
        int[] spaces = new int[cnt - 1];

        for (int i=0; i<spaces.length; i++) {
            spaces[i] = 1;
        }

        int i = 0;
        while (curLength < maxWidth) {
            spaces[i]++;
            curLength++;

            i++;
            i = i % (spaces.length);
        }

        StringBuffer sb = new StringBuffer();
        i=0;
        for (String s: curList) {
            sb.append(s);
            if (i < spaces.length) {
                for (int j=0; j<spaces[i]; j++)
                    sb.append(' ');
            }
            i++;
        }
        ans.add(sb.toString());
    }
