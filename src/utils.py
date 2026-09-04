# Build: 3d80a8196f9ce586e4872f7ac3aa2079

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
