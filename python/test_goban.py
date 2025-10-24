from goban import Goban


def test_white_is_taken_when_surrounded_by_black() -> None:
    goban = Goban([
        '.#.',
        '#o#',
        '.#.',
    ])

    assert goban.is_taken(1, 1) is True


def test_white_is_not_taken_when_it_has_a_liberty() -> None:
    goban = Goban([
        '...',
        '#o#',
        '.#.',
    ])

    assert goban.is_taken(1, 1) is False


def test_black_shape_is_taken_when_surrounded() -> None:
    goban = Goban([
        'oo.',
        '##o',
        'o#o',
        '.o.',
    ])

    assert goban.is_taken(0, 1) is True
    assert goban.is_taken(1, 1) is True
    assert goban.is_taken(1, 2) is True


def test_black_shape_is_not_taken_when_it_has_a_liberty() -> None:
    goban = Goban([
        'oo.',
        '##.',
        'o#o',
        '.o.',
    ])

    assert goban.is_taken(0, 1) is False
    assert goban.is_taken(1, 1) is False
    assert goban.is_taken(1, 2) is False


def test_square_shape_is_taken() -> None:
    goban = Goban([
        'oo.',
        '##o',
        '##o',
        'oo.',
    ])

    assert goban.is_taken(0, 1) is True
    assert goban.is_taken(0, 2) is True
    assert goban.is_taken(1, 1) is True
    assert goban.is_taken(1, 2) is True
