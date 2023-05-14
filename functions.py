class Color:
    pass


def isInrectangle(pos, pos0, width, height):
   
    return pos0[0] <= pos[0] <= pos0[0] + width and pos0[1] <= pos[1] <= pos0[1] + height


def isInbounds(i, j):
    return 0 <= i <= 7 and 0 <= j <= 7


def other_color(color: Color):
    from pieces import Color
    return Color.WHITE if color == Color.BLACK else Color.BLACK
