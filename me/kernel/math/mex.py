def mex(S: set) -> int:
    """mexする
    Original: jelly
    Arrangement: Muzudho

    Parameters
    ----------
    S : set
    """
    SS = {k for k in range(len(S)+1)}
    m = min(SS.difference(set(S)))
    return m
