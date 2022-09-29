# Author: jelly
# Commentary and Arrangement: Muzudho

def mex(S: set) -> int:
    """mexする"""
    SS = {k for k in range(len(S)+1)}
    m = min(SS.difference(set(S)))
    return m


def AddGrundy(S: set, previousG, k):
    """グランディ数の集合 G に要素を１つ加える

    - あらかじめ計算されているGにさらにk項付け加える

    Parameters
    ----------
    S : set
        サブトラクションセット
    previousG : _type_
        _description_
    k : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """

    G = previousG
    kk = k - len(previousG)
    for n in range(kk):
        L = len(G)
        """グランディ数の集合 G の要素数 L"""

        R = {G[L - s] for s in S if L - s >= 0}
        """遷移先の グランディ数の集合 R

        s - int
            サブトラクションセットの要素
        """

        G.append(mex(R))
        """非負整数から R を除外した残りのうち最小の数"""

    return G


# 計算している範囲に周期があるか判定．あれば[period, tail length, cycle, tail]を吐き出す
def find_period(S, G, k):
    m = k//2
    s0 = max(S)
    for n in range(m+1, k-s0):
        if G[m: m+s0] == G[n: n+s0]:
            p = n - m
            cycle = G[m: n]
            mm = m - p
            nn = n - p
            while G[mm: mm+s0] == G[nn: nn+s0] and mm >= 0:
                m = mm
                n = nn
                mm -= p
                nn -= p
            mm = m - 1
            nn = n - 1
            while G[mm: mm+s0] == G[nn: nn+s0] and mm >= 0:
                m = mm
                n = nn
                mm -= 1
                nn -= 1
            prep = m
            tail = G[:prep]
            return p, prep, cycle, tail
    return False


def Period_Tail2(S: set) -> list:
    """周期が見つかるまで計算範囲を2倍して何度も繰り返し、[period, tail length, cycle, tail]をアウトプット

    Parameters
    ----------
    S : set
        サブトラクションセット
    """
    # グランディ数の集合 G
    G = [0]
    k = 2**8
    F = False
    while F == False:
        G = AddGrundy(S, G, k)
        F = find_period(S, G, k)
        k *= 2
    return F


# フィボナッチ数列を作っている
#
# Author: jelly
# Arrangement: Muzudho
Fib = [1, 2]  # basecase
for n in range(100):
    Fib.append(Fib[-1]+Fib[-2])  # 新しい項
    # 作るたび表示
    print(Fib[-1], Period_Tail2(set(Fib))[:2])
