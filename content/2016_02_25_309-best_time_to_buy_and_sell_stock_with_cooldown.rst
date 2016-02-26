309-best_time_to_buy_and_sell_stock
###################################

:date: 2016-2-25 9:53
:tags: Best Time To Buy/Sell
:category: LeetCode
:slug: 309-best_time_to_buy_and_sell_stock_with_cooldown

`LeetCode Problem Link <https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/>`_

We can make as many trades as needed, but each buy cannot be immediately after a sell.

int array ``buy`` is the profit with one outstanding stock.
int array ``sell`` is the profit with no oustanding stock.

``buy[i]`` is the amount of cash with one outstanding stock position, it is purchased either at day ``i``
 or any day before day ``i``.

``sell[i]`` is the amount of chash with no oustanding stock position, the last sold occurred on day ``i`` or
 any day before day ``i``.

::

    buy[i] = Math.max(buy[i-1], sell[i-2] - prices[i])
    sell[i] = Math.max(sell[i-1], buy[i-1] + prices[i])

    return sell[n-1]
    it wouldn't make sense to return a value from ``buy`` because why would we want a outstanding stock position?

.. code-block:: java

    public int maxProfit(int[] prices) {
        int n = prices.length;

        if (n<=1)
            return 0;

        int[] buy = new int[n];
        int[] sell = new int[n];

        // buy[i] = Math.max(buy[i-1], sell[i-2] - prices[i])
        // sell[i] = Math.max(sell[i-1], buy[i-1] + prices[i])


        buy[0] = -prices[0];
        sell[0] = 0;

        sell[1] = Math.max(sell[0], buy[0] + prices[1]);
        buy[1] = Math.max(buy[0], 0 - prices[1]);

        for (int i=2; i<n; i++) {
            buy[i] = Math.max(buy[i-1], sell[i-2] - prices[i]);
            sell[i] = Math.max(sell[i-1], buy[i-1] + prices[i]);
        }

        //System.out.println(Arrays.toString(buy));
        //System.out.println(Arrays.toString(sell));

        return sell[n-1];
    }

In 188-best_time_to_buy_and_sell_stock_iv, we used a very similar approach.

