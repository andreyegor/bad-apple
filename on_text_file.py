import transform_frames
from time import sleep

path = 'screen.txt'
for i in range(1, 6571, 6):
    with open(path, 'w+') as f:
        f.seek(0)
        frame = transform_frames.get_converted_image(
            f'frames/frame{i}.jpg', width=230)
        f.write(frame+'\n'+str(i))
        sleep(0.0626)
