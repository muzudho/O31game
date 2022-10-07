class EoCode:
    """偶奇表記"""

    @staticmethod
    def stringify(a, b, c):
        """文字が潰れると見分けにくいので e の方を大文字にした"""

        if a % 2 == 0:
            eo_a = "E"
        else:
            eo_a = "o"

        if b % 2 == 0:
            eo_b = "E"
        else:
            eo_b = "o"

        if c % 2 == 0:
            eo_c = "E"
        else:
            eo_c = "o"

        return f"{eo_a}{eo_b}{eo_c}"
