import hashlib
import os
import platform
import sys
import time
from os.path import isfile, join

import config
import ffmpeg
import vlc
from config import logger


def end_reached_cb(event, params):
    logger.info("video end reached")
    params['finish'] = True


def ms_to_time(total_ms):
    total_sec = total_ms / 1000
    min = total_sec // 60
    sec = total_sec % 60
    t = '%02d:%02d' % (min, sec)
    return t


def position_changed_cb(event, player):
    npos = event.u.new_position * 100
    time_ms = player.get_time()
    ms = ms_to_time(time_ms)
    sys.stdout.write('\r%s %s (%.2f%%)' % ('Position', ms, npos))
    sys.stdout.flush()


def write_audio(audio_file_path, input_file):
    (
        ffmpeg
        .output(input_file, audio_file_path, loglevel='quiet')
        .run(overwrite_output=True)
    )


def shake256_hash(s):
    m = hashlib.shake_256()
    m.update(str.encode(s))
    hash = m.hexdigest(8)
    return hash


def temp_file_path(name, ext):
    '''
    creates a valid path to a temp file
    '''
    if not os.path.exists(config.TEMP_DIR):
        os.makedirs(config.TEMP_DIR)
    hash = shake256_hash(name + str(time.time_ns()))
    temp_file_name = 'temp_' + name + '_' + hash + ext
    temp_file_path = config.TEMP_DIR + '/' + temp_file_name
    return temp_file_path


def color_tint(name, input_file_path, r, g, b):
    '''
    tints a input video and returns it's output
    '''
    # if color is none, return
    if r is None and g is None and b is None:
        print('\tNo color tint to apply')
        return input_file_path

    # check and calculate rgb values
    is_rgb = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
    if not is_rgb:
        print(f'ERROR: {r},{g},{b} is not a valid 0-255 rgb value')
        quit(-1)
    r = float(r/255)
    g = float(g/255)
    b = float(b/255)

    print('Applying color_tint...')
    print(f'\tinput file : {os.path.basename(input_file_path)}')
    print(f'\tname       : {name}')
    print(f'\tr,g,b      : {r},{g},{b}')
    print('\tstatus     : processing...', end='')
    input_file = ffmpeg.input(input_file_path)
    output_file = temp_file_path(name, '.mp4')

    # process
    # colorchannelmixer=rr:rg:rb:ra:gr:gg:gb:ga:br:bg:bb:ba:ar:ag:ab:aa
    mix = f'{r}:0:0:0:' + f'{g}:{g}:{g}:0:' + f'{b}:{b}:{b}:0:' + '0:0:0:1'
    (
        ffmpeg
        .filter(input_file, 'colorchannelmixer', *mix.split(':'))
        .output(output_file, loglevel='quiet')
        .run()
    )

    print('done')
    print(f'\toutput file: {os.path.basename(output_file)}')
    return output_file


def over(name, input_file_path_a, input_file_path_b, x, y):
    '''
    puts video a over video b
    '''
    if x < 0 or y < 0:
        print(f'ERROR: {x},{y} is invalid. x and y must be non-negative')
        quit(-1)

    print('Applying over...')
    print(f'\tinput file a: {os.path.basename(input_file_path_a)}')
    print(f'\tinput file b: {os.path.basename(input_file_path_b)}')
    print(f'\tname       : {name}')
    print('\tstatus     : processing...', end='')
    input_file_a = ffmpeg.input(input_file_path_a)
    input_file_b = ffmpeg.input(input_file_path_b)
    output_file = temp_file_path(name, '.mp4')

    # process
    (
        ffmpeg
        .overlay(input_file_b, input_file_a, x=x, y=y)
        .output(output_file, loglevel='quiet')
        .run()
    )

    print('done')
    print(f'\toutput file: {os.path.basename(output_file)}')
    return output_file


def audio(name, input_video_file_path, input_audio_file_path):
    '''
    adds audio back into file
    '''
    print('Applying audio...')
    print(f'\tinput video file : {os.path.basename(input_video_file_path)}')
    print(f'\tinput audio file : {os.path.basename(input_audio_file_path)}')
    print(f'\tname       : {name}')
    print('\tstatus      : processing...', end='')
    video_file = ffmpeg.input(input_video_file_path)
    audio_file = ffmpeg.input(input_audio_file_path)
    output_file = temp_file_path(name, '.mp4')

    # process
    (
        ffmpeg
        # add audio back in to video
        .concat(video_file, audio_file, v=1, a=1)
        .output(output_file, loglevel='quiet')
        .run()
    )

    print('done')
    print(f'\toutput file: {os.path.basename(output_file)}')
    return output_file


def play(file_path):

    # creating a vlc instance
    vlc_instance = vlc.Instance()

    # creating a media player
    player = vlc_instance.media_player_new()

    # creating a media, prepend C: if on windows
    if platform.system() == 'Windows':
        file_path = 'C:' + file_path
    media = vlc_instance.media_new(file_path)

    # setting media to the player
    player.set_media(media)

    params = {
        'finish': False
    }

    # callbacks
    events = player.event_manager()
    events.event_attach(vlc.EventType.MediaPlayerEndReached,
                        end_reached_cb, params)
    events.event_attach(
        vlc.EventType.MediaPlayerPositionChanged, position_changed_cb, player)

    # play until finished
    player.play()
    while not params['finish']:
        time.sleep(0.5)

    # getting the duration of the video
    duration = player.get_length()

    # printing the duration of the video
    logger.info("Duration : " + ms_to_time(str(duration)))


def clean_temp_directory():

    for temp_file in os.listdir(config.TEMP_DIR):
        if isfile(join(config.TEMP_DIR, temp_file)):
            os.remove(config.TEMP_DIR + '/' + temp_file)
