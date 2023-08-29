import re


def identify_price(text):
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

    if len(prices) == 0:
        return "No price found"
    return prices[0]


# ==================Test==================

# price = identify_price('''District - Colombo
# City - Bokundara
# Price : Rs.33,000,000''')

# print(price)