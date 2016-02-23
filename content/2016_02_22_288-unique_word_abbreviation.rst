288-unique_word_abbreviation
############################

:date: 2016-2-22 17:08
:tags:
:category:
:slug: 288-unique_word_abbreviation
:status: draft

`LeetCode Problem Link <https://leetcode.com/problems/unique-word-abbreviation/>`_

The given word is unique iff no *other* words have the same abbreviation.

So we need to be able to determine if ``word`` is in the dictionary. ---> ``HashSet<String>``

We need to be able to find the abbreviation of any word. ---> ``getAbbr()``

.. code-block:: java

    public class ValidWordAbbr {

    HashMap<String, Integer> abbrs;
    HashSet<String> words;

    public ValidWordAbbr(String[] dictionary) {
        words = new HashSet<String>();
        abbrs = new HashMap<String, Integer>();

        for (int i=0; i<dictionary.length; i++) {
            if (!words.contains(dictionary[i])) {
                words.add(dictionary[i]);

                String abbrStr = getAbbr(dictionary[i]);

                if (!abbrs.containsKey(abbrStr))
                    abbrs.put(abbrStr, 1);
                else
                    abbrs.put(abbrStr,
                              abbrs.get(abbrStr)+1);
            }
        }
    }

    public boolean isUnique(String word) {
        String abbr = getAbbr(word);

        if (words.contains(word)) {
            return abbrs.get(abbr) == 1;
        }
        else {
            return !abbrs.containsKey(abbr);
        }
    }

    private String getAbbr(String s) {
        int n = s.length();

        if (n > 2) {
            StringBuffer sb = new StringBuffer();
            sb.append(s.charAt(0));
            sb.append(n-2);
            sb.append(s.charAt(n-1));
            return sb.toString();
        }
        else {
            return s;
        }
    }

    public static void main(String[] args) {
        String[] strs = {
                "deer",
                "door",
                "cake",
                "card"
        };
        ValidWordAbbr chk = new ValidWordAbbr(strs);

        System.out.println(chk.isUnique("caad"));

    }

}

