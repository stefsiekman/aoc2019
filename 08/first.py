import aoc.input
from PIL import Image

w = 25
h = 6


def find_pixel(layers, x, y):
    for layer in layers:
        print(x, y, len(layer))
        p = layer[x + y * w]
        if p == 2:
            continue
        else:
            return tuple([p * 255] * 3)


if __name__ == "__main__":
    lines = aoc.input.input_text()
    layers = []
    layercount = 0
    for l in range(len(lines) // (w * h)):
        layer = []
        for i in range(w * h):
            layer.append(int(lines[i + layercount * (w * h)]))
        layercount += 1
        layers.append(layer)


    min_zeros = None
    the_layer = None
    for layer in layers:
        if min_zeros is None or layer.count(0) < min_zeros:
            min_zeros = layer.count(0)
            the_layer = layer

    pixels = [None] * (w*h)
    for y in range(h):
        for x in range(w):
            pixels[x + y * w] = find_pixel(layers, x, y)

    img = Image.new('RGB', (w,h))
    img.putdata(pixels)
    img.save('out.png')



