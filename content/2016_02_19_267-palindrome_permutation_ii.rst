267-palindrome_permutation_ii
#############################

:date: 2016-2-19 10:44
:tags: Palindrome Permutation, Palindromes, Permutations
:category: LeetCode
:slug: 267-palindrome_permutation_ii

`LeetCode Problem Link <https://leetcode.com/problems/palindrome-permutation-ii/>`_

The problem is not so hard if you remember the precise implementation in 047-permutations_ii.

Also note that the strings in the returned list must all be palindromes.

.. code-block:: java

    // return all palindromic permutations
    public List<String> generatePalindromes(String s) {
        List<String> ans = new ArrayList<String>();

        List<Character> choices = new ArrayList<Character>();
        char[] odd = new char[1];

        if (!canPalindromePermute(s, choices, odd)) {
            return ans;
        }

        //System.out.println("choices: ");
        //System.out.println(choices);

        int n = s.length();

        List<String> permutations = getUniquePermutations(choices);

        for (String str: permutations) {
            StringBuffer sb = new StringBuffer(str);
            if (choices.size() * 2 == n) {
                String p = str + sb.reverse();
                ans.add(p);
            }
            else {
                String p = str + odd[0] + sb.reverse();
                ans.add(p);
            }
        }



        return ans;
    }

    private List<String> getUniquePermutations(List<Character> choices) {
        List<String> ans = new ArrayList<String>();
        Collections.sort(choices);
        boolean[] tried = new boolean[choices.size()];
        getPermutation(choices, tried, new StringBuffer(), ans);

        return ans;
    }

    private void getPermutation(List<Character> choices,
                                boolean[] tried,
                                StringBuffer sb,
                                List<String> ans) {

        if (sb.length() == choices.size()) {
            ans.add(sb.toString());
            return;
        }

        for (int i=0; i<choices.size(); i++) {
            if (!tried[i]) {
                if (i-1 >=0 && choices.get(i) == choices.get(i-1) && !tried[i-1]) {
                    continue;
                }
                tried[i] = true;
                sb.append(choices.get(i));
                getPermutation(choices, tried, sb, ans);
                sb.deleteCharAt(sb.length()-1);
                tried[i] = false;
            }
        }

    }

    private boolean canPalindromePermute(String s, List<Character> choices, char[] odd) {
        HashMap<Character, Integer> frequency = new HashMap<Character, Integer>();

        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);

            if (frequency.containsKey(c)) {
                frequency.put(c, frequency.get(c) + 1);
            }
            else {
                frequency.put(c, 1);
            }
        }

        int oddCnt = 0;

        for(char c: frequency.keySet()) {
            if (frequency.get(c) % 2 == 1) {
                oddCnt++;
                odd[0] = c;

                for (int i=0; i<(frequency.get(c)-1)/2; i++)
                    choices.add(c);
            }
            else {
                for (int i=0; i<frequency.get(c)/2; i++)
                    choices.add(c);
            }
        }

        return oddCnt==0 || oddCnt==1;
    }
