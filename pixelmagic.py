"""
CPE 101
Section 6
Project 5
Pete Woo
pswoo@calpoly.edu
"""
import sys
import copy
file = sys.argv
not_valid = 0

try:
    mode = file[1]
except:
    mode = "nothing"

if mode == 'decode' or mode == 'fade' or mode == 'denoise':
    try:
        test = open(file[2], 'r')
    except:
        print(f'Error: Unable to Open {file[2]}')
        not_valid = 1
else:
    print('Error: Invalid Mode')


def fine_images(pixels):
    """This function decodes an image.
    Args:
      pixels(list): A list of pixels
    Returns:
      list: A decoded list of pixels
    """
    for index in range(3, len(pixels)):
        if int(pixels[index][0]) * 10 > 255:
            pixels[index][0] = '255'
            pixels[index][0] = '255'
            pixels[index][0] = '255'
        else:
            pixels[index][0] = str(int(pixels[index][0]) * 10)
            pixels[index][1] = pixels[index][0]
            pixels[index][2] = pixels[index][0]
    return pixels


def fade_image(pixels, width, row, col, radius):
    """This function fades an image.
    Args:
      pixels(list): A list of pixels
      width(str): The number of pixels for the width
      row(str): The row of the center pixel
      col(str): The column of the center pixel
      radius(str): The radius of the fade
    Returns:
      list: A list with pixels of faded image
    """
    height = 0
    real_width = 0
    for index in range(3, len(pixels)):
        if index % int(width) == 0:
            height += 1
            real_width = 0
        distance = int(
            ((real_width - int(row))**2 + (height - int(col))**2)**0.5)
        scale = ((int(radius) - distance) / int(radius))
        if distance > int(radius):
            scale = 0.2
        if scale < 0.2:
            scale = 0.2
        pixels[index][0] = str(int(int(pixels[index][0]) * scale))
        pixels[index][1] = str(int(int(pixels[index][1]) * scale))
        pixels[index][2] = str(int(int(pixels[index][2]) * scale))
        real_width += 1
    return pixels


def denoise_image(pixels, width, height, reach, beta):
    """This function denoises an image.
    Args:
      pixels(list): A list of pixels
      width(str): The number of pixels for the width
      height(str): The number of pixels for the height
      reach(str): The number of pixels to test per pixel
      beta(str): The number to judge if a pixel is good enough to modify
    Returns:
      list: A list with pixels of faded image
    """
    new_pixels = copy.deepcopy(pixels)
    current_height = 0
    current_width = 0
    x_val = 0
    y_val = 0
    med = 0
    neighbors = []
    for index in range(3, len(pixels)):
        if index % int(width) == 0:
            current_height += 1
            current_width = 0
        for not_used in range(0, (2 * int(reach) + 1)**2):
            x_val += 1
            if x_val == int(reach) + 1:
                x_val = -1 * int(reach)
                y_val += 1
            if index < 0 or index > len(new_pixels) - 3:
                continue
            if current_width == 0 or current_width == 1 or current_width == 2:
                continue
            if (current_width == int(width)) or (current_width == int(width) -1) or (current_width == int(width) - 2):
                continue
            neighbors.append(int(pixels[index + x_val][0]))
        insertion_sort(neighbors)
        if neighbors != []:
            med = neighbors[len(neighbors) // 2]
        if abs(int(pixels[index][0]) - med) / (int(pixels[index][0]) + 0.1) > float(beta):
            new_pixels[index][0] = str(med)
            new_pixels[index][1] = str(med)
            new_pixels[index][2] = str(med)
        x_val = -1 * int(reach)
        y_val = -1 * int(reach)
        current_width += 1
        neighbors = []
    return new_pixels


def insertion_sort(int_list):
    """This function sorts a list of interger numbers.
    Args:
      int_list(list): A list of unsorted numbers
    Returns:
      list: A list of sorted numbers
    """
    for index, value in enumerate(int_list):
        sort_val = int_list[index]
        while int(int_list[index - 1]) > sort_val and index > 0:
            int_list[index], int_list[index - 1] = int_list[index - 1], int_list[index]
            index = index - 1
    return int_list


def main():
    """This function is the main function.
    """
    test.close()
    with open(file[2], 'r+') as content:
        lines = content.readlines()
        pixels = []
        for line in lines:
            line = line.strip()
            line = line.split()
            pixels.append(line)
        if file[1] == 'decode':
            decoded = fine_images(pixels)
            out = open('decoded.ppm', 'w')
            for line in decoded:
                joining = ' '.join(line)
                out.write(f'{joining}\n')
            out.close()
        if file[1] == 'fade':
            faded = fade_image(pixels, pixels[1][0], file[3], file[4], file[5])
            out = open('faded.ppm', 'w')
            for line in faded:
                joining = ' '.join(line)
                out.write(f'{joining}\n')
            out.close()
        if file[1] == 'denoise':
            try:
                reach = file[3]
            except:
                reach = 2
            try:
                beta = file[4]
            except:
                beta = 0.2
            denoised = denoise_image(pixels, pixels[1][0], pixels[1][1], reach, beta)
            out = open('denoised.ppm', 'w')
            for line in denoised:
                joining = ' '.join(line)
                out.write(f'{joining}\n')
            out.close()


if __name__ == '__main__':
    if not_valid == 0:
        main()
