from src.loop import loop_over

from .utilities import assert_loop_raises, assert_loops_as_expected


def test_empty():
    def raise_error(x):
        raise RuntimeError

    for _ in loop_over([]).map(raise_error):
        assert False


def test_plus_one():
    inp = [1, 2, 3, 4, 5, 6, 7, 8]
    out = [x + 1 for x in inp]
    loop = loop_over(inp).map(lambda x: x + 1)
    assert_loops_as_expected(loop, out)


def test_times_two_plus_one():
    inp = [1, 2, 3, 4, 5, 6, 7, 8]
    out = [(2 * x) + 1 for x in inp]
    loop = loop_over(inp).map(lambda x: 2*x).map(lambda x: x + 1)
    assert_loops_as_expected(loop, out)


def test_plus_one_times_two():
    inp = [1, 2, 3, 4, 5, 6, 7, 8]
    out = [(x + 1) * 2 for x in inp]
    loop = loop_over(inp).map(lambda x: x + 1).map(lambda x: 2*x)
    assert_loops_as_expected(loop, out)


def test_args_kwargs_values():
    args = (1, 'a', False)
    kwargs = {'a': [], 'b': {}, 'c': None}

    def function(x, *args_, **kwargs_):
        assert args_ == args
        assert kwargs_ == kwargs
        return x

    inp = range(10)
    out = range(10)
    loop = loop_over(inp).map(function, *args, **kwargs)
    assert_loops_as_expected(loop, out)


def test_type_error():
    inp = range(10)
    loop = loop_over(inp).map('not a function')
    assert_loop_raises(loop, TypeError)


def test_error_in_function():
    def raise_error(x):
        raise RuntimeError

    inp = range(10)
    loop = loop_over(inp).map(raise_error)
    assert_loop_raises(loop, RuntimeError)


def test_wrong_signature():
    def takes_two(one, two):
        return one

    inp = range(10)
    loop = loop_over(inp).map(takes_two)
    assert_loop_raises(loop, TypeError)


def test_unpack():
    inp = [[1,2], [4,7], [9,15], [6,6]]
    out = [x[0] + x[1] for x in inp]
    loop = loop_over(inp).next_call_with(unpacking='*').map(lambda x, y: x + y)
    assert_loops_as_expected(loop, out)


def test_not_unpackable():
    inp = range(10)
    loop = loop_over(inp).next_call_with(unpacking='*').map(lambda x: x)
    assert_loop_raises(loop, TypeError)


def test_side_effects():
    inp = range(10)
    out = []

    for _ in loop_over(inp).map(out.append):
        pass

    assert out == list(inp)


def test_combo():
    inp = [1, 2, 3, 4, 5, 6, 7, 8]
    out = [((x - 1/x) ** 2, x) for x in inp]
    loop = loop_over(inp).map(lambda x: (x, 1/x)).next_call_with(unpacking='*').map(lambda x, y: ((x - y) ** 2, x))
    assert_loops_as_expected(loop, out)


def test_dict_unpack():
    def aspect_ratio(*, height, width):
        return width / height
    
    inp = [{'height': 1080, 'width': 1920}, {'width': 640, 'height': 480}]
    out = [1920/1080, 640/480]
    loop = loop_over(inp).next_call_with(unpacking='**').map(aspect_ratio)
    assert_loops_as_expected(loop, out)


def test_args_first():
    from math import pow

    inp = range(10)
    out = [2 ** x for x in range(10)]
    loop = loop_over(inp).next_call_with(args_first=True).map(pow, 2)
    assert_loops_as_expected(loop, out)
