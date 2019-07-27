def is_between(pos, pos1, pos2):
    (x, y), (minX, minY), (maxX, maxY) = pos, pos1, pos2
    return True if x >= minX and x <= maxX and y >= minY and y <= maxY else False