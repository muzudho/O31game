def main():
    print("")
    # 取っていい石の数（複数）
    numerics = input("""Rule how many can be taken?
Example: 1,2,3
> """).split(",")
    numbers = [int(numeric) for numeric in numerics]
    print(f"{numbers}")

    total = 31

    print(create_position_text(total))

    # Your turn.
    while True:
        try:
            choose = " ".join(numerics)
            n = input(f"""How many do you take?
Please choose: {choose}
> """)

            n = int(n)
            if n in numbers:
                # ループから抜ける
                break

        except Exception as e:
            print("Please try again!")
            # print(e)

    total -= n

    pos_txt = create_position_text(total)
    print(pos_txt)

    # Opponent turn.

    print("finishied")


def create_position_text(total):
    s = ""

    for _ in range(0, total):
        s += "o"

    s += """
-------------------------------
         1111111111222222222233
1234567890123456789012345678901
"""

    return s


if __name__ == "__main__":
    main()
