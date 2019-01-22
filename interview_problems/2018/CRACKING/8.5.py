


def mul(a, b):
    def mulR(x, y):
        if y == 0:
            return 0
        elif y == 1:
            return x
        elif y & (y - 1) == 0:
            while y > 1:
                x = x << 1
                y = y >> 1
            return x
        elif y % 2 == 0:
            half_product = mulR(x, y / 2)
            return half_product * half_product
        else:
            return x + mulR(x, y - 1)

    return mulR(a, b) if a >= b else mulR(b, a)


print mul(8, 9)
