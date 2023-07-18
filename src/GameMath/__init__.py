def Lerp(a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b

def LerpTuple(a: tuple[float, float], b: tuple[float, float], t: float) -> tuple[float, float]:
    return Lerp(a[0], b[0], t), Lerp(a[1], b[1], t)