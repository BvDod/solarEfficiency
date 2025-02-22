# converts CMYK color tuple to RGB color tuple
def cmyk_to_rgb(color, rgb_scale=255):
    cmyk_scale = 1
    c, m, y, k = color
    r = rgb_scale * (1.0 - c / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    g = rgb_scale * (1.0 - m / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    b = rgb_scale * (1.0 - y / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    r, g, b = int(r), int(g), int(b)
    return [r, g, b]