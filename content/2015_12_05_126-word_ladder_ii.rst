126-word_ladder_ii
##################

:date: 2015-12-5 16:39
:tags: Find All Shortest Paths, BFS, DFS, Two-Way BFS
:category: LeetCode
:slug: 126-word_ladder_ii

`LeetCode Problem Link <https://leetcode.com/problems/word-ladder-ii/>`_

We must first perform BFS find out the length of the shortest path. While doing this, we should
save the choices at each level. When we have found the length of the shortest path and the
choices at each level, we can then perform DFS to find all shortest paths. What info do we need
when we perform the DFS? We must know the neighbors of each word at each level. Therefore, it is important
that we build the neighbors as part of the BFS. I used a HashMap<String, HashSet> for this. The key is string in
question and its value is a HashSet of strings which are the neighbors of that string. This simply records the
neighboring relationship, it has nothing to do with the data structure that we use to prevent duplicates being
inserted onto the BFS queue.

.. code-block:: java

    // find all shortest transformations
    public List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordList) {

        List<String> q = new ArrayList<String>();
        HashSet<String> dup = new HashSet<String>();
        q.add(beginWord);

        int nextLevelSize = 0;
        int curLevelSize = 1;
        int levels = 0;
        int level = 1;

        List<List<String>> levelWords = new ArrayList<List<String>>();
        List<String> curLevelWords = new ArrayList<String>();

        HashMap<String, HashSet<String>> neighbors = new HashMap<String, HashSet<String>>();

        while (!q.isEmpty()) {

            String cur = q.remove(0);
            char[] arr = cur.toCharArray();
            curLevelWords.add(cur);

            for (int i=0; i<arr.length; i++) {
                char oldC = arr[i];

                for (char c='a'; c<='z'; c++) {
                    if (c == oldC)
                        continue;

                    arr[i] = c;


                    String modified = new String(arr);
                    boolean reachedEnd = modified.equals(endWord);

                    if (wordList.contains(modified) || reachedEnd) {
                        if (neighbors.containsKey(cur)) {
                            if (!neighbors.get(cur).contains(modified))
                                neighbors.get(cur).add(modified);
                        }
                        else {
                            HashSet<String> myNeighbors = new HashSet<String>();
                            myNeighbors.add(modified);
                            neighbors.put(cur, myNeighbors);
                        }

                        if (dup.contains(modified))
                            continue;

                        if (levels == 0 && reachedEnd) {
                            levels = level + 1;
                        }

                        q.add(modified);
                        dup.add(modified);

                        nextLevelSize++;
                    }

                }

                arr[i] = oldC;
            }

            curLevelSize--;

            if (curLevelSize==0) {
                levelWords.add(new ArrayList<String>(curLevelWords));
                curLevelWords.clear();

                curLevelSize = nextLevelSize;
                nextLevelSize = 0;
                level++;
                if (level == levels)
                    break;
            }
        }

        List<List<String>> ans = new ArrayList<List<String>>();
        dfs(levelWords, 0, new ArrayList<String>(), neighbors, ans, levels, endWord);
        return ans;
    }

    private void dfs(List<List<String>> levelWords, int index, List<String> curList,
                     HashMap<String, HashSet<String>> neighbors, List<List<String>> ans,
                     int levels, String endWord) {

        List<String> words = levelWords.get(index);

        int origSize = words.size();

        if (origSize == 0)
            return;

        String last = null;
        if (!curList.isEmpty()) {
            last = curList.get(curList.size() - 1);
        }

        for (int i=0; i<origSize; i++) {
            String s = words.get(i);

            if (last == null || neighbors.get(last).contains(s)) {
                curList.add(s);

                if (curList.size() < levels - 1) {
                    dfs(levelWords, index+1, curList, neighbors, ans, levels, endWord);
                }
                else {
                    if (neighbors.containsKey(s) && neighbors.get(s).contains(endWord)) {
                        curList.add(endWord);
                        ans.add(new ArrayList<String>(curList));
                        curList.remove(curList.size() - 1);
                    }
                }

                curList.remove(curList.size() - 1);
            }
        }
    }

This approach won't pass the large test case on OJ. If we decrease the number of choices at each level, the spent on
the DFS can be reduced (think exponential time complexity). The way we could decrease the number of choices at each
level is to perform BFS from the other end. Only the words that appear at that level from both times ar the choices
worth considering.

.. code-block:: java

    public List<List<String>> findLadders(
            String beginWord,
            String endWord,
            Set<String> wordList) {

        List<HashSet<String>> levelWords = new ArrayList<HashSet<String>>();

        List<String> q = new ArrayList<String>();
        HashSet<String> dup = new HashSet<String>();
        HashMap<String, HashSet<String>> neighbors =
                new HashMap<String, HashSet<String>>();

        q.add(beginWord);
        int curLevelSize = 1;
        int nextLevelSize = 0;
        int levels = 0;
        int level = 1;

        while (!q.isEmpty()) {
            String cur = q.remove(0);
            char[] arr = cur.toCharArray();

            for (int i=0; i<arr.length; i++) {
                char oldChar = arr[i];

                for (char c='a'; c<='z'; c++) {
                    if (c == oldChar)
                        continue;

                    arr[i] = c;
                    String modified = new String(arr);
                    boolean reachedEnd = modified.equals(endWord);

                    if (wordList.contains(modified) || reachedEnd) {
                        if (!neighbors.containsKey(cur))
                            neighbors.put(cur, new HashSet<String>());

                        if (!neighbors.get(cur).contains(modified))
                            neighbors.get(cur).add(modified);

                        if (dup.contains(modified)) {
                            continue;
                        }

                        if (reachedEnd && levels == 0) {
                            levels = level + 1;
                        }

                        q.add(modified);

                        if (!reachedEnd)
                            dup.add(modified);

                        nextLevelSize++;
                    }

                }

                arr[i] = oldChar;
            }

            curLevelSize--;

            if (levelWords.size() < level) {
                HashSet<String> words = new HashSet<String>();
                words.add(cur);
                levelWords.add(words);
            }
            else {
                levelWords.get(level-1).add(cur);
            }

            if (curLevelSize == 0) {
                if (levels > 0)
                    break;

                level++;
                curLevelSize = nextLevelSize;
                nextLevelSize = 0;
            }
        }

        List<List<String>> ans = new ArrayList<List<String>>();

        if (levels == 0)
            return ans;

        if (levels > 2) {
            q.clear();
            dup.clear();

            q.add(endWord);
            curLevelSize = 1;
            nextLevelSize = 0;
            level = 0;
            int index = levels - 2;
            HashSet<String> replacedWords = new HashSet<String>();

            while (!q.isEmpty()) {
                String cur = q.remove(0);
                char[] arr = cur.toCharArray();

                for (int i=0; i<arr.length; i++) {
                    char oldC = arr[i];

                    for (char c='a'; c<='z'; c++) {
                        if (c==oldC)
                            continue;

                        arr[i] = c;

                        String modified = new String(arr);
                        boolean reachedEnd = false;

                        if (level == levels - 1)
                            reachedEnd = modified.equals(beginWord);

                        if (wordList.contains(modified) || reachedEnd) {
                            if (dup.contains(modified))
                                continue;

                            if (levelWords.get(index).contains(modified)) {
                                replacedWords.add(modified);

                                q.add(modified);
                                dup.add(modified);
                                nextLevelSize++;
                            }
                        }
                    }

                    arr[i] = oldC;
                }

                curLevelSize--;

                if (curLevelSize == 0) {
                    if (index > 0) {
                        HashSet<String> oldWords = levelWords.get(index);
                        levelWords.set(index, replacedWords);
                        replacedWords = oldWords;
                    }

                    index--;
                    replacedWords.clear();

                    level++;
                    if (index < 0)
                        break;

                    curLevelSize = nextLevelSize;
                    nextLevelSize = 0;
                }
            }
        }
        dfs(levelWords, new ArrayList<String>(), neighbors, levels, 0, ans, endWord);

        return ans;
    }

    private void dfs(
            List<HashSet<String>> levelWords,
            List<String> curList,
            HashMap<String, HashSet<String>> neighbors,
            int levels,
            int index,
            List<List<String>> ans,
            String endWord) {

        HashSet<String> words = levelWords.get(index);

        for (String s: words) {

            String prevWord = null;

            if (!curList.isEmpty())
                prevWord = curList.get(curList.size() - 1);

            if (curList.isEmpty() || (neighbors.containsKey(prevWord) && neighbors.get(prevWord).contains(s))) {
                curList.add(s);

                if (curList.size() < levels - 1) {
                    dfs(levelWords, curList, neighbors, levels, index+1, ans, endWord);
                }
                else {
                    if (neighbors.get(s).contains(endWord)) {
                        curList.add(endWord);
                        ans.add(new ArrayList<String>(curList));
                        curList.remove(curList.size() - 1);
                    }
                }
                curList.remove(curList.size() - 1);
            }
        }
    }