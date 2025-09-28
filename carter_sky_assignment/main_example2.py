import os

import config
import video


def main():
    '''
    this example tints a level 2 square yellow color, then put it into position over level 1, and plays the video
    '''

    # clean temp video directory
    video.clean_temp_directory()

    # tint yellow square
    level1_file_path = config.PROJECT_DIR + \
        '/video/pyramid/level_001/x_000_y_180_width_320_height_180.mp4'
    name = 'yellow'
    r, g, b = 255, 255, 0
    level1_tint = video.color_tint(name, level1_file_path, r, g, b)

    # level1 square over video, panned the square into it's proper position
    level0_file_path = config.PROJECT_DIR + \
        '/video/pyramid/level_000/x_000_y_000_width_640_height_360.mp4'
    name = 'level1_over'
    x = 0
    y = 180
    level1_over_level0 = video.over(
        name, level1_tint, level0_file_path, x, y)

    # add audio back into file
    name = 'result'
    result_video_with_audio = video.audio(name, level1_over_level0,
                                          config.SOURCE_AUDIO_FILE_PATH)

    # clean up and delete any intermediate files
    for f in (level1_tint, level1_over_level0):
        if os.path.exists(f):
            os.remove(f)

    # play video
    print(f'playing {result_video_with_audio}')
    video.play(result_video_with_audio)


main()
