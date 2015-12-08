130-surrounded_regions
######################

:date: 2015-12-8 13:02
:tags: DFS, Blob Analysis
:category: LeetCode
:slug: 130-surrounded_regions

`LeetCode Problem Link <https://leetcode.com/problems/surrounded-regions/>`_

This is the recursive solution. Go through all 'O's at the edge and recursive mark its connected 'O' cells to 'o'.
These 'O's cannot be enclosed by 'X'. Once this is done, go through the board again, mark all other 'O's to 'X' and
change 'o's to 'O's.

This will pass the large test case though. The following the blob analysis solution. For each blob, we are keeping
track of the ``xMin``, ``xMax``, ``yMin``, and ``yMax``. We can tell if the blob of 'O's are touching the edge. If not,
they will be changed to 'X's.

.. code-block:: java

public class Solution {

    class BlobProperties {
        int xMin;
        int xMax;
        int yMin;
        int yMax;
    }

    /*    U
     *  L X
     */

    // the 2D char array contains only 'O' and 'X'
    // Eat up all regions of 'O's that are surrounded by 'X's
    public void solve(char[][] board) {
        int m = board.length;

        if (m < 1)
            return;

        int n = board[0].length;

        int[][] blobs = new int[m][n];

        int blobNum = 1;
        HashMap<Integer, Integer> lookup = new HashMap<Integer, Integer>();

        for (int row=0; row<m; row++) {
            for(int col=0; col<n; col++) {
                if (board[row][col] == 'O') {
                    int topBlob = 0;
                    int leftBlob = 0;

                    if (row - 1 >= 0 && board[row-1][col] == 'O')
                        topBlob = blobs[row-1][col];

                    if (col - 1 >= 0 && board[row][col-1] == 'O')
                        leftBlob = blobs[row][col-1];

                    if (topBlob > 0 &&  leftBlob > 0) {
                        int top = topBlob;
                        int left = leftBlob;
                        while (lookup.containsKey(top))
                            top = lookup.get(top);

                        while (lookup.containsKey(left))
                            left = lookup.get(left);

                        int smallerBlobNum = Math.min(top, left);

                        blobs[row][col] = smallerBlobNum;

                        if (smallerBlobNum < top)
                            lookup.put(top, smallerBlobNum);
                        if (smallerBlobNum < left)
                            lookup.put(left, smallerBlobNum);
                    }
                    else if (topBlob == 0 && leftBlob == 0) {
                        // use a brand new blob number
                        blobs[row][col] = blobNum;
                        blobNum++;
                    }
                    else if (topBlob > 0) {
                        while (lookup.containsKey(topBlob))
                            topBlob = lookup.get(topBlob);

                        blobs[row][col] = topBlob;
                    }
                    else if (leftBlob > 0) {
                        while (lookup.containsKey(leftBlob))
                            leftBlob = lookup.get(leftBlob);

                        blobs[row][col] = leftBlob;
                    }
                }
            }
        }

        int maxBlobNum = 0;

        for (int row=0; row<m; row++) {
            for(int col=0; col<n; col++) {
                if (blobs[row][col] > 0) {
                    int b = blobs[row][col];

                    while (lookup.containsKey(b))
                        b = lookup.get(b);

                    if (b > maxBlobNum)
                        maxBlobNum = b;

                    blobs[row][col] = b;
                }
            }
        }

        BlobProperties[] properties = new BlobProperties[maxBlobNum];
        for (int i=0; i<properties.length; i++) {
            BlobProperties b = new BlobProperties();
            b.xMax = Integer.MIN_VALUE;
            b.yMax = Integer.MIN_VALUE;
            b.xMin = Integer.MAX_VALUE;
            b.yMin = Integer.MAX_VALUE;
            properties[i] = b;
        }

        for (int row=0; row<m; row++) {
            for(int col=0; col<n; col++) {
                if (blobs[row][col] > 0) {
                    int b = blobs[row][col];

                    if (row < properties[b-1].yMin)
                        properties[b-1].yMin = row;
                    if (row > properties[b-1].yMax)
                        properties[b-1].yMax = row;
                    if (col < properties[b-1].xMin)
                        properties[b-1].xMin = col;
                    if (col > properties[b-1].xMax)
                        properties[b-1].xMax = col;
                }
            }
        }

        for (int row=0; row<m; row++) {
            for(int col=0; col<n; col++) {
                int b = blobs[row][col];

                if (b > 0) {
                    BlobProperties prop = properties[b-1];
                    if (prop.xMin != 0 && prop.yMin != 0 &&
                        prop.xMax != n-1 && prop.yMax != m-1) {
                        board[row][col] = 'X';
                    }
                }
            }
        }
    }


    public static void main(String[] args) {

        char[][] board = {{'O', 'O', 'O', 'O', 'X', 'X'},
                          {'O', 'O', 'O', 'O', 'O', 'O'},
                          {'O', 'X', 'O', 'X', 'O', 'O'},
                          {'O', 'X', 'O', 'O', 'X', 'O'},
                          {'O', 'X', 'O', 'X', 'O', 'O'},
                          {'O', 'X', 'O', 'O', 'O', 'O'}};

        Solution sol = new Solution();

        sol.solve(board);

        System.out.println(Arrays.deepToString(board));
    }

}
