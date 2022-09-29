def make_fib(end_num=100, set_new_item=lambda x: 0):
    """フィボナッチ数列を作る
    Original author: jelly
    Arrangement: Muzudho
    """

    fib = [1, 2]  # basecase

    for _ in range(end_num):
        # 新しい項
        succ = fib[-1]+fib[-2]

        # 新しい項を作ったとき
        set_new_item(succ)

        fib.append(succ)

    return fib
