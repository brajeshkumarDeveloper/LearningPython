tea_prices_inr={
    "masala Chai": 30,
    "ginger tea": 25,
    "lemon tea": 20,
    "black tea": 15,
    "green tea": 35
}

tea_prices_usd={
    tea:price /80 for tea, price in tea_prices_inr.items()
}
print(tea_prices_usd)