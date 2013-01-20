from PIL import Image

def flatten(arr):
    return [item for sublist in arr for item in sublist]

def v_average(arr, i, j):
    values = []
    for y in [-1, 1]:
        try:
            values.append(arr[i][j + y])
        except IndexError, e: pass
    return sum(values) / len(values)

def l_average(arr, i, j):
    values = []
    for x in [-1, 1]:
        try:
            values.append(arr[i + x][j])
        except IndexError, e: pass
    return sum(values) / len(values)

def p_average(arr, i, j):
    values = []
    for x in [-1, 1]:
        try:
            values.append(arr[i + x][j])
        except IndexError, e: pass
    for y in [-1, 1]:
        try:
            values.append(arr[i][j + y])
        except IndexError, e: pass
    #values = [v_average(arr, i, j), l_average(arr, i, j)]
    return sum(values) / len(values)

def x_average(arr, i, j):
    values = []
    for x in [-1, 1]:
        for y in [-1, 1]:
            try:
                values.append(arr[i + x][j + y])
            except IndexError, e:
                pass
    return sum(values) / len(values)

def is_even(element):
    return element % 2 == 0

def checkerboard():
    filename = 'checkerboard.jpg'
    rimg = Image.open(filename)
    print list(rimg.getdata())
    width, height = 6, 6
    l = []
    for i in xrange(width):
        for j in xrange(height):
            #if is_even(i):
                if is_even(j):
                    l.append((0, 255, 0))
                else:
                    l.append((255, 0, 0))
                    """
                    else:
                        if is_even(j):
                            l.append((0, 0, 255))
                        else:
                            l.append((0, 255, 0))
                    """
    print l
    im = Image.new('RGB', (width, height))
    im.putdata([(255,0,0)]*(width * height))#l)
    im.save(filename)

def get_arr(filename):
    image = Image.open(filename)
    pixels = list(image.getdata())
    width, height = image.size
    pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
    #new_arr = [[(0,0,0)]*width for i in xrange(height)]
    new_arr = []
    for i, row in enumerate(pixels):
        for j, cvalue in enumerate(row):
            if is_even(i):
                if is_even(j):
                    #new_arr[i][j] = (l_average(pixels, i, j), cvalue, v_average(pixels, i, j))
                    new_arr.append((l_average(pixels, i, j), cvalue, v_average(pixels, i, j)))
                else:
                    #new_arr[i][j] = (cvalue, p_average(pixels, i, j), x_average(pixels, i, j))
                    new_arr.append((cvalue, p_average(pixels, i, j), x_average(pixels, i, j)))
            else:
                if is_even(j):
                    #new_arr[i][j] = (x_average(pixels, i, j), p_average(pixels, i, j), cvalue)
                    new_arr.append((x_average(pixels, i, j), p_average(pixels, i, j), cvalue))
                else:
                    #new_arr[i][j] = (v_average(pixels, i, j), cvalue, l_average(pixels, i, j))
                    new_arr.append((v_average(pixels, i, j), cvalue, l_average(pixels, i, j)))
    mode = "RGB"
    im = Image.new(mode, (width, height))
    #im.putdata(flatten(new_arr))
    im.putdata(new_arr)
    im.save("output.jpg")

if __name__ == '__main__':
    checkerboard()
    get_arr('image_bayer.jpg')
