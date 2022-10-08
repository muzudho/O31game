"""
cd me

python.exe -m ideas.clouds_passer_calc.main
"""


def main():
    n = 1
    a1, a2, b1, b2 = clouds_passer_calc(3, 5, n)
    print(f"n:{n} a:({a1},{a2}) b:{b1,b2}")
    pass


def clouds_passer_calc(a, b, n):
    a_begin = (a+b)*n+a
    a_end = (a+b)*n+2*a-1
    b_begin = (a+b)*n+b
    b_end = (a+b)*(n+1)-1
    return a_begin, a_end, b_begin, b_end


if __name__ == "__main__":
    main()
