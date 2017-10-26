def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    k = 2 
    profits = [0 for _ in range(k+1)] 
    maximize = [-prices[0] for _ in range(k+1)]
    for price in prices:
        for i in range(1, len(profits)):
            profits[i] = max(profits[i], maximize[i] + price)
            maximize[i] = max(maximize[i], profits[i-1] - price)
    return profits[-1]