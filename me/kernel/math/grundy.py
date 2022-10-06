from kernel.math.mex import mex


class GrundySequence:
    """グランディ数列

    X軸上の任意の１点だけのグランディ数が欲しい、ということはできず、
    グランディ数は、原点から X軸上の任意の点までのグランディ数の配列として用意される"""

    @staticmethod
    def make(S: set, len_N: int):
        """グランディ数生成アルゴリズム

        Parameters
        ----------
        len_N : int
            山の石の数（ゲーム上、最大数）
        S : set
            サブトラクションセット

        Returns
        -------
        grundy_sequence : GrundySequence
        """

        # グランディ数の配列のサイズ確定。 0 を含めるので 1 足す
        len_Nz = len_N + 1
        grundy_list = [0] * len_Nz

        # 昇順ソート a < b < c
        S_list = list(S)
        S_list.sort()

        for i in range(0, len_Nz):
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

        return GrundySequence(grundy_list, S_list)

    def __init__(self, grundy_list: list, S_list: list):

        self.__grundy_list = grundy_list
        """添え字は、盤上の石の数 n （ 0 ～ len(N) ）"""

        self.__S_list = S_list
        """サブストラクションセット"""

    @property
    def len(self):
        return len(self.__grundy_list)

    @property
    def S_list(self):
        return self.__S_list

    def get_grundy_at(self, i: int):
        """グランディ数

        Parameters
        ----------
        i : int
            局面の石の数
        """
        return self.__grundy_list[i]

    def get_bit_grundy_at(self, i: int):
        """ビット グランディ数

        Parameters
        ----------
        i : int
            局面の石の数
        """
        if self.__grundy_list[i] == 0:
            return 0

        return 1


class DameColorSequence():
    """囲碁の駄目のようにグランディ数 0 を着色"""

    @staticmethod
    def make(grundy_sequence):
        len_Nz = grundy_sequence.len
        dame_color_list = [0] * len_Nz

        adjacent_eye_color = 0  # 黒

        # 往路
        for i in range(0, len_Nz):
            grundy_num = grundy_sequence.get_grundy_at(i)

            if grundy_num != 0:  # 石
                if i % grundy_sequence.S_list[2] == 0:
                    eye_color = 3  # 青
                elif i % grundy_sequence.S_list[1] == 0:
                    eye_color = 2  # 緑
                elif i % grundy_sequence.S_list[0] == 0:
                    eye_color = 1  # 赤
                else:
                    eye_color = 0  # 黒

                adjacent_eye_color = eye_color
            else:  # 目
                dame_color_list[i] = adjacent_eye_color

        # 復路
        for i in range(1, len_Nz):
            rev_i = len_Nz - i - 1

            grundy_num = grundy_sequence.get_grundy_at(rev_i)

            if grundy_num != 0:  # 石
                if rev_i % grundy_sequence.S_list[2] == 0:
                    eye_color = 3  # 青
                elif rev_i % grundy_sequence.S_list[1] == 0:
                    eye_color = 2  # 緑
                elif rev_i % grundy_sequence.S_list[0] == 0:
                    eye_color = 1  # 赤
                else:
                    eye_color = 0  # 黒

                adjacent_eye_color = eye_color
            else:  # 目
                dame_color = dame_color_list[rev_i]
                if dame_color != adjacent_eye_color:
                    """駄目"""
                    dame_color_list[rev_i] = 0  # 黒

        return DameColorSequence(dame_color_list)

    def __init__(self, dame_color_list):
        self.__dame_color_list = dame_color_list

    def get_dame_color_at(self, i):
        return self.__dame_color_list[i]
