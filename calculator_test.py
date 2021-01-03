import pytest

@pytest.mark.parametrize(
    'x,result',
    [
        (3, 9),
        (4,16),
        (5,25),
        (100,1000),
        (15, 225)
    ]
)
def test_square(calc, x, result):
    assert calc.square(x) == result


@pytest.mark.parametrize(
    'x,y, result',
    [
        (8, 9, 8),
        (5,16, 5),
        (7,16,7),
        (90,3,0),
        (15,2,1)
    ]
)
def test_division(calc, x, y, result):
    assert calc.division(x, y) == result


@pytest.mark.parametrize(
    'x,y,result',
    [
        (24, 36, 12),
        (12, 78, 6),
        (15, 30, 15),
        (9, 15, 3),
        (100, 13, 1)

    ]
)
def test_nwd(calc, x, y, result):
    assert calc.nwd(x, y) == result