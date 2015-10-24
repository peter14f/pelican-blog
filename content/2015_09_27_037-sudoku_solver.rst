037-sudoku_solver
#################

:date: 2015-09-27 10:49
:tags: Recursion, NP, DFS
:category: LeetCode
:slug: 037-sudoku_solver

`LeetCode Problem Link <https://leetcode.com/problems/sudoku-solver/>`_

We will have to backtrack using a stack. Here are the information that we need when backtracking:

| 1) to which cell are we backtracking to?
| 2) what other numbers can we choose from now?


.. code-block:: java

    public class Solution {

        public static final int SIZE = 9;
        public static final int SUBSIZE = 3;

        class Cell {
            int row;
            int col;
            HashSet<Character> numbers;

            public Cell(int row, int col, char[][] board) {
                this.row = row;
                this.col = col;

                numbers = new HashSet<Character>();
                for (int i=1; i<=SIZE; i++) {
                    numbers.add((char) ('0' + i));
                }

                // numbers already in the row
                for (int i=0; i<SIZE; i++) {
                    if (numbers.contains(board[row][i])) {
                        numbers.remove(board[row][i]);
                    }
                }

                // numbers already in the column
                for (int i=0; i<SIZE; i++) {
                    if (numbers.contains(board[i][col])) {
                        numbers.remove(board[i][col]);
                    }
                }

                // numbers already in the subboard
                int subboardRow = (row/SUBSIZE)*SUBSIZE;
                int subboardCol = (col/SUBSIZE)*SUBSIZE;

                for (int i=0; i<SUBSIZE; i++) {
                    for (int j=0; j<SUBSIZE; j++) {
                        if (numbers.contains(board[subboardRow+i][subboardCol+j])) {
                            numbers.remove(board[subboardRow+i][subboardCol+j]);
                        }
                    }
                }
            }
        }

        public void solveSudoku(char[][] board) {

            Stack<Cell> stk = new Stack<Cell>();

            // find blank cells
            for (int row=0; row<SIZE; row++) {
                for (int col=0; col<SIZE; col++) {
                    if (board[row][col] == '.') {
                        Cell cell = new Cell(row, col, board);

                        if (cell.numbers.isEmpty()) {
                            // time to backtrack
                            do {
                                if (stk.isEmpty())
                                    throw new IllegalArgumentException("board cannot be solved");

                                cell = stk.pop();
                                board[cell.row][cell.col] = '.';

                            } while (cell.numbers.isEmpty());

                            row = cell.row;
                            col = cell.col;
                        }

                        char choice = cell.numbers.iterator().next();
                        board[row][col] = choice;
                        cell.numbers.remove(choice);
                        stk.push(cell);
                    }
                }
            }
        }
    }