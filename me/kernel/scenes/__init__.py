class Scenes:
    """31game の画面まとめ"""

    @staticmethod
    def print_title():
        """タイトル画面"""
        print("""
＼ ──┐　┐　    ─┐   ┌─┐ ／
／ ──┤　│　┌─┐┌─┤├┬┐├─┘ ＼
＼ ──┘　┴　└─┤└─┴│││└─┘ ／
／          ─┘       .. ＼
＼ ..................   ／
／      ...........     ＼
""")

    @staticmethod
    def stringify_how_many_stones_there_in_there_heap():
        """山にはいくつ石がありますか？"""
        return """
     ┌─┐
┌─┐┌─┼┬┴┐　？
└─┘└─┘└─┘
How many stones are there in the heap? (0 - 99)
Example: n=31
n="""

    @staticmethod
    def print_you_win_stone_none():
        """あなたの勝ち。石が残ってないとき"""
        print("""
 ^v^v^v^v^v^v^v^
<               >
 >  PERFECT !  <
<               >
 >  You win !  <
<               >
 v^v^v^v^v^v^v^v
""")

    @staticmethod
    def print_you_win_stone_remaining():
        """あなたの勝ち。相手が残っている石を取れないとき"""
        print("""
 ^v^v^v^v^v^v^v^
<               >
 >  You win !  <
<               >
 v^v^v^v^v^v^v^v
""")

    @staticmethod
    def print_you_lose_stone_none():
        """あなたの負け。石が残ってないとき"""
        print("""
  │
  └┐
   ・
Please choose: None!
There are no stones left!

 ~~~~~~~~~~
| You lose |
 ~~~~~~~~~~
""")

    @staticmethod
    def print_you_lose_stone_remaining():
        """あなたの負け。あなたが残っている石を取れないとき"""
        print("""
  │
  └┐
   ・
Please choose: None!
You can't take the remaining stones!

 ~~~~~~~~~~
| You lose |
 ~~~~~~~~~~
""")
