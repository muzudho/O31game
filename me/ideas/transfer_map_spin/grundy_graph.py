from kernel.math.grundy_sequence import GrundySequence
from kernel.math.stone_sequence import StoneSequence

from ideas.transfer_map_spin.transposition_table import TranspositionTable
from ideas.transfer_map_spin.trident_hair import TridentHair


class GrundyGraph:

    @staticmethod
    def make(drawing_columns, drawing_rows, a, b, c, ha, hb, hc):

        ins = GrundyGraph(S={a, b, c}, len_Nz=drawing_columns+c)

        GrundyGraph.__make_each_tridents_from(
            ins, drawing_columns, drawing_rows, a, b, c, ha, hb, hc,
            ins.root_point, ins.tp_table)
        return ins

    @staticmethod
    def __make_each_tridents_from(ins, drawing_columns, drawing_rows, a, b, c, ha, hb, hc, src_point, tp_table):
        sx = src_point[0]
        sy = src_point[1]
        if sx < drawing_columns and sy < drawing_rows:
            """指定の範囲内のみモデル作成"""

            trident = TridentHair.make(
                src_point,
                a=a,
                b=b,
                c=c,
                ha=ha,
                hb=hb,
                hc=hc)

            hash_key = trident.create_hash()

            if not tp_table.contains_key(hash_key):
                """存在しない三本毛なら登録"""
                tp_table.add_trident(hash_key, trident)

                GrundyGraph.__make_each_tridents_from(
                    ins, drawing_columns, drawing_rows, a, b, c, ha, hb, hc,
                    trident.a_point, tp_table)
                """a点から生えている三本毛"""

                GrundyGraph.__make_each_tridents_from(
                    ins, drawing_columns, drawing_rows, a, b, c, ha, hb, hc,
                    trident.b_point, tp_table)
                """b点から生えている三本毛"""

                GrundyGraph.__make_each_tridents_from(
                    ins, drawing_columns, drawing_rows, a, b, c, ha, hb, hc,
                    trident.c_point, tp_table)
                """c点から生えている三本毛"""

    def __init__(self, S: set, len_Nz: int):
        self.__len_Nz = len_Nz
        self.__grundy_sequence = GrundySequence.make(S=S, len_N=len_Nz-1)
        self.__stone_sequence = StoneSequence.make(S=S, len_N=len_Nz-1)

        self.__tp_table = TranspositionTable()
        """三本毛のテーブル"""
        self.__root_point = (0, 0)  # x, y
        """根の点"""

    @property
    def len_Nz(self):
        return self.__len_Nz

    @property
    def grundy_sequence(self):
        return self.__grundy_sequence

    @property
    def stone_sequence(self):
        return self.__stone_sequence

    @property
    def tp_table(self):
        return self.__tp_table

    @property
    def root_point(self):
        return self.__root_point
