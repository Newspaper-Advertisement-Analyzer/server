import re

def identify_price(text):
    # Regular expression patterns for price detection
    price_patterns = [
        r"(?:(?:Rs\.?|LKR)?\s*([0-9,.]+)\s*million|mn)",  # e.g., 18.5mn, 2 Million per Perch
        r"(?:(?:Rs\.?|LKR)?\s*([0-9,.]+)\s*lakh)",  # e.g., 1 lakh
        r"(?:Price\s*:\s*(?:Rs\.?|LKR)?\s*([0-9,.]+))"  # e.g., Price : Rs.3,700,000
    ]

    prices = []

    # Iterate through each price pattern and find matches in the text
    for pattern in price_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            if match:  # Check if match is not an empty string
                # Handle commas and convert to float
                price_value = float(match.replace(',', ''))
                
                # Check context for 'million' or 'lakh' and adjust the price accordingly
                if 'million' in pattern.lower() or 'mn' in pattern.lower():
                    price_value *= 1000000  # Convert million to base currency
                elif 'lakh' in pattern.lower():
                    price_value *= 100000  # Convert lakh to base currency

                prices.append(("LKR", price_value))

    if len(prices) == 0:
        return "No price found"
    
    # Sort prices by value in descending order (highest first)
    prices.sort(key=lambda x: x[1], reverse=True)
    
    return prices[0]
