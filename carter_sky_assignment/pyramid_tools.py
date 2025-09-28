import json
import os

import config
import ffmpeg
from config import logger


def write(video_dir, pyramid_data):
    pyramid_file_dir = video_dir + '/pyramid'
    if not os.path.exists(pyramid_file_dir):
        os.makedirs(pyramid_file_dir)
    pyramid_file_path = pyramid_file_dir + '/pyramid.json'

    try:
        pyramid_file = open(pyramid_file_path, 'w')
    except Exception as e:
        logger.error(
            f'Unable to write {pyramid_file_path} exception={type(e).__name__}')
        quit(-1)

    # write the json
    s_json = json.dumps(pyramid_data, indent=4)
    pyramid_file.write(s_json)

    # close file
    pyramid_file.close()


def read():
    '''
    read pyramid_tools.json file
    '''
    pyramid_file_dir = config.PROJECT_DIR + '/video/pyramid'
    pyramid_file_path = pyramid_file_dir + '/pyramid.json'
    try:
        pyramid_file = open(pyramid_file_path, 'r')

    except Exception as e:
        logger.error(
            f'Unable to write {pyramid_file_path} exception={type(e).__name__}')
        quit(-1)

    # read the json
    s = pyramid_file.read()
    pyramid = json.loads(s)

    # close file
    pyramid_file.close()

    return pyramid


def dimensions(video_file_path):
    probe = ffmpeg.probe(video_file_path)
    probe_video = next(
        (stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    width = int(probe_video['width'])
    height = int(probe_video['height'])
    return (width, height)


def create_pyramid_level(video_file_path, audio_file_path, dimension, i, n):

    level_name = f'level_{str(i).zfill(3)}'
    output_dir = config.PROJECT_DIR + '/video/pyramid/' + level_name

    '''
    crop dimensions are out_w:out_h:x:y
        out_w is the width of the output rectangle
        out_h is the height of the output rectangle
        x and y specify the top left corner of the output rectangle
        coordinates start at (0,0) in the top left corner
    '''
    video_width, video_height = dimension
    width = video_width // n
    height = video_height // n

    video_file = ffmpeg.input(video_file_path)

    level_data = []

    for r in range(n):
        level_row = []
        for c in range(n):
            # calculate dimensions
            x = width*r
            y = height*c
            x_name = f'x_{str(x).zfill(3)}'
            y_name = f'y_{str(y).zfill(3)}'
            width_name = f'width_{str(width).zfill(3)}'
            height_name = f'height_{str(height).zfill(3)}'
            output_file_name = f'{x_name}_{y_name}_{
                width_name}_{height_name}.mp4'
            output_file_path = output_dir + '/' + output_file_name
            crop_dimensions = f'{width}:{height}:{x}:{y}'

            # if needed, create dir
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            # crop and write the video, if it doesnt exist already
            if not os.path.exists(output_file_path):
                logger.info(f'writing pyramid video {output_file_path}')
                (
                    ffmpeg
                    # crop
                    .filter(video_file, 'crop', *crop_dimensions.split(':'))
                    # output the file
                    .output(output_file_path, loglevel='quiet')
                    .run(overwrite_output=True)
                )
            else:
                logger.info(f'pyramid video already exists {output_file_path}')
            # add to level data
            level_row.append({
                'row': r,
                'column': c,
                'color_tint': [None, None, None],
                'crop_dimension': {
                    'x': x,
                    'y': y,
                    'width': width,
                    'height': height
                },
            })
        level_data.append(level_row)

    return level_data
