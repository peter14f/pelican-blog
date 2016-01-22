121-best_time_to_buy_and_sell_stock
###################################

:date: 2015-11-30 22:11
:tags:
:category: LeetCode
:slug: 121-best_time_to_buy_and_sell_stock

`LeetCode Problem Link <https://leetcode.com/problems/best-time-to-buy-and-sell-stock/>`_

In this problem, we're only allowed to make one trade. That means we can only buy once at time ``i`` and then
sell once at time ``j`` where ``j>i``.
Keep track of the ``maxProfit`` and ``buyIndex``. Update ``buyIndex`` if current price is lower than price at
``buyIndex``. This take O(n) time.

.. code-block:: java

    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int buyIndex = 0;

        for (int i=1; i<prices.length; i++) {

            if (prices[i] < prices[buyIndex]) {
                buyIndex = i;
            }

            if (prices[i] - prices[buyIndex] > maxProfit) {
                maxProfit = prices[i] - prices[buyIndex];
            }
        }

        return maxProfit;
    }

Here is another way to think about the problem. This will help us later when we do
188-best_time_to_buy_and_sell_stock_iv.

Before we make any trade, our cash position is ``0``. Buying the stock at price ``p`` reduces our cash position to a
negative number ``-p``. Selling the stock at price ``j`` increases our cash position from ``-p`` to ``-p + j``.

The cash position we are left with will be the profit.

.. code-block:: java

    public int maxProfit(int[] prices) {
        if (prices.length < 2)
            return 0;

        /* before we make any trade, our cash position is 0
         * buying a stock reduces our cash position to a negative number
         * selling a stock increases our cash position and the final cash
         * position we're left with is the profit we make
         */
        int n = prices.length;

        /* allPositionClose[i] is the maximum cash position considering prices
         * 0, ..., i.
         */
        int[] allPositionClosed = new int[n];

        /* the minimum effect on our cash position considering all prices in the past
         * (t is current day)
         */
        int oneNakedBuy = -prices[0];

        for (int t=1; t<n; t++) {
            /* so whenever we encounter a new stock price, we can choose to sell the stock
             * at this price
             *
             * OR
             *
             * ignore the stock price and be content with the cash position we have so far
             */

            allPositionClosed[t] = Math.max(allPositionClosed[t-1], oneNakedBuy + prices[t]);

            /* so either a buy in the past yields a lower impact on the cash position or
             * a buy in this new price yields a lower impact on the cash position
             *
             * remember the larger negative number is the one that yields a smaller impact
             * on our cash position
             */
            oneNakedBuy = Math.max(oneNakedBuy, -prices[t]);
        }

        return allPositionClosed[n-1];
    }

