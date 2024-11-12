""" My stock pricing project

Used to check what's the best profit in your array
"""


def max_profit(prices):
    """
    :param prices: A list of integers or float as prices
    :return: the best deal of your array to get the best profit
    """
    buying_day = prices[0]
    selling_day = 0
    for i in prices[1:]:  # it will slice list and start comparing on values without returning back
        if buying_day > i:  # checking the lowest value to buy
            buying_day = i
        elif selling_day < i:  # checking the highest value to sell
            selling_day = i
    print("best price to buy : " + str(buying_day))
    print("best day to sell : " + str(selling_day))
    profit = selling_day - buying_day  # checking the value we got
    return profit

Prices = [100,50,7,6,22,9,88]
print(Prices)
print("Your Max Profit Is : "+str(max_profit(Prices)))
