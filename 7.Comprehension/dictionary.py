tea_prices_inr = {
    "masala chai": 20,
    "ginger chai": 15,
    "lemon tea": 10,
    "green tea": 25,
    "black tea": 18,
    "ice tea": 12,
    "milk tea": 20,
}   

tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)