def main():
    total = 31

    pos_txt = create_position_text(total)
    print(pos_txt)

    # Your turn.
    while True:
        try:
            n = int(input("how many do you take? "))
        except:
            continue

        break

    total -= n

    pos_txt = create_position_text(total)
    print(pos_txt)

    # Opponent turn.

    print("finishied")


def create_position_text(total):
    s = ""

    for _ in range(0, total):
        s += "o"

    return s


if __name__ == "__main__":
    main()
