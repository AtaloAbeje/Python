def get_max_profit(prices):
    prices_index = []

    for i in range(len(prices)):
        prices_index.append((prices[i], i))

    prices_index.sort()
   # print(prices_index)

    len_prices = len(prices)
    max_profit = 0

    for buy_index in range(0,len_prices):
        buy, buy_pos = prices_index[buy_index]

        for sell_index in range(len_prices-1,buy_index,-1):
            sell,sell_pos = prices_index[sell_index]
            print("buy_index",buy_index,"sell_index",sell_index)
            print("buy",buy,"sell",sell)
            if buy_pos < sell_pos:
                profit = sell-buy
                print("profit",profit)
                if profit > max_profit:
                    max_profit = profit
                break           
        return max_profit


prices = [7,1,5,3,6,4]
print(get_max_profit(prices))

