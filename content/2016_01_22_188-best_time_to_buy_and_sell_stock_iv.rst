188-best_time_to_buy_and_sell_stock_iv
######################################

:date: 2016-1-22 15:19
:tags: Best Time To Buy/Sell, Dynamic Programming
:category: LeetCode
:slug: 188-best_time_to_buy_and_sell_stock_iv

`LeetCode Problem Link <https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/>`_

Before we make any trade, our cash position is ``0``.
Buying a stock at price ``p`` reduces our cash position to ``-p``.
Selling a stock at price ``z`` increases our cash position to ``(-p + z)``.
And the final cash position we're left with is the profit we make.

``allPositionClosed[i][j]`` is the maximum cash position we have at j-th day with at most
``i`` trades and considering prices 0, ..., j. All we have is cash.

When we encounter a new price at j-th day, we can choose to sell the stock at j-th day or
be content with the cash position we have so far.

``minEffectOneNakedBuy`` is the minimum effect on the cash position when we make one buy on
any day in the past. ``t`` is the current day.

.. code-block:: java

    public int maxProfit(int k, int[] prices) {
        int n = prices.length;

        if (k >= n/2)
            return maxProfitAsMany(prices);

        /* before we make any trade, our cash position is 0
         * buying a stock at price p reduces our cash position to -p
         * selling a stock at price z increases our cash position to (-p + z)
         * and the final cash position we're left with is the profit we make
         */

        /* allPositionClosed[i][j] - the max profit we have realized at j-th day with at most
         * i trades, and all we hold is cash.
         *
         * at j-th day, we can choose to use and not use the j-th price.
         *
         * If we do not use the j-th price, then we have cash position allPositionClosed[i][j-1],
         * i.e., yesterday's cash position.
         *
         * If we choose the j-th price, we must pair it with a previous naked buy position because
         * we want to exit with cash and without any stocks.
         *
         * minEffectOneNakedBuy + prices[j] precisely does this. Here we use "+" because after sell,
         * we keep prices[j] in pocket
         *
         */
        int[][] allPositionClosed = new int[k+1][n];

        /* minEffectOneNakedBuy - the minimum effect on our cash position when we hold a single
         * buy position considering the prices in the past
         *
         * t is the current day
         *
         *  (remember, buy always lowers our cash position, that's why oneNakedBuyPosition is
         *  initialized to -prices[0], indicated exactly by its name, after we open a naked buy,
         *  it lowers our cash position to -prices[0].)
         *
         */

        for (int m=1; m<=k; m++) {
            int minEffectOneNakedBuy = -prices[0];

            for (int t=1; t<prices.length; t++) {
                allPositionClosed[m][t] = Math.max(allPositionClosed[m][t-1],
                                                   minEffectOneNakedBuy + prices[t]);
                minEffectOneNakedBuy = Math.max(minEffectOneNakedBuy,
                                                allPositionClosed[m-1][t-1] - prices[t]);
            }
        }

        return allPositionClosed[k][prices.length-1];
    }

    private int maxProfitAsMany(int[] prices) {
        int profit = 0;
        for (int i=1; i<prices.length; i++) {
            if (prices[i] - prices[i-1] > 0) {
                profit += prices[i] - prices[i-1];
            }
        }
        return profit;
    }


Another way to think of the problem.
My solution to 309-best_time_to_buy_and_sell_stock_with_cooldown is closer to this one.

.. code-block:: java

    // at most k transactions
    public int maxProfit(int k, int[] prices) {

        int n = prices.length;

        // with n prices, you can make at most n/2 trades
        // if k >= n/2, it's equivalent to being able to
        // make a unlimited number of trades
        if (k >= n/2)
            return maxProfitAsMany(prices);

        if (n==0 || k==0)
            return 0;

        // buy[i][j] is the max profit on day j with at most i transactions
        //           with stock position in hand
        int[][] maxProfitBuy = new int[k+1][n];

        // sell[i][j] is the max profit on day i with at most i transactions
        //            with no stock position in hand
        //
        int[][] maxProfitSell = new int[k+1][n];

        for (int i=1; i<=k; i++) {
            // making at most i transactions

            maxProfitBuy[i][0] = -prices[0];

            for (int j=1; j<n; j++) {

                // be content with the profit I held yesterday or
                // sell at today
                maxProfitSell[i][j] = Math.max(
                        maxProfitSell[i][j-1],
                        maxProfitBuy[i][j-1] + prices[j]);

                maxProfitBuy[i][j] = Math.max(maxProfitBuy[i][j-1],
                                              maxProfitSell[i-1][j-1] - prices[j]);
            }
        }

        return maxProfitSell[k][n-1];
    }

    private int maxProfitAsMany(int[] prices) {
        int profit = 0;

        for (int i=1; i<prices.length; i++) {
            if (prices[i] > prices[i-1]) {
                profit += prices[i] - prices[i-1];
            }
        }

        return profit;
    }