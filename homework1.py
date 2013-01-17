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
    values = [v_average(arr, i, j), l_average(arr, i, j)]
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

def get_arr(filename):
    image = Image.open(filename)
    pixels = list(image.getdata())
    width, height = image.size
    pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
    new_arr = [[(0,0,0)]*width for i in xrange(height)]
    for i, row in enumerate(pixels):
        for j, cvalue in enumerate(row):
            if i % 2 == 0:
                if j % 2 == 0:
                    new_arr[i][j] = (l_average(pixels, i, j), cvalue, v_average(pixels, i, j))
                else:
                    new_arr[i][j] = (cvalue, p_average(pixels, i, j), x_average(pixels, i, j))
            else:
                if j % 2 == 0:
                    new_arr[i][j] = (x_average(pixels, i, j), p_average(pixels, i, j), cvalue)
                else:
                    new_arr[i][j] = (v_average(pixels, i, j), cvalue, l_average(pixels, i, j))

    #print flatten(new_arr)
    mode = "RGB"
    im = Image.new(mode, (width, height))#fromstring(mode, (width, height), str(flatten(new_arr)), 'raw', mode, 0, 1)
    im.putdata(flatten(new_arr))
    im.save("output.jpg")

if __name__ == '__main__':
    get_arr('image_bayer.jpg')
