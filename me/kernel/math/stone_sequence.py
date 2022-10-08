from ideas.transfer_map_victory.nim_constants import nim_constants


class StoneSequence:
    @staticmethod
    def make(S: set, len_N: int):

        # グランディ数の配列のサイズ確定。 0 を含めるので 1 足す
        len_Nz = len_N + 1
        sequence = [""] * len_Nz

        # 昇順ソート a < b < c
        S_list = list(S)
        S_list.sort()

        da = S_list[0]
        db = S_list[1]
        dc = S_list[2]

        for a in range(0, len_Nz, da):
            sequence[a] += "a"

        for b in range(0, len_Nz, db):
            sequence[b] += "b"

        for c in range(0, len_Nz, dc):
            sequence[c] += "c"

        return StoneSequence(sequence)

    def __init__(self, sequence):
        self.__sequence = sequence

    def get_largest_stonecolor_at(self, i):
        text = self.__sequence[i]
        print(f"i:{i} text:{text} len(text):{len(text)}")
        if 0 < len(text):
            last_char = text[len(text)-1]
            print(f"last_char:{last_char}")

            if last_char == "a":
                return nim_constants.stonecolor_a

            if last_char == "b":
                return nim_constants.stonecolor_b

            if last_char == "c":
                return nim_constants.stonecolor_c

        return nim_constants.stonecolor_x
