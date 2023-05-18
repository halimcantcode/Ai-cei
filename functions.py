class Color:
    pass



def isInbounds(i, j):
    return 0 <= i <= 7 and 0 <= j <= 7


def other_color(color: Color):
    from pieces import Color
    return Color.WHITE if color == Color.BLACK else Color.BLACK
