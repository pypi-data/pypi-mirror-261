from pathlib import Path

import numpy as np

import sfio.dataurl

cases = [
    np.inf,
    None,
    {1: 2, 3: 4}.keys(),
    Path('/home/henry/a'),
    [[1, 2, 3, [3, 'd', slice(1, 6, 3)]], [4, 5, 6]],
    tuple([slice(1, 6, 3), [set(['s', 4, 7.8]), 2], 's']),
    tuple([1, 2, 3]),
    b'a',
    set([1, 2, 3]),
    np.array([[1 + 2j, 2, 3.4, 5], [1, 2, 3, 4]]),
    {
        1: slice(1, 6, 3),
        2: [
            set(['s', (4, 'a'), 7.8]),
            [
                [True, False, None],
                2,
                (Path('/home/test/a'), 2),
                np.array([[1 + 2j, 2, 3.4, 5], [1, 2, 3, 4]]),
            ],
            b'6',
            'data:python/slice,[1,6,3]',
        ],
    },
]


# ----------------------------------


def I(b):
    return b


def byte_to_str(b):
    return b.decode()


# convert type before comparing
cvt = {
    'dict_keys': list,
    'bytes': byte_to_str,
}


# ----------------------------------


def compare1(a, b):
    return a == b


def compare2(a, b):
    return a is b


def compare3(a, b):
    return np.array_equal(a, b)


# method of comparison
checks = {
    'NoneType': compare2,
    'ndarray': compare3,
}

# ----------------------------------


def test_encode_then_decode():
    for case in cases:
        datastr = sfio.dataurl.encode(case)
        decoded = sfio.dataurl.decode(datastr)

        typ = type(case).__name__

        check = checks.get(typ, compare1)
        target = cvt.get(typ, I)(case)

        assert check(target, decoded)
