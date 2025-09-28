#
# STUDENTS NEED TO ADD CODE HERE
# Students need to add code in this module and change any functions as needed.
#

import command

PYRAMID = [
    {
        "level": 0,
        "videos": [
            [
                {
                    "row": 0,
                    "column": 0,
                    "color_tint": [
                        None,
                        None,
                        None
                    ],
                    "crop_dimension": {
                        "x": 0,
                        "y": 0,
                        "width": 640,
                        "height": 360
                    }
                }
            ]
        ]
    },
    {
        "level": 1,
        "videos": [
            [
                {
                    "row": 0,
                    "column": 0,
                    "color_tint": [
                        None,
                        None,
                        None
                    ],
                    "crop_dimension": {
                        "x": 0,
                        "y": 0,
                        "width": 320,
                        "height": 180
                    }
                },
                {
                    "row": 0,
                    "column": 1,
                    "color_tint": [
                        None,
                        None,
                        None
                    ],
                    "crop_dimension": {
                        "x": 0,
                        "y": 180,
                        "width": 320,
                        "height": 180
                    }
                }
            ],
            [
                {
                    "row": 1,
                    "column": 0,
                    "color_tint": [
                        None,
                        None,
                        None
                    ],
                    "crop_dimension": {
                        "x": 320,
                        "y": 0,
                        "width": 320,
                        "height": 180
                    }
                },
                {
                    "row": 1,
                    "column": 1,
                    "color_tint": [
                        None,
                        None,
                        None
                    ],
                    "crop_dimension": {
                        "x": 320,
                        "y": 180,
                        "width": 320,
                        "height": 180
                    }
                }
            ]
        ]
    },
]

PYRAMID_ONE_LEVEL = [
    {
        "level": 0,
        "videos": [
            [
                {
                    "row": 0,
                    "column": 0,
                    "color_tint": [
                        None,
                        None,
                        None
                    ],
                    "crop_dimension": {
                        "x": 0,
                        "y": 0,
                        "width": 640,
                        "height": 360
                    }
                }
            ]
        ]
    },
]


def test_handle_print():
    command.handle_print(PYRAMID)
    assert True


def test_handle():
    command.handle(PYRAMID, 'p')
    command.handle(PYRAMID, 'bogus_command')
    assert True
