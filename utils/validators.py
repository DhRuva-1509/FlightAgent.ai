def normalize_city(city):
    return city.lower().strip() if city else None


def validate_price(price):
    try:
        price = int(price)
        return price if price > 0 else None
    except:
        return None
