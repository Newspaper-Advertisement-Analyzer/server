import re


def extract_price(text):
    # Regular expression patterns for price detection
    lkr_pattern = r"RS?\.?\s*(\d{1,3}(,\d{3})*(\.\d{1,2})?)"
    usd_pattern = r"\$\s*(\d+(\.\d{1,2})?)"

    lkr_prices = re.findall(lkr_pattern, text, re.IGNORECASE)
    usd_prices = re.findall(usd_pattern, text, re.IGNORECASE)

    prices = []

    # Append Sri Lankan Rupee prices to the list
    for lkr_price in lkr_prices:
        currency = "LKR"
        price_value = float(lkr_price[0].replace(",", ""))
        prices.append((currency, price_value))


    # Append US Dollar prices to the list
    for usd_price in usd_prices:
        price_value = float(usd_price[0])
        prices.append(("USD", price_value))

    print(text)
    print(prices)

    if len(prices) == 0:
        return None
    
    return prices[0] #_________________________________change this later



#________Test___________________________
# price = extract_price(" for Three Vehicles, Pantry, Wet Kitchen. 33 M 0773033852.")

# print(price)