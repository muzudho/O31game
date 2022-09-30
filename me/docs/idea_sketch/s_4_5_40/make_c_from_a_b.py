"""
cd me/docs/idea_sketch/s_4_5_40

python.exe make_c_from_a_b.py

Explanation
===========
S = { a, b, c }
の、いい感じの a, b, c を選んでくれるアルゴリズム。

a と b を選べば、 いい感じの c を勝手に選んでくれる
"""

enter = input("""S = { a, b, c }
Please enter a and b. This program chooses a nice looking c.
Example: S=4 5
S=""")
tokens = enter.split(" ")
a = int(tokens[0])
b = int(tokens[1])

"""
やりたいことは次の通り

    c = ax
    c = by
    x = bz
    y = az
    z = まだ分かっていないが、2 以上の整数にしたらいいんじゃないか

上式を満たす c を返せばよい。
z は分かってないんで、いくつでも候補を挙げればいいだろう
"""

for z in range(2, 10):
    c = a * b * z
    a_p_b = a + b
    b_p_c = b + c
    a_p_c = a + c
    print(
        f"Example: S={{{a}, {b}, {c}}} The period the program predicts: {a_p_b} or {b_p_c} or {a_p_c}")
