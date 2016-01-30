212-word_search_ii
##################

:date: 2016-1-30 15:55
:tags: Trie, DFS, Boggle
:category: LeetCode
:slug: 212-word_search_ii

`LeetCode Problem Link <https://leetcode.com/problems/word-search-ii/>`_

Doing DFS to try to find each word in the dictionary will result in TLE.

.. code-block:: java

    public List<String> findWords(char[][] board, String[] words) {
        List<String> ans = new ArrayList<String>();

        for (int i=0; i<words.length; i++) {
            if (canFindWord(board, words[i])) {
                ans.add(words[i]);
            }
        }

        return ans;
    }

    private boolean canFindWord(char[][] board, String word) {
        if (word.length() == 0)
            return true;

        int m = board.length;
        int n = board[0].length;
        int index = 0;

        for (int row=0; row<m; row++) {
            for (int col=0; col<n; col++) {
                if (board[row][col] == word.charAt(index)) {
                    boolean[][] visited = new boolean[m][n];
                    visited[row][col] = true;
                    if (dfs(board, row, col, word, visited, index + 1))
                        return true;
                }
            }
        }

        return false;
    }

    private boolean dfs(char[][] board, int row, int col,
                        String word, boolean[][] visited, int index) {
        if (index == word.length())
            return true;

        int m = board.length;
        int n = board[0].length;

        char ch = word.charAt(index);

        boolean up = false;
        boolean down = false;
        boolean left = false;
        boolean right = false;

        if (row-1 >= 0 && !visited[row-1][col] && board[row-1][col] == ch) {
            visited[row-1][col] = true;
            up = dfs(board, row-1, col, word, visited, index+1);
            visited[row-1][col] = false;

            if (up)
                return true;
        }

        if (row+1 < m && !visited[row+1][col] && board[row+1][col] == ch) {
            visited[row+1][col] = true;
            down = dfs(board, row+1, col, word, visited, index+1);
            visited[row+1][col] = false;

            if (down)
                return true;
        }

        if (col-1 >= 0 && !visited[row][col-1] && board[row][col-1] == ch) {
            visited[row][col-1] = true;
            left = dfs(board, row, col-1, word, visited, index+1);
            visited[row][col-1] = false;

            if (left)
                return true;
        }

        if (col+1 < n && !visited[row][col+1] && board[row][col+1] == ch) {
            visited[row][col+1] = true;
            right = dfs(board, row, col+1, word, visited, index+1);
            visited[row][col+1] = false;
            if (right)
                return true;
        }

        return false;
    }

Instead we can store the words in the dictionary in a Trie first and then form words from each location in
the board. When a prefix is not found in the Trie, we can stop and move to the next starting position.

.. code-block:: java

    class TrieNode {
        TrieNode[] children;
        boolean isLeaf;

        public TrieNode() {
            children = new TrieNode[26];
            isLeaf = false;
        }
    }

    class Trie {
        TrieNode root;

        public Trie() {
            root = new TrieNode();
        }

        public boolean hasPrefix(String prefix) {
            TrieNode cur = root;

            for (int i=0; i<prefix.length(); i++) {
                char c = prefix.charAt(i);
                if (cur.children[c-'a'] == null)
                    return false;
                cur = cur.children[c-'a'];
            }

            return true;
        }

        public boolean hasWord(String word) {
            TrieNode cur = root;

            for (int i=0; i<word.length(); i++) {
                char c = word.charAt(i);
                if (cur.children[c-'a'] == null)
                    return false;
                cur = cur.children[c-'a'];
            }

            return cur.isLeaf;
        }

        public void AddWord(String word) {
            TrieNode cur = root;
            for (int i=0; i<word.length(); i++) {
                char c = word.charAt(i);

                if (cur.children[c-'a'] == null)
                    cur.children[c-'a'] = new TrieNode();

                cur = cur.children[c-'a'];
            }
            cur.isLeaf = true;
        }
    }

    Trie t;

    public SolutionTrie() {
        t = new Trie();
    }

    public List<String> findWords(char[][] board, String[] words) {
        List<String> ans = new ArrayList<String>();
        HashSet<String> a = new HashSet<String>();

        int m = board.length;
        if (m == 0)
            return ans;
        int n = board[0].length;

        for (int i=0; i<words.length; i++) {
            String w = words[i];
            t.AddWord(w);
        }

        boolean[][] visited = new boolean[m][n];
        StringBuffer sb = new StringBuffer();

        for (int row=0; row<m; row++) {
            for (int col=0; col<n; col++) {
                findWord(board, sb, row, col, visited, a);
            }
        }

        for (String s: a) {
            ans.add(s);
        }

        return ans;
    }

    private void findWord(char[][] board,
            StringBuffer sb, int row, int col,
            boolean[][] visited, HashSet<String> a) {

        int m = board.length;
        int n = board[0].length;
        int oldLength = sb.length();
        sb.append(board[row][col]);

        if (!t.hasPrefix(sb.toString())) {
            sb.setLength(oldLength);
            return;
        }

        if (t.hasWord(sb.toString()))
            a.add(sb.toString());

        visited[row][col] = true;

        if (row-1 >=0 && visited[row-1][col]==false) {
            findWord(board, sb, row-1, col, visited, a);
        }

        if (row+1 < m && visited[row+1][col]==false) {
            findWord(board, sb, row+1, col, visited, a);
        }

        if (col-1 >=0 && visited[row][col-1]==false) {
            findWord(board, sb, row, col-1, visited, a);
        }

        if (col+1 < n && visited[row][col+1]==false) {
            findWord(board, sb, row, col+1, visited, a);
        }

        visited[row][col] = false;
        sb.setLength(oldLength);
    }
