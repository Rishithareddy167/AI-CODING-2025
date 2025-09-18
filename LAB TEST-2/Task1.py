def apply_discount(price: float, category: str) -> float:
    """
    Applies a seasonal discount based on product category.

    Discount Table:
        seeds:      10%
        fertilizer: 15%
        tools:       5%

    Returns:
        float: Discounted price.

    Raises:
        ValueError: If category is invalid.

    Examples:
        >>> apply_discount(100, "fertilizer")
        85.0
        >>> apply_discount(200.0, "seeds")
        180.0
        >>> apply_discount(50, "tools")
        47.5
        >>> apply_discount(100, "unknown")
        Traceback (most recent call last):
        ...
        ValueError: Invalid category: unknown
    """
    discounts = {
        "seeds": 0.10,
        "fertilizer": 0.15,
        "tools": 0.05
    }
    if category not in discounts:
        raise ValueError(f"Invalid category: {category}")
    discount = discounts[category]
    return round(price - price * discount, 2)

if __name__ == "__main__":
    print(apply_discount(100, 'seeds'))        # 90.0
    print(apply_discount(200, 'fertilizer'))   # 170.0
    print(apply_discount(50, 'tools'))         # 47.5
    print(apply_discount(100, 'fertilizer'))   # 85.0
    print(apply_discount(100, 'tools'))        # 95.0
    print(apply_discount(99.99, 'fertilizer')) # 84.99
    assert apply_discount(100, "fertilizer") == 85.0
    assert apply_discount(200.0, "seeds") == 180.0
    assert apply_discount(50, "tools") == 47.5
    try:
        apply_discount(100, "unknown")
    except ValueError as e:
        print(e)