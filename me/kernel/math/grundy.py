from kernel.math.mex import mex


class GrundyListObj:
    """グランディ数のリストを持つオブジェクト"""

    @staticmethod
    def make(len_N: int, S: set):
        """グランディ数生成アルゴリズム

        Parameters
        ----------
        len_N : int
            山の石の数（ゲーム上、最大数）
        S : set
            サブトラクションセット

        Returns
        -------
        grundy_list_obj : GrundyListObj
        """

        # グランディ数の配列のサイズ確定
        grundy_list = [0] * len_N

        # 昇順ソート
        S_list = list(S)
        S_list.sort()

        for i in range(0, len_N+1):
            """i は局面の石の数"""

            T = []
            """T は 隣接する遷移先のグランディ数のリスト"""

            for s in S_list:
                """s は 除去可能数"""

                ti = i-s
                """ti は 遷移先の局面の石の数"""

                if ti < 0:
                    # 石の数が負数の局面は無いのでスキップ
                    continue

                t = grundy_list[ti]
                """t は 遷移先の局面のグランディ数"""

                T.append(t)

            grundy = mex(T)
            """grundy は、この局面のグランディ数"""

            grundy_list[i] = grundy

        return GrundyListObj(grundy_list)

    def __init__(self, grundy_list: list):

        self.__grundy_list = grundy_list
        """添え字は、盤上の石の数 n （ 0 ～ len(N) ）"""

    @property
    def grundy_list(self):
        """グランディ数のリスト。
        添え字は、盤上の石の数 n （ 0 ～ len(N) ）"""
        return self.__grundy_list
