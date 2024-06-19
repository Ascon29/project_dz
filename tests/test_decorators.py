from src.decorators import log


@log()
def func_1(a, b):
    return a / b


def test_func(capsys):
    result = func_1(2, 1)
    captured = capsys.readouterr()
    assert captured.out == "func_1 ok\n"
    assert result == 2


def test_func_err(capsys):
    func_1(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "func_1 error: division by zero. Inputs: (2, 0), {}\n"


@log(filename="log.txt")
def func_2(a, b):
    return a / b


def test_func_err2(filename="log.txt"):
    func_2(2, 0)
    with open(filename, "r") as f:
        result = f.read()
        assert result == "func_2 error: division by zero. Inputs: (2, 0), {}\n"


def test_func_ok(filename="log.txt"):
    func_2(2, 1)
    with open(filename, "r") as f:
        result = f.read()
        assert result == "func_2 ok\n"
