def buySellStock(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])
    return max_profit


# to track buying and selling days.


def BuySellStock(prices):
    if not prices:
        return 0, None, None

    min_price = prices[0]
    buy_price = prices[0]
    sell_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        # check profit first
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            buy_price = min_price
            sell_price = prices[i]

        # update min price
        if prices[i] < min_price:
            min_price = prices[i]

    return max_profit, buy_price, sell_price


if __name__ == "__main__":
    prices = list(map(int, input().split()))
    res = buySellStock(prices)
    print("maximum profit is:", res)
