from kernel.math.grundy import GrundyListObj


class Scenes:
    """31game の画面まとめ"""

    @staticmethod
    def stringify_title():
        """タイトル画面"""
        return """
＼ ──┐　┐　    ─┐   ┌─┐ ／
／ ──┤　│　┌─┐┌─┤├┬┐├─┘ ＼
＼ ──┘　┴　└─┤└─┴│││└─┘ ／
／          ─┘       .. ＼
＼ ..................   ／
／      ...........     ＼
"""

    @staticmethod
    def stringify_how_many_stones_there_in_there_heap():
        """山にはいくつ石がありますか？"""
        return """
     ┌─┐
┌─┐┌─┼┬┴┐　？
└─┘└─┘└─┘
How many stones are there in the heap? (0 - 99)
Example: len(N)=31
len(N)="""

    @staticmethod
    def stringify_you_win_stone_none():
        """あなたの勝ち。石が残ってないとき"""
        return """
 ^v^v^v^v^v^v^v^
<               >
 >  PERFECT !  <
<               >
 >  You win !  <
<               >
 v^v^v^v^v^v^v^v
"""

    @staticmethod
    def stringify_how_many_do_you_want_to_take_at_one_time():
        """一度にいくつ取りたいですか？"""
        return """
 ┌─┐    ┌─┐┌─┐    ┌─┬─┐┌─┐
 └─┘    └─┘└─┘    └─┴─┘└─┘   ？
└───┘  └──────┘  └────────┘
How many do you want to take at one time?
Example: S=1,2,3
S="""

    @staticmethod
    def stringify_how_many_do_you_take(choose):
        """いくつ取りますか？"""

        # "exit" もあるけど説明が長くなるので省略
        return f"""
 ┌──┐
   ┌┘
   ・
How many do you take?
Please choose: {choose} or "undo", "quit"
> """

    @staticmethod
    def stringify_computer_took_some_stones(number_taken):
        return f"""
  ┌─────┐
  │ ^ ^ │
  │  q  │
  └─┐ ┌─┘
┌───┘ └───┐
│         │ The computer took {number_taken} stone(s)."""

    @staticmethod
    def stringify_you_win_stone_remaining():
        """あなたの勝ち。相手が残っている石を取れないとき"""
        return """
 ^v^v^v^v^v^v^v^
<               >
 >  You win !  <
<               >
 v^v^v^v^v^v^v^v
"""

    @staticmethod
    def stringify_you_lose_stone_none():
        """あなたの負け。石が残ってないとき"""
        return """
  │
  └┐
   ・
Please choose: None!
There are no stones left!

 ~~~~~~~~~~
| You lose |
 ~~~~~~~~~~
"""

    @staticmethod
    def stringify_you_lose_stone_remaining():
        """あなたの負け。あなたが残っている石を取れないとき"""
        return """
  │
  └┐
   ・
Please choose: None!
You can't take the remaining stones!

 ~~~~~~~~~~
| You lose |
 ~~~~~~~~~~
"""

    @staticmethod
    def stringify_position_text(rest, number_taken, grundy_list_obj: GrundyListObj):
        """局面の文字列

        Example
        -------
                                      v 31
                                    ooo
        oooooooooooooooooooooooooooo
        -------------------------------
                 1111111111222222222 len(N)=28
        1234567890123456789012345678
        """

        s = "\n"

        # 持ち上げた石の描画
        if 0 < number_taken:
            # 持ち上げた石の右端が何番目だったのか知りたい
            for _ in range(0, rest + number_taken - 1):
                s += " "

            s += f"v {rest + number_taken}\n"

            # 取った石
            for _ in range(0, rest):
                s += " "

            for _ in range(0, number_taken):
                s += "o"  # 取った石

            s += "\n"

        # 残っている石を描画
        for _ in range(0, rest):
            s += "o"  # 残ってる石

        s += "\n"

        # 机の広さを描画
        desk_len = rest + number_taken

        for _ in range(0, desk_len):
            s += "-"  # 机

        s += "\n"

        # 石の数の十の位を描画（上限を９９とします）
        for nth in range(1, rest+1):  # 序数に変換
            if nth < 10:
                s += " "
            else:
                s += f"{nth//10}"

        s += f" len(N)={rest}\n"

        # 石の数の一の位を描画
        for nth in range(1, rest+1):  # 序数に変換
            s += f"{nth%10}"

        s += "\n\n"

        # グランディ数の十の位を描画（上限を９９とします）
        for nth in range(1, rest+1):  # 序数に変換
            grundy = grundy_list_obj.get_grundy_at(nth)
            if grundy < 10:
                s += " "
            else:
                s += f"{grundy//10}"

        s += "\n"

        # グランディ数の一の位を描画
        for nth in range(1, rest+1):  # 序数に変換
            grundy = grundy_list_obj.get_grundy_at(nth)
            s += f"{grundy%10}"

        s += " grundy\n"

        return s
