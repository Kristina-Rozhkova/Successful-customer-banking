from src.decorators import log


def test_log_success(capsys):
    @log()
    def my_function(a, b):
        return a + b

    my_function(1, 10)

    captured = capsys.readouterr()
    assert "The result of working my_function: 11" in captured.out
    assert "Time for working:" in captured.out


def test_log_error(capsys):
    @log()
    def my_function(a, b):
        return a + b

    my_function("1", 10)

    captured = capsys.readouterr()
    assert "my_function fell down with the error" in captured.out
    assert "The arguments of function was ('1', 10), {}" in captured.out
