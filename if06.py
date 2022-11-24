def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1=n%10
    n=n//10
    x2=n%10
    n=n//10
    x3=n%10
    n=n//10
    x4=n%10
    x5=n//10
    v=0
    n=5
    if v<x1:
        v=x1
    if v<x2:
        v=x2
        n=n-1
    if v<x3:
        v=x3
        n=n-1
    if v<x4:
        v=x4
        n=n-1
    if v<x5:
        v=x5
        n=n-1
    return n
print(main(56371))