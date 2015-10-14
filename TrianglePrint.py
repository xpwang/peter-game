def printTriangle(size):
    mid = size >> 1;
    levels = (size + 1) >> 1
    space = ' '
    dot = '*'
    for level in range(levels):
        left = mid - level;
        right = mid + level;
        levelRes = ''
        for index in range(size):
            if index < left:
                levelRes = levelRes + space
            elif index <= right:
                levelRes = levelRes + dot
        print levelRes

def printTriangle2(size):
    for level in range(size):
        print ' '*(size-level -1) + '*'*(2*level+1)

printTriangle2(5)
