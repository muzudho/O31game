class TridentHair:
    """三本毛"""

    @staticmethod
    def make_next_nodes_from(src_point, columns, rows, wa, wb, wc, ha, hb, hc):
        sx = src_point["x"]
        sy = src_point["y"]
        if sx < columns and sy < rows:
            a_point = {"x": sx+wa, "y": sy+ha}
            """次のa点"""

            b_point = {"x": sx+wb, "y": sy+hb}
            """次のb点"""

            c_point = {"x": sx+wc, "y": sy+hc}
            """次のc点"""

            return (src_point, a_point, b_point, c_point)

        return None
