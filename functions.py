class Color:
    pass




def other_color(color: Color):
    from pieces import Color
    return Color.WHITE if color == Color.BLACK else Color.BLACK
