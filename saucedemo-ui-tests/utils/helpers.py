def to_slug(text):
    """'Sauce Labs Backpack' -> 'sauce-labs-backpack' (used in SauceDemo element ids)."""
    return text.lower().replace(" ", "-")
