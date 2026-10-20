def total(prices, discount_percent=0):
    """Sum prices and apply a percentage discount."""
    subtotal = sum(prices)
    return subtotal * (1 - discount_percent / 100)
