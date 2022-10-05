"""
cd me

python.exe -m ideas.gear_with_moving_hole.main
"""
import random

expected_grundy_seq = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
                       2, 2, 0, 2, 2, 3, 3, 1, 0, 3, 0, 0, 0, 1, 0, 1, 1, 1, 2, 1, 0, 2, 0, 3, 2, 1, 0, 1, 0, 3, ]
"""S={3,5,7}"""


def main():
    global expected_grundy_seq
    len_Nz = 40

    playout = 100
    for i in range(0, playout):

        a = random.randint(1, 100)
        b = random.randint(a+1, a+100)
        c = random.randint(b+1, b+100)

        # 係数。線形ではないだろうし
        aa = random.randint(0, 10)
        bb = random.randint(0, 10)
        cc = random.randint(0, 10)

        print("Gear with moving hole")
        print(f"S={{a,b,c}} : S={{{a}, {b}, {c}}}")

        # n aa mod a + n bb mod b + n cc mod c の略
        go_gear("a + b + c", a, b, c, aa, bb, cc, len_Nz)  # a.b.c
        go_gear("a + b - c", a, b, c, aa, bb, cc, len_Nz)
        go_gear("a - b + c", a, b, c, aa, bb, cc, len_Nz)
        go_gear("a - b - c", a, b, c, aa, bb, cc, len_Nz)
        go_gear("a + c + b", a, c, b, aa, cc, bb, len_Nz)  # a.c.b
        go_gear("a + c - b", a, c, b, aa, cc, bb, len_Nz)
        go_gear("a - c + b", a, c, b, aa, cc, bb, len_Nz)
        go_gear("a - c - b", a, c, b, aa, cc, bb, len_Nz)
        go_gear("b + a + c", b, a, c, bb, aa, cc, len_Nz)  # b.a.c
        go_gear("b + a - c", b, a, c, bb, aa, cc, len_Nz)
        go_gear("b - a + c", b, a, c, bb, aa, cc, len_Nz)
        go_gear("b - a - c", b, a, c, bb, aa, cc, len_Nz)
        go_gear("b + c + a", b, c, a, bb, cc, aa, len_Nz)  # b.c.a
        go_gear("b + c - a", b, c, a, bb, cc, aa, len_Nz)
        go_gear("b - c + a", b, c, a, bb, cc, aa, len_Nz)
        go_gear("b - c - a", b, c, a, bb, cc, aa, len_Nz)
        go_gear("c + a + b", c, a, b, cc, aa, bb, len_Nz)  # c.a.b
        go_gear("c + a - b", c, a, b, cc, aa, bb, len_Nz)
        go_gear("c - a + b", c, a, b, cc, aa, bb, len_Nz)
        go_gear("c - a - b", c, a, b, cc, aa, bb, len_Nz)
        go_gear("c + b + a", c, b, a, cc, bb, aa, len_Nz)  # c.b.a
        go_gear("c + b - a", c, b, a, cc, bb, aa, len_Nz)
        go_gear("c - b + a", c, b, a, cc, bb, aa, len_Nz)
        go_gear("c - b - a", c, b, a, cc, bb, aa, len_Nz)


def go_gear(expression, a, b, c, aa, bb, cc, len_Nz):
    """n1 op1 n2 op2 op3"""
    global expected_grundy_seq

    tokens = expression.split(" ")
    m1 = choise_operand(tokens[0], a, b, c)
    m2 = choise_operand(tokens[2], a, b, c)
    m3 = choise_operand(tokens[4], a, b, c)
    mm1 = choise_operand(tokens[0], aa, bb, cc)
    mm2 = choise_operand(tokens[2], aa, bb, cc)
    mm3 = choise_operand(tokens[4], aa, bb, cc)
    print(f"""
n {mm1:>2}n mod {m1:>2} {tokens[1]} {mm2:>2}n mod {m2:>2} {tokens[3]} {mm3:>2}n mod {m3:>2}   Grundy
  ----------   ----------   ----------   ------""")

    is_perfect = True

    i = 0
    for n in range(0, len_Nz):
        l1 = mm1 * n % m1
        l2 = mm2 * n % m2
        l3 = mm3 * n % m3
        value = do_operator(l1, tokens[1], l2)
        value = do_operator(value, tokens[3], l3)
        value = value % 4  # 0～3 にしたい
        print(
            f"n {l1:8} {tokens[1]} {l2:8} {tokens[3]} {l3:8} = {value:6}")

        if expected_grundy_seq[i] != value:
            is_perfect = False

        i += 1

    if is_perfect:
        raise ValueError("Oh, my God!")


def choise_operand(expected, a, b, c):
    if expected == "a":
        return a
    elif expected == "b":
        return b
    elif expected == "c":
        return c
    else:
        raise ValueError(f"unexpected:{expected}")


def do_operator(n1, operator, n2):
    if operator == "+":
        return n1+n2
    elif operator == "-":
        return n1-n2
    else:
        raise ValueError(f"unexpected operator:{operator}")


if __name__ == "__main__":
    main()
