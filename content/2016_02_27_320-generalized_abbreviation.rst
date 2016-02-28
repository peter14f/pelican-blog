320-generalized_abbreviation
############################

:date: 2016-2-27 13:30
:tags: DFS, Recursion
:category: LeetCode
:slug: 320-generalized_abbreviation

`LeetCode Problem Link <https://leetcode.com/problems/generalized-abbreviation/>`_

The list of generalized abbreviations for the word ``word`` is

::

    ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]


So just by looking at the example, I am assuming an integer simply means the number of characters it represents.

And it sure looks like you cannot have two integers next to each other. Notice that we have ``1o1d`` but not ``11rd``.

I think we can use recursion and DFS.

My first attempt

.. code-block:: java

    public List<String> generateAbbreviations(String word) {
        List<String> ans = new ArrayList<String>();

        StringBuffer sb = new StringBuffer(word);

        findAllAbbreviations(sb, 0, ans);

        return ans;
    }

    private void findAllAbbreviations(StringBuffer sb, int i, List<String> ans) {

        if (i>=sb.length()) {
            ans.add(sb.toString());
            return;
        }

        // when arriving at a new letter we have two choices
        // choice 1: do not replace the current letter
        findAllAbbreviations(sb, i+1, ans);



        // choice 2: replace the current letter
        int n = sb.length();


        for (int num=n-i; num > 0; num--) {
            String before = sb.substring(i, i+num-1);
            char replaced = sb.charAt(i+num-1);

            sb.setCharAt(i+num-1, (char)('0' + num));
            sb.delete(i, i+num-1);

            //System.out.println("a=" + sb.toString());

            findAllAbbreviations(sb, i+2, ans);

            sb.insert(i, before);
            sb.setCharAt(i+num-1, replaced);

            //System.out.println("b=" + sb.toString());
        }
    }

This works for strings of size < 10.

.. code-block:: java

    public List<String> generateAbbreviations(String word) {
        List<String> ans = new ArrayList<String>();

        StringBuffer sb = new StringBuffer(word);

        findAllAbbreviations(sb, 0, ans);

        return ans;
    }

    private void findAllAbbreviations(StringBuffer sb, int i, List<String> ans) {

        if (i>=sb.length()) {
            ans.add(sb.toString());
            return;
        }

        // when arriving at a new letter we have two choices
        // choice 1: do not replace the current letter
        findAllAbbreviations(sb, i+1, ans);



        // choice 2: replace the current letter
        int n = sb.length();


        for (int num=n-i; num > 0; num--) {

            String s = Integer.toString(num);
            int numLen = s.length();

            String before = sb.substring(i, i+num-numLen);
            String replaced = sb.substring(i+num-numLen, i+num);

            sb.replace(i+num-numLen, i+num, s);
            sb.delete(i, i+num-numLen);

            //System.out.println("a=" + sb.toString());

            findAllAbbreviations(sb, i+numLen+1, ans);

            sb.insert(i, before);
            sb.replace(i+num-numLen, i+num, replaced);

            //System.out.println("b=" + sb.toString());
        }
    }