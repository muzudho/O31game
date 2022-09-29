from kernel.math.grundy import GrundyListObj


class Kernel:
    """31game の基本部品"""

    @staticmethod
    def remove_out_of_range_choices(rest, numbers_to_choose):
        """残りの石の数を超える数の選択肢は削除"""

        removed_items = []

        while 0 < len(numbers_to_choose) and rest < numbers_to_choose[len(numbers_to_choose)-1]:
            removed_item = numbers_to_choose.pop(-1)
            removed_items.append(removed_item)

        return removed_items

    def __init__(self):
        """初期化"""

        self.__rest = 0
        """残りの石の個数"""

        self.__numbers_to_choose = []
        """石をいくつ取るかの一覧"""

        self.__record = []
        """棋譜"""

        self.__grundy_list_obj = None
        """局面の石の数に対応付くグランディ数の一覧"""

    @property
    def rest(self):
        """残りの石の個数"""
        return self.__rest

    @rest.setter
    def rest(self, value):
        """残りの石の個数"""
        self.__rest = value

    @property
    def numbers_to_choose(self):
        """石をいくつ取るかの一覧"""
        return self.__numbers_to_choose

    @numbers_to_choose.setter
    def numbers_to_choose(self, value):
        """石をいくつ取るかの一覧"""
        self.__numbers_to_choose = value

    @property
    def record(self):
        """棋譜"""
        return self.__record

    @record.setter
    def record(self, value):
        """棋譜"""
        self.__record = value

    @property
    def grundy_list_obj(self):
        """グランディ数の一覧オブジェクト"""
        return self.__grundy_list_obj

    def append_record_item(self, item):
        self.__record.append(item)

    def pop_record_item(self):
        return self.__record.pop(-1)

    def new_game(self):
        """新規対局作成"""
        self.__grundy_list_obj = GrundyListObj.make(
            self.__rest, set(self.__numbers_to_choose))
