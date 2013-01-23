from PIL import Image

from numpy import average

def flatten(arr):
    return [item for sublist in arr for item in sublist]

def v_average(arr, i, j):
    values = []
    for y in [-1, 1]:
        try:
            value = arr[i + y][j]#arr[i][j + y]
            values.append(value)
        except IndexError, e:
            continue
    #return sum(values) / len(values)
    return int(average(values))

def l_average(arr, i, j):
    values = []
    for x in [-1, 1]:
        try:
            value = arr[i][j + x]#arr[i + x][j]
            values.append(value)
        except IndexError, e: 
            continue
    #return sum(values) / len(values)
    return int(average(values))

def p_average(arr, i, j):
    values = []
    for x in [-1, 1]:
        try:
            value = arr[i][j + x]#[i + x][j]
            values.append(value)
        except IndexError, e:
            continue
    for y in [-1, 1]:
        try:
            value = arr[i + y][j]#[i][j + y]
            values.append(value)
        except IndexError, e:
            continue
    return int(average(values))#return sum(values) / len(values)

def x_average(arr, i, j):
    values = []
    for x in [-1, 1]:
        for y in [-1, 1]:
            try:
                value = arr[i + x][j + y]
                values.append(value)
            except IndexError, e:
                continue
    return int(average(values))#return sum(values) / len(values)

def is_even(element):
    return element % 2 == 0

def get_arr(filename):
    image = Image.open(filename)
    image.convert('RGB')
    pixels = list(image.getdata())
    width, height = image.size
    pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
    new_arr = []
    pcolor = []
    mode = "RGB"
    for i, row in enumerate(pixels):
        for j, cvalue in enumerate(row):
            if is_even(i):
                if is_even(j):
                    new_arr.append((l_average(pixels, i, j), cvalue, v_average(pixels, i, j)))
                else:
                    new_arr.append((cvalue, p_average(pixels, i, j), x_average(pixels, i, j)))
            else:
                if is_even(j):
                    new_arr.append((x_average(pixels, i, j), p_average(pixels, i, j), cvalue))
                else:
                    new_arr.append((v_average(pixels, i, j), cvalue, l_average(pixels, i, j)))
    im2 = Image.new(mode, size=(width,height))
    im2.putdata(new_arr)
    im2.save('output.JPG')

if __name__ == '__main__':
    get_arr('image_bayer.jpg')
