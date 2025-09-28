import os

import config
import pyramid_tools


def test_write():
    video_dir = config.PROJECT_DIR + '/video_test/'
    pyramid_data = {'data': 5}
    pyramid_tools.write(video_dir, pyramid_data)
    pyramid_file = video_dir + '/pyramid/pyramid.json'
    exists = os.path.exists(pyramid_file)
    if exists:
        # clean up
        os.remove(pyramid_file)
        os.rmdir(video_dir + '/pyramid')
        os.rmdir(video_dir)
    assert exists


def test_read():
    pyr = pyramid_tools.read()
    assert len(pyr) > 0


def test_dimensions():
    video_file_path = config.PROJECT_DIR + \
        '/video/carter-skyers-easiest-goodbye-official-music-video.mp4'
    dimensions = pyramid_tools.dimensions(video_file_path)
    assert len(dimensions) == 2


def test_create_pyramid_level():
    video_file_path = config.PROJECT_DIR + '/' + \
        'video/carter-skyers-easiest-goodbye-official-music-video.mp4'
    audio_file_path = video_file_path.replace('mp4', 'mp3')
    dimensions = pyramid_tools.dimensions(video_file_path)
    level_data = pyramid_tools.create_pyramid_level(
        video_file_path, audio_file_path, dimensions, 0, 1)
    print(f'level_data={level_data}')
    assert level_data
