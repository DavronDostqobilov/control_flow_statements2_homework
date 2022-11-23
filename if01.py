def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    x=a
    if a>x:
        x=a
    elif b>x:
        x=b
    elif c>x:
        x=c

    return x
print(main(23,43,5))