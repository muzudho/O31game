

class MusicChord:

    __music_scale = ["", "C", "C#", "D", "D#",
                     "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    """Music scale
    1: C
    2: C#
    3: D
    4: D#
    5: E
    6: F
    7: F#
    8: G
    9: G#
    10: A
    11: A#
    12: B
    """

    @staticmethod
    def stringify(a, b, c):
        """和音
        - ファイル名にも使える文字
        """

        if a < len(MusicChord.__music_scale):
            scale = MusicChord.__music_scale[a]
        else:
            scale = ""

        d_a_b = b - a
        d_b_c = c - b

        if d_a_b == 4 and d_b_c == 3:
            """メジャーコード"""
            chord = ""
        elif d_a_b == 3 and d_b_c == 4:
            """m マイナーコード"""
            chord = "m"
        elif d_a_b == 5 and d_b_c == 2:
            """sus4 サスフォー"""
            chord = "sus4"
        elif d_a_b == 4 and d_b_c == 2:
            """-5 フラットファイブ"""
            chord = "-5"
        elif d_a_b == 4 and d_b_c == 4:
            """aug オーギュメント"""
            chord = "aug"
        elif d_a_b == 3 and d_b_c == 3:
            """dim ディミニッシュ"""
            chord = "dim"
        else:
            """該当無し"""
            scale = ""
            chord = ""

        return f"{scale}{chord}"
