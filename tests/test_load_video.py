from src.load_video import reduced_frame_numbers, turntable_filenames_from_frame_numbers, turntable_frame_numbers


def test_reduced_frame_numbers():
    assert [3, 10, 17] == reduced_frame_numbers(total_count=20, reduction=7, offset=3)


def test_turntable_filenames_from_frame_numbers():
    expected = [
        '../videos/turntable_frames/turntable_0123.png',
        '../videos/turntable_frames/turntable_2220.png'
    ]
    assert turntable_filenames_from_frame_numbers([123, 2220]) == expected


def test_turntable_frame_numbers():
    expected = [17, 1017, 2017]
    actual = turntable_frame_numbers(reduction=1000, offset=17)
    assert actual == expected

def test_turntable_frame_numbers_all():
    expected = [1 + f for f in range(2220)]
    actual = turntable_frame_numbers()
    assert actual == expected
