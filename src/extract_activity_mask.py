import imageio

from src.load_video import generate_turntable_frames
import numpy as np


def extract_activity_mask(frame_generator):
    frame_count, mean, deviation = extract_deviation_and_mean(frame_generator)
    peak_deviation = np.max(deviation)
    print(peak_deviation)
    mask = deviation / peak_deviation
    print(frame_count)
    return mask

def extract_deviation_and_mean(frame_generator):
    summed_images = None
    sum_of_squared_images = None
    frame_count = 0.0
    for bytes_frame in frame_generator:
        frame = np.asarray(bytes_frame, dtype=np.float64)
        frame_count += 1
        if summed_images is None:
            summed_images = np.zeros_like(frame, dtype=np.float64)
        if sum_of_squared_images is None:
            sum_of_squared_images = np.zeros_like(frame, dtype=np.float64)
        summed_images += frame
        sum_of_squared_images += frame * frame
    mean = summed_images / frame_count
    mean_squared = sum_of_squared_images / frame_count
    variance_squared = mean_squared - mean * mean
    deviation = np.sqrt(variance_squared)
    return frame_count, mean, deviation


if __name__ == '__main__':
    activity_mask = extract_activity_mask(
        generate_turntable_frames(reduction=1))
    scaled_mask = activity_mask * 255
    scaled_byte_mask = np.asarray(scaled_mask, dtype=np.ubyte)
    imageio.imwrite("../videos/mask.png", scaled_byte_mask, "png")

