"""
cd me

python.exe -m ideas.clouds_passer_calc.main
"""


def main():
    a = 3
    b = 5
    for n in range(0, 3):
        a1, a2, b1, b2 = clouds_passer_calc(a, b, n)
        print(f"S={{ {a}, {b} }} n:{n} a_b=[{a1}:{b2}]")

    a = 4
    b = 6
    for n in range(0, 3):
        a1, a2, b1, b2 = clouds_passer_calc(a, b, n)
        print(f"S={{ {a}, {b} }} n:{n} a_b=[{a1}:{b2}]")


def clouds_passer_calc(a, b, n):
    a_begin = (a+b)*n+a
    a_end = (a+b)*n+2*a-1
    b_begin = (a+b)*n+b
    b_end = (a+b)*(n+1)-1
    return a_begin, a_end, b_begin, b_end


if __name__ == "__main__":
    main()
