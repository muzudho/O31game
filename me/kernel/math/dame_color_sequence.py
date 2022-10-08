class DameColorSequence():
    """WIP 囲碁の駄目のようにグランディ数 0 を着色"""

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
