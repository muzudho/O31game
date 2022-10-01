"""
cd me

python.exe -m docs.idea_sketch.s_4_5_40.make_c_from_a_b

Explanation
===========
S = { a, b, c }
の、いい感じの a, b, c を選んでくれるアルゴリズム。
"""


def get_3_periods_given_a_b_c(a, b, c):
    """S = { a, b, c } を渡すと、周期の候補を３つ返します。
    やりたいことは次の通り

        c = ax
        c = by
        x = bz
        y = az
        z = まだ分かっていないが、 1 は例外な動きをするので、 2 以上の整数にしたらいいんじゃないかな

    上式を満たす c を返せばよい。
    z は分かってないんで、いくつでも候補を挙げればいいだろう

    よくみたら　この式、 c = abz なんじゃないのか。 x も y も要らないや
    """

    # 全ての組み合わせについて、足すだけじゃないか（＾～＾）
    return a + b, b + c, c + a


def choose_period_with_guess(a_p_b, b_p_c, c_p_a):
    """推測で周期を選ぶ。
    周期の候補を３つ受け取るが、どれが本物なのか、分かんないんで、とりあえず　当てずっぽうで決めてみる。
    しかし、取り方が３種類あるので、結局３つ返す"""
    ab = a * b
    loop_length = 3 * a * b
    c_mod_loop_length = c % loop_length
    feeling = c_mod_loop_length // ab
    # print(
    #    f"loop_length:{loop_length} c:{c} c_mod_loop_length:{c_mod_loop_length} feeling:{feeling}")

    # TODO 外れるときは外れるし、当たるときは当たる。そこをどうにかしなきゃ（＾～＾）
    if a * b == c:
        # z が 1 のとき。よく分かってない。例外的な動きをする。まだ適当な if文
        maybe_numbers = [c_p_a, a_p_b, b_p_c]
    else:
        # よく分かってない。まだ適当な 場合分け
        if feeling == 1:
            maybe_numbers = [a_p_b, b_p_c, c_p_a]
        elif feeling == 2:
            maybe_numbers = [b_p_c, c_p_a, a_p_b]
        elif feeling == 0:
            maybe_numbers = [c_p_a, a_p_b, b_p_c]
        else:
            raise ValueError(f"unexpected feeling:{feeling}")

    return maybe_numbers[0], maybe_numbers[1], maybe_numbers[2]


if __name__ == "__main__":
    """a と b を選べば、 いい感じの c を勝手に選んでくれる"""

    enter = input("""S = { a, b, c }
Please enter a and b. This program chooses a nice looking c.
Example: S=4 5
Example: S=3 8
S=""")
    tokens = enter.split(" ")
    a = int(tokens[0])
    b = int(tokens[1])

    for z in range(1, 10):
        """z は、 ab の定数倍を意味している。いくつも候補を出す"""
        c = a * b * z

        a_p_b, b_p_c, c_p_a = get_3_periods_given_a_b_c(a, b, c)
        """S = { a, b, c } を渡すと、周期の候補を３つ返す"""

        period1, period2, period3 = choose_period_with_guess(
            a_p_b, b_p_c, c_p_a)
        """周期の候補が３つ返ってくるが、どれが本物なのか、分かんないんで、とりあえず　当てずっぽうで決めてみる。
        しかし、取り方が３種類あるので、結局３つ返す"""

        print(
            f"Example: S={{{a}, {b}, {c}}} The period the program predicts:  {a_p_b}  or  {b_p_c}  or  {c_p_a}.    May come off but maybe: (A) {period1}   (B) {period2}   (C) {period3}.")
