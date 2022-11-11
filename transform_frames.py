from PIL import Image
import data
from time import sleep


def start():
    for i in range(1, 3970):
        try:
            braille = get_converted_image(f'frames/frame{i}.png')
            for e in braille:
                print(''.join(e))
            sleep(1/60)
        except FileNotFoundError:
            pass


def get_converted_image(path, width=204):
    image_data = get_image_data(path, width=width)
    #image_data = format_image(image_data)
    blocks = get_blocks(image_data)
    braille = convert_blocks_to_braille(blocks)
    return braille

# получаю и кропаю картинку, получаю информацию по цвету пикселей, а потом преобразую в чб


def get_image_data(path, width=204):
    with Image.open(path) as image:
        true_width, true_height = image.size
        height = int(width*(true_height/true_width))
        image = image.resize((width, height), Image.ANTIALIAS)
        pixels = list(image.getdata())
    for i, e in enumerate(pixels):
        pixels[i] = 0 if sum(e) < 383 else 1
    return [pixels[i * width:(i + 1) * width] for i in range(height)]


# форматирую изображение, что бы количество пикселей было кратным числам, НЕ РАБОТАЕТ
def format_image(image_data, width_multiple=2, heigt_multiple=3):
    image_data = image_data.copy()
    # в ширину
    kf = len(image_data[0]) % width_multiple
    if kf:
        for i in range(len(image_data)):
            image_data[i].append([1]*kf)

    # в высоту
    kf = len(image_data) % heigt_multiple
    for i in range(kf):
        image_data.append([1]*len(image_data[0]))

    return image_data

# получаю блоки по 6 пикселей


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
    braille = []
    for e in blocks:
        braille.append([])
        for j in e:
            braille[-1].append(data.braille_pattern[j])
    return braille


if __name__ == '__main__':
    start()
