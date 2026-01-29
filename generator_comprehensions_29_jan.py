#Generator -> (expression for item in iterable if condition)

daily_sales= [1500, 2300, 1800, 2000, 1700, 2500, 3000]
total_sales= sum(sale for sale in daily_sales if sale > 2000)
print("Total sale   s for days with sales over 2000:", total_sales)