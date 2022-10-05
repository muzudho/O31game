"""
cd me

python.exe -m ideas.gear_with_moving_hole.main
"""
import random


def main():
    print("Gear with moving hole")

    a = random.randint(0, 10)
    b = random.randint(a+0, a+10)
    c = random.randint(b+0, b+10)
    print(f"S={{a,b,c}} : S={{{a}, {b}, {c}}}")

    go_gear("a + b + c", a, b, c)  # a.b.c
    go_gear("a + b - c", a, b, c)
    go_gear("a - b + c", a, b, c)
    go_gear("a - b - c", a, b, c)

    go_gear("a + c + b", a, c, b)  # a.c.b
    go_gear("a + c - b", a, c, b)
    go_gear("a - c + b", a, c, b)
    go_gear("a - c - b", a, c, b)

    go_gear("b + a + c", b, a, c)  # b.a.c
    go_gear("b + a - c", b, a, c)
    go_gear("b - a + c", b, a, c)
    go_gear("b - a - c", b, a, c)

    go_gear("b + c + a", b, c, a)  # b.c.a
    go_gear("b + c - a", b, c, a)
    go_gear("b - c + a", b, c, a)
    go_gear("b - c - a", b, c, a)

    go_gear("c + a + b", c, a, b)  # c.a.b
    go_gear("c + a - b", c, a, b)
    go_gear("c - a + b", c, a, b)
    go_gear("c - a - b", c, a, b)

    go_gear("c + b + a", c, b, a)  # c.b.a
    go_gear("c + b - a", c, b, a)
    go_gear("c - b + a", c, b, a)
    go_gear("c - b - a", c, b, a)


def go_gear(expression, a, b, c):
    """n1 op1 n2 op2 op3"""
    tokens = expression.split(" ")
    n1 = choise_operand(tokens[0], a, b, c)
    n2 = choise_operand(tokens[2], a, b, c)
    n3 = choise_operand(tokens[4], a, b, c)
    print(f"""
n {tokens[0]:2} mod 3 {tokens[1]} {tokens[2]:2} mod 5 {tokens[3]} {tokens[4]:2} mod 7
  --------   --------   --------   -----""")
    m1 = 3
    m2 = 5
    m3 = 7

    l1 = n1 % m1
    l2 = n2 % m2
    l3 = n3 % m3
    value = do_operator(l1, tokens[1], l2)
    value = do_operator(value, tokens[3], l3)
    print(
        f"n {l1:8} {tokens[1]} {l2:8} {tokens[3]} {l3:8} = {value:5}\n")


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
