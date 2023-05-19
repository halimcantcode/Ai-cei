class Color:
    pass




def other_color(color: Color):
    from piece import Color
    return Color.WHITE if color == Color.BLACK else Color.BLACK
