def maxProfit(s):
    min = s[0]
    profit = 0
    for i, price in enumerate(s):
        if price < min:
            min = price
        elif price - min > profit:
            profit = price - min 
        
    
    return profit

