from PIL import Image
import data
from time import sleep

pattern = data.braille_pattern


def start():
    for i in range(1, 6571):
        frame = get_converted_image(f'frames/frame{i}.jpg')
        print(frame)
        sleep(1/30)


def get_converted_image(path, width=204):
    image_data = get_image_data(path, width=width)
    blocks = get_blocks(image_data)
    braille = convert_blocks_to_braille(blocks)
    return braille

# получаю и кропаю картинку, получаю информацию по цвету пикселей, а потом преобразую в чб


def get_image_data(path, width=202):
    ratio = 0.55
    with Image.open(path) as image:
        true_width, true_height = image.size
        height = int(width*(true_height/true_width)*ratio)
        width += 2-(width % 2)
        height += 3-(height % 3)
        image = image.resize((width, height), Image.ANTIALIAS)
        pixels = list(image.getdata())
    for i, e in enumerate(pixels):
        pixels[i] = 0 if sum(e) < 383 else 1
    return [pixels[i * width:(i + 1) * width] for i in range(height)]


def get_blocks(image_data, width=2, heigth=3):
    blocks = []
    for y in range(0, len(image_data)-1, heigth):
        blocks.append([])
        for x in range(0, len(image_data[0])-1, width):
            blocks[-1].append((image_data[y][x], image_data[y][x+1],
                               image_data[y+1][x], image_data[y+1][x+1],
                               image_data[y+2][x], image_data[y+2][x+1],
                               ))
    return (blocks)

# получаю арт шрифтом брайля из информации о блоках


def convert_blocks_to_braille(blocks):
    braille = ''
    for e in blocks:
        for j in e:
            braille += pattern[j]
        braille += '\n'
    return braille


if __name__ == '__main__':
    start()
