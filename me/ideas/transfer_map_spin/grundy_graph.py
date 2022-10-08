from ideas.transfer_map_spin.transposition_table import TranspositionTable
from ideas.transfer_map_spin.transposition_color_table import TranspositionColorTable


class GrundyGraph:
    def __init__(self):
        self.__tp_table = TranspositionTable()
        """三本毛のテーブル"""
        self.__src_color_table = TranspositionColorTable()
        """重なる始点の優先色テーブル"""

    @property
    def tp_table(self):
        return self.__tp_table

    @property
    def src_color_table(self):
        return self.__src_color_table
