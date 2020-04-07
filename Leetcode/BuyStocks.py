"""
1) Find the efficient way of buying a stock. In our case from left-to-right its 1
2) Buy on one day and sell it on the next day only for a profit
"""
def maxProfit(PriceList):
    best_without_stock = 0;
    best_with_stock = -(1e9 +5)
    for x in PriceList:
        
        best_with_stock = max(best_with_stock, best_without_stock - x)
        best_without_stock = max(best_without_stock, best_with_stock +x)
        print("Without stock", best_without_stock)
        print("With stock", best_with_stock)

    return best_without_stock

print(maxProfit([7, 1, 5, 3, 6, 4]))

