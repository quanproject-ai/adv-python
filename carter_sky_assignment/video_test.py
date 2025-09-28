import video


def test_end_reached_cb():
    params = {
        'finish': False
    }
    video.end_reached_cb(None, params)
    assert params['finish']


def test_ms_to_time():
    t = video.ms_to_time(70000)
    assert t == '01:10'


def test_clean_temp_directory():
    video.clean_temp_directory()
