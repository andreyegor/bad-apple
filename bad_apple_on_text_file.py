import transform_frames
from time import sleep

path = 'screen.txt'
for i in range(1, 3970, 3):
    with open(path, 'w+') as f:
        f.seek(0)
        braille = transform_frames.get_converted_image(
            f'frames/frame{i}.jpg', width=230)
        frame = ''
        for e in braille:
            frame += ''.join(e)+'\n'
        f.write(frame+'\n'+str(i))
        sleep(0.0626)
