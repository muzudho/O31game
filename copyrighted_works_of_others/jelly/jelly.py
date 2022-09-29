# Author: jelly
# Commentary and Arrangement: Muzudho

def mex(S: set) -> int:
    SS = {k for k in range(len(S)+1)}
    m = min(SS.difference(set(S)))
    return m


def Period_Tail(S: set) -> list:
    # 周期とtail lengthを返す
    # n-max(S)からn-1までのグランディ数の組Rsが決まればそれ以降が決まる
    # 同じRsが以前既に現れていればそれ以降のGrundy数は同じ、つまり周期的になる
    # 以前のRsのindexをIとしてI-1までをTail, n-Iをperiodとしてアウトプット
    G = [0]
    RefG = [()]
    n = 1
    L = len(set(S))
    while n <= (L+1)**(max(S))+1:
        R = []
        for s in S:
            if n >= s:
                R.append(G[n-s])
        R = tuple(R)
        G.append(mex(R))
        Rs = tuple(G[max(0, n-max(S)):n])
        if n >= max(S) and Rs in RefG:
            # Rsの長さが短い間はまだ周期に入っていなくても同じRsが出てきうる
            I = RefG.index(Rs)
            p = n - I
            break
        else:
            RefG.append(Rs)
        n += 1
    while n-p >= 0 and G[n] == G[n-p]:
        n -= 1
    prep = n-p+1
    return p, prep, G[prep:n+1], G[:prep]
