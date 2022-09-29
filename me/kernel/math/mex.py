def mex(S: set) -> int:
    """mexする

    Original author: jelly
    Commentary and Arrangement: Muzudho

    Parameters
    ----------
    S : set
        サブトラクションセット
    """

    grundy_set = {t for t in range(len(S)+1)}
    """例えば S={1,3,5} なら、 grundy_set={0,1,2,3}
    t は grundy 集合 の要素
    """

    m = min(grundy_set.difference(S))
    """２つのリストのうち、片方にしかない要素で集合を作り、その中で最小の数"""

    return m
