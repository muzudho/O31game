# Author: Muzudho

from kernel import Kernel
from kernel.scenes import Scenes
from kernel.think import Think


def main():
    # このゲームの基本部品
    kernel = Kernel()

    # Title
    print(Scenes.stringify_title())

    # Stage edit: 山にいくつ石がありますか？
    while True:
        # [Ctrl]+[C]キーで抜けたいので、input を try 句の外に出します
        enter = input(
            Scenes.stringify_how_many_stones_there_in_there_heap())

        try:
            if enter == "exit" or enter == "quit":
                print("Bye.")
                exit(0)

            kernel.rest = int(enter)
            break

        except:
            print("Please try again!")

    # Stage edit: 取っていい石の数（複数）
    while True:
        # [Ctrl]+[C]キーで抜けたいので、input を try 句の外に出します
        enter = input(
            Scenes.stringify_how_many_do_you_want_to_take_at_one_time())

        try:
            if enter == "exit" or enter == "quit":
                print("Bye.")
                exit(0)

            numerics = enter.split(",")
            kernel.numbers_to_choose = [int(numeric) for numeric in numerics]
            # 昇順ソート
            kernel.numbers_to_choose.sort()
            print(Scenes.stringify_position_text(kernel.rest, 0))
            break

        except:
            print("Please try again!")

    # Play
    while True:

        # 残りの石の数以上の選択肢は削除します
        Kernel.remove_out_of_range_choices(
            kernel.rest, kernel.numbers_to_choose)

        # Your turn.

        if len(kernel.numbers_to_choose) < 1:
            # まだ石が残っているのに、選択肢がない
            print(Scenes.stringify_you_lose_stone_remaining())
            break

        while True:
            # 入力を並び替える
            numerics = [str(number) for number in kernel.numbers_to_choose]
            choose = " ".join(numerics)

            # [Ctrl]+[C]キーで抜けたいので、input を try 句の外に出します
            # Play: 幾つ石を取りますか？
            enter = input(Scenes.stringify_how_many_do_you_take(choose))

            try:
                if enter == "exit" or enter == "quit":
                    print("Bye.")
                    exit(0)

                if enter == "undo":
                    if 2 <= len(kernel.record):
                        # TODO １つ前のコンピューターが取った石と、２つ前の自分が取った石を戻せばアンドゥと同じ
                        number_taken = kernel.record.pop(-1)
                        kernel.rest += number_taken
                        number_taken = kernel.record.pop(-1)
                        kernel.rest += number_taken
                        print(Scenes.stringify_position_text(
                            kernel.rest, number_taken))
                    else:
                        print("No more undo!")

                    # なんにせよループ戻る
                    continue

                number_taken = int(enter)

                # 選択肢の中からちゃんと選んだら
                if number_taken in kernel.numbers_to_choose:
                    # ループから抜ける
                    break

                print("Please try again!")

            except:
                print("Please try again!")

        kernel.record.append(number_taken)
        kernel.rest -= number_taken
        print(Scenes.stringify_position_text(kernel.rest, number_taken))

        if kernel.rest < 1:
            # 最後の石を取った
            print(Scenes.stringify_you_win_stone_none())
            break

        # 残りの石の数以上の選択肢は削除します
        Kernel.remove_out_of_range_choices(
            kernel.rest, kernel.numbers_to_choose)

        # Opponent turn.

        if len(kernel.numbers_to_choose) < 1:
            # まだ石が残っているのに、選択肢がないなら、コンピューターの負け
            print(Scenes.stringify_you_win_stone_remaining())
            break

        number_taken = Think.get_bestmove(
            kernel.rest, kernel.numbers_to_choose)

        print(Scenes.stringify_computer_took_some_stones(number_taken))

        kernel.record.append(number_taken)
        kernel.rest -= number_taken
        print(Scenes.stringify_position_text(kernel.rest, number_taken))

        if kernel.rest < 1:
            # 最後の石を取られた
            print(Scenes.stringify_you_lose_stone_none())
            break

    # finished.


if __name__ == "__main__":
    main()
