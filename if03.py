def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if b>a:
        if b<c:
            return b
        else:
            return a
    else:
        if a<c:
            return a
        else:
            return c
print(main(-1,0,-3))
