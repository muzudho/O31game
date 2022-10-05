"""
cd me

python.exe -m ideas.gear_with_moving_hole.main
"""
import random


def main():
    print("Gear with moving hole")

    a = 5
    b = 7
    c = 13
    len_Nz = 40
    print(f"S={{a,b,c}} : S={{{a}, {b}, {c}}}")

    # n mod a + n mod b + n mod c の略
    go_gear("a + b + c", a, b, c, len_Nz)  # a.b.c
    go_gear("a + b - c", a, b, c, len_Nz)
    go_gear("a - b + c", a, b, c, len_Nz)
    go_gear("a - b - c", a, b, c, len_Nz)
    go_gear("a + c + b", a, c, b, len_Nz)  # a.c.b
    go_gear("a + c - b", a, c, b, len_Nz)
    go_gear("a - c + b", a, c, b, len_Nz)
    go_gear("a - c - b", a, c, b, len_Nz)
    go_gear("b + a + c", b, a, c, len_Nz)  # b.a.c
    go_gear("b + a - c", b, a, c, len_Nz)
    go_gear("b - a + c", b, a, c, len_Nz)
    go_gear("b - a - c", b, a, c, len_Nz)
    go_gear("b + c + a", b, c, a, len_Nz)  # b.c.a
    go_gear("b + c - a", b, c, a, len_Nz)
    go_gear("b - c + a", b, c, a, len_Nz)
    go_gear("b - c - a", b, c, a, len_Nz)
    go_gear("c + a + b", c, a, b, len_Nz)  # c.a.b
    go_gear("c + a - b", c, a, b, len_Nz)
    go_gear("c - a + b", c, a, b, len_Nz)
    go_gear("c - a - b", c, a, b, len_Nz)
    go_gear("c + b + a", c, b, a, len_Nz)  # c.b.a
    go_gear("c + b - a", c, b, a, len_Nz)
    go_gear("c - b + a", c, b, a, len_Nz)
    go_gear("c - b - a", c, b, a, len_Nz)


def go_gear(expression, a, b, c, len_Nz):
    """n1 op1 n2 op2 op3"""
    tokens = expression.split(" ")
    m1 = choise_operand(tokens[0], a, b, c)
    m2 = choise_operand(tokens[2], a, b, c)
    m3 = choise_operand(tokens[4], a, b, c)
    print(f"""
n n mod {m1:>2} {tokens[1]} n mod {m2:>2} {tokens[3]} n mod {m3:>2}   Grundy
  --------   --------   --------   ------""")

    for n in range(0, len_Nz):
        l1 = n % m1
        l2 = n % m2
        l3 = n % m3
        value = do_operator(l1, tokens[1], l2)
        value = do_operator(value, tokens[3], l3)
        value = value % 4  # 0～3 にしたい
        print(
            f"n {l1:8} {tokens[1]} {l2:8} {tokens[3]} {l3:8} = {value:6}")


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
