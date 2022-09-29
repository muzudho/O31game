def mex(S: set) -> int:
    """mexする

    Original: jelly
    Commentary or Arrangement: Muzudho

    Parameters
    ----------
    S : set
        サブトラクションセット
    """

    N = {s for s in range(len(S)+1)}
    """例えば S={1,3,5} なら、 N={0,1,2,3}
    s は N集合 の要素
    """

    m = min(N.difference(set(S)))
    """２つのリストのうち、片方にしかない要素で集合を作り、その中で最小の数"""

    return m
