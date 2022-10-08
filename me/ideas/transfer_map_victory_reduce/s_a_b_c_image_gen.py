"""
pip install opencv-python
pip install Pillow

cd me

python.exe -m ideas.vector_coordinate.main
"""
import cv2
import numpy as np
from kernel.math.eo_code import EoCode
from kernel.math.music_chord import MusicChord
from ideas.transfer_map_victory.grundy_graph import GrundyGraph
from ideas.transfer_map_victory.nim_constants import nim_constants


def gen_s_a_b_c_image(a, b, c, zoom=1.0, is_temporary=True):
    """
    a < b < c

    Parameters
    ----------
    zoom : float
        倍率。1倍はかなりでかい
    """

    eo_code = EoCode.stringify(a, b, c)
    music_chord = MusicChord.stringify(a, b, c)
    display_max_number = 50

    d_a_b = b-a
    d_b_c = c-b
    d_c_apb = c-(a+b)
    minimum_d = min([d_a_b, d_b_c, d_c_apb])
    maximum_d = max([d_a_b, d_b_c, d_c_apb])
    """a,b,cの間隔"""

    # x軸、y軸、z軸と考えれば、３次元の格子になる
    ha = (-a*b)/2
    hb = 0
    hc = c/2

    #hc = a+b
    # hb = 0  # bは水平
    # ha = a  # aはナナメ
    """width と height"""

    margin_left = 20
    margin_right = 5
    margin_top = 2500
    margin_bottom = 5

    columns = 80
    rows = 80
    drawing_columns = columns
    drawing_rows = rows

    char_base_width = -10
    char_base_height = 5
    char_width = 50
    char_height = 50
    """一文字の幅の目安"""

    color_black = (55, 55, 55)  # (B,G,R)
    color_red = (90, 90, 220)
    color_green = (90, 220, 90)
    color_blue = (220, 90, 90)
    color_cyan = (220, 220, 90)
    color_magenta = (220, 90, 220)
    color_yellow = (90, 220, 220)
    """色"""

    line_thickness = 1
    """線の太さ"""

    def make_image():
        image_width = int(
            (columns * char_width + margin_left + margin_right) * zoom)
        image_height = int(
            (rows * char_height+margin_top + margin_bottom)*2/3*zoom)

        # 画像データは数値の配列
        monochrome_color = 240  # 0黒→255白
        canvas = np.full((image_height, image_width, 3),
                         monochrome_color, dtype=np.uint8)

        # モデル作成
        grundy_graph = GrundyGraph.make(
            drawing_columns=drawing_columns,
            drawing_rows=drawing_rows,
            a=a,
            b=b,
            c=c,
            ha=ha,
            hb=hb,
            hc=hc)

        # １つの x に、複数の y があるので、最小の y だけ残します
        x_sequence_with_smallest_y = {}
        for trident in grundy_graph.tp_table.values():
            sx = trident.src_point[0]
            sy = trident.src_point[1]

            if sx in x_sequence_with_smallest_y:
                element = x_sequence_with_smallest_y[sx]
                if sy < element[0]:
                    x_sequence_with_smallest_y[sx] = (sy, trident)  # Update
            else:
                x_sequence_with_smallest_y[sx] = (sy, trident)

        draw_subtraction_set(canvas, (0, 0))
        """サブストラクションセット描画"""

        draw_x_stone(canvas, grundy_graph.root_point)
        """根の点描画"""

        for key in x_sequence_with_smallest_y:
            element = x_sequence_with_smallest_y[key]
            trident = element[1]
            draw_trident(canvas, trident, grundy_graph)
            """三本毛の描画"""

        if music_chord != "":
            music_chord_text = f"_{music_chord}"
        else:
            music_chord_text = ""

        if is_temporary:
            tmp_text = "_tmp"
        else:
            tmp_text = ""

        cv2.imwrite(
            f"./output_tmp/transfer_vict_redu_s_{a:02}_{b:02}_{c:02}_{eo_code}{music_chord_text}{tmp_text}.png", canvas)
        """画像出力"""

    def draw_subtraction_set(canvas, point):
        """サブトラクションセットを表示"""
        x = point[0]
        y = point[1]
        location = (int((x+char_base_width+margin_left)*zoom),
                    int((y+char_base_height+margin_left)*zoom))
        font_scale = 1.0 * zoom

        cv2.putText(canvas,
                    f"S = {{   ,   ,    }} {eo_code} {music_chord}",
                    location,  # x,y
                    None,  # font
                    font_scale,  # font_scale
                    color_black,  # color
                    0)  # line_type

        cv2.putText(canvas,
                    f"      {a:2}",
                    location,  # x,y
                    None,  # font
                    font_scale,  # font_scale
                    color_red,  # color
                    0)  # line_type

        cv2.putText(canvas,
                    f"          {b:2}",
                    location,  # x,y
                    None,  # font
                    font_scale,  # font_scale
                    color_green,  # color
                    0)  # line_type

        cv2.putText(canvas,
                    f"              {c:2}",
                    location,  # x,y
                    None,  # font
                    font_scale,  # font_scale
                    color_blue,  # color
                    0)  # line_type

    def draw_trident(canvas, trident, grundy_graph):
        """三本毛を描く"""

        sx = trident.src_point[0]
        ax = trident.a_point[0]
        ax_grundy_num = grundy_graph.grundy_sequence.get_grundy_at(ax)
        bx = trident.b_point[0]
        bx_grundy_num = grundy_graph.grundy_sequence.get_grundy_at(bx)
        cx = trident.c_point[0]
        cx_grundy_num = grundy_graph.grundy_sequence.get_grundy_at(cx)
        """点の位置x"""

        # 石は必ず描画

        if ax_grundy_num == 0:
            draw_x_stone(canvas, trident.a_point)
        else:
            draw_stone(canvas, trident.a_point,
                       get_color_from_stonecolor(grundy_graph.stone_sequence.get_largest_stonecolor_at(ax)))
        """終点a石"""

        if bx_grundy_num == 0:
            draw_x_stone(canvas, trident.b_point)
        else:
            draw_stone(canvas, trident.b_point,
                       get_color_from_stonecolor(grundy_graph.stone_sequence.get_largest_stonecolor_at(bx)))
        """終点b石"""

        if cx_grundy_num == 0:
            draw_x_stone(canvas, trident.c_point)
        else:
            draw_stone(canvas, trident.c_point,
                       get_color_from_stonecolor(grundy_graph.stone_sequence.get_largest_stonecolor_at(cx)))
        """終点c石"""

        # エッジの描画
        # 三本毛の根 が、グランディ数 0 のものだけ描けば必勝ルート
        sx_grundy_number = grundy_graph.grundy_sequence.get_grundy_at(sx)
        if 0 == sx_grundy_number:
            # 始点と終点の組み合わせによって色を変える
            draw_line(canvas, trident.src_point, trident.a_point,
                      color_red)
            """s-->a線"""

            draw_line(canvas, trident.src_point, trident.b_point,
                      color_green)
            """s-->b線"""

            draw_line(canvas, trident.src_point, trident.c_point,
                      color_blue)
            """s-->c線"""

    def get_color_from_stonecolor(stonecolor):
        if stonecolor == nim_constants.stonecolor_x:
            return color_black

        if stonecolor == nim_constants.stonecolor_a:
            return color_red

        if stonecolor == nim_constants.stonecolor_b:
            return color_green

        if stonecolor == nim_constants.stonecolor_c:
            return color_blue

        raise ValueError(f"unexpected stonecolor:{stonecolor}")

    def draw_x_stone(canvas, point):
        """x石を描く"""
        x = point[0]
        y = point[1]
        cv2.putText(canvas,
                    "x",
                    (int((x*char_width+char_base_width+margin_left)*zoom),
                     int((y*char_height+char_base_height+margin_top)*zoom)),  # x,y
                    None,  # font
                    zoom,  # font_scale
                    color_black,  # color
                    0)  # line_type

    def draw_stone(canvas, point, color_stone):
        """石を描く"""
        x = point[0]
        y = point[1]

        if x <= display_max_number:
            label = f"{x}"
        else:
            label = ""

        cv2.putText(canvas,
                    label,
                    (int((x*char_width+char_base_width+margin_left)*zoom),
                     int((y*char_height+char_base_height+margin_top)*zoom)),  # x,y
                    None,  # font
                    zoom,  # font_scale
                    color_stone,  # color
                    0)  # line_type

    def draw_line(canvas, src_point, dst_point, color_line):
        """線の描画"""
        sx = src_point[0]
        sy = src_point[1]
        dx = dst_point[0]
        dy = dst_point[1]
        cv2.line(canvas, (int((sx*char_width+margin_left)*zoom), int((sy*char_height+margin_top)*zoom)),
                 (int((dx*char_width+margin_left)*zoom), int((dy*char_height+margin_top)*zoom)), color_line, thickness=line_thickness)

    make_image()
