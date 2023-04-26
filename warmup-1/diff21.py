def diff21(n):
    """Return the absolute difference between n and 21, or double the absolute difference if n is over 21."""
    if n > 21:
        return 2 * abs(n - 21)
    else:
        return abs(n - 21)
