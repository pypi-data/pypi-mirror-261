def add(a, b):
    if a < 0 or a > 100 or b < 0 or b > 100:
        raise ValueError("Arguments must be between 0 and 100")
    return a + b
