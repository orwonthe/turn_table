from datetime import datetime

import imageio as imageio


def generate_turntable_frames(reduction=1):
    file_names = turntable_filenames_from_frame_numbers(
            turntable_frame_numbers(reduction=reduction)
        )
    yield from generate_video_frames_from_file_list(file_names)

def generate_video_frames_from_file_list(file_name_list):
    for file_name in file_name_list:
        yield imageio.imread(file_name)

def turntable_frame_numbers(total_count=2220, reduction=1, offset=1):
    return reduced_frame_numbers(total_count, reduction, offset)


def turntable_filenames_from_frame_numbers(frame_numbers):
    return [f'../videos/turntable_frames/turntable_{frame:04d}.png' for frame in frame_numbers]


def reduced_frame_numbers(total_count, reduction, offset):
    return [frame + offset for frame in range(total_count) if frame % reduction == 0]


if __name__ == '__main__':
    start_time = datetime.now()
    images = list(generate_turntable_frames(reduction=100))
    stop_time = datetime.now()
    elapsed_time = stop_time - start_time
    print(elapsed_time)
    first_image = images[0]
    print (first_image.shape, first_image.itemsize)
