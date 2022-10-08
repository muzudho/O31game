from ideas.transfer_map_spin.transposition_table import TranspositionTable
from ideas.transfer_map_spin.transposition_color_table import TranspositionColorTable
from ideas.transfer_map_spin.trident_hair import TridentHair
from ideas.transfer_map_spin.nim_constants import nim_constants


class GrundyGraph:

    @staticmethod
    def make(drawing_columns, drawing_rows, a, b, c, ha, hb, hc):

        ins = GrundyGraph()

        GrundyGraph.__make_each_tridents_from(
            ins, drawing_columns, drawing_rows, a, b, c, ha, hb, hc,
            ins.root_point, ins.tp_table, nim_constants.stonecolor_x, ins.src_color_table)
        return ins

    @staticmethod
    def __make_each_tridents_from(ins, drawing_columns, drawing_rows, a, b, c, ha, hb, hc, src_point, tp_table, src_stonecolor, src_color_table):
        trident = TridentHair.make(
            src_point,
            columns=drawing_columns,
            rows=drawing_rows,
            a=a,
            b=b,
            c=c,
            ha=ha,
            hb=hb,
            hc=hc)

        if trident is not None:
            """指定の範囲内のみ描画"""

            hash_key = trident.create_hash()
            print(f"src({trident.src_point}) hash_key:{hash_key}")

            if not tp_table.contains_key(hash_key):
                """存在しない三本毛なら登録"""
                tp_table.add_trident(hash_key, trident)
                src_color_table.add_stonecolor(
                    trident.src_point, src_stonecolor)
                print(
                    f"新規　 src({trident.src_point}) src_stonecolor:{src_stonecolor}")

                GrundyGraph.__make_each_tridents_from(
                    ins, drawing_columns, drawing_rows, a, b, c, ha, hb, hc,
                    trident.a_point, tp_table, nim_constants.stonecolor_a, src_color_table)
                """a点から生えている三本毛"""

                GrundyGraph.__make_each_tridents_from(
                    ins, drawing_columns, drawing_rows, a, b, c, ha, hb, hc,
                    trident.b_point, tp_table, nim_constants.stonecolor_b, src_color_table)
                """b点から生えている三本毛"""

                GrundyGraph.__make_each_tridents_from(
                    ins, drawing_columns, drawing_rows, a, b, c, ha, hb, hc,
                    trident.c_point, tp_table, nim_constants.stonecolor_c, src_color_table)
                """c点から生えている三本毛"""
            else:
                """存在する三本毛なら"""
                exist_src_stonecolor = src_color_table.get_stonecolor(
                    trident.src_point)
                if exist_src_stonecolor < src_stonecolor:
                    """上書きできる石の色なら"""
                    src_color_table.add_stonecolor(
                        trident.src_point, src_stonecolor)  # Update
                    print(
                        f"上書き src({trident.src_point}) exist_src_stonecolor:{exist_src_stonecolor} src_stonecolor:{src_stonecolor}")
                else:
                    print(
                        f"無視　 src({trident.src_point}) exist_src_stonecolor:{exist_src_stonecolor} src_stonecolor:{src_stonecolor}")

    def __init__(self):
        self.__tp_table = TranspositionTable()
        """三本毛のテーブル"""
        self.__src_color_table = TranspositionColorTable()
        """重なる始点の優先色テーブル"""
        self.__root_point = (0, 0)  # x, y
        """根の点"""

    @property
    def tp_table(self):
        return self.__tp_table

    @property
    def src_color_table(self):
        return self.__src_color_table

    @property
    def root_point(self):
        return self.__root_point
