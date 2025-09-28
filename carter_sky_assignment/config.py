import logging

#
# STUDENTS NEED TO CHANGE THE PROJECT DIRECTORY FOR THEIR COMPUTER
#
# project directory
PROJECT_DIR = "~/Code/Github/adv-python/carter_sky_assignment"

# temporary directory for videos
TEMP_DIR = PROJECT_DIR + "/temp"

# url
URL = "https://www.youtube.com/watch?v=WU4UxWaf8U8&list=PLIx-eqjsmIuCoHbep0iithAFB6U793VVA"

# source hires files
SOURCE_VIDEO_BASENAME = "carter-skyers-easiest-goodbye-official-music-video"
SOURCE_VIDEO_FILE_PATH = PROJECT_DIR + "/video/" + SOURCE_VIDEO_BASENAME + ".mp4"
SOURCE_AUDIO_FILE_PATH = PROJECT_DIR + "/video/" + SOURCE_VIDEO_BASENAME + ".mp3"

# configure log output format
FORMAT = "[%(asctime)s:%(levelname)-8s] %(message)s"
logging.basicConfig(format=FORMAT)

# get logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
