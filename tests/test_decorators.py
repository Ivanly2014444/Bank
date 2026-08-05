import pytest

from src.decorators import log


def test_log(capsys):
    """Тестирование успешного выполнения функции с выводом лога в консоль."""

    @log()
    def dec_func(a, b):
        return a * b

    result = dec_func(1, 2)
    captured = capsys.readouterr().out.strip()

    assert result == 2
    assert captured == "dec_func ok"


def test_log_error(capsys):
    """Тестирование логирования исключений при выводе в консоль"""

    @log()
    def dec_func_err(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        dec_func_err(5, 0)

    captured_error = capsys.readouterr().out.strip()

    assert captured_error == "dec_func_err error: ZeroDivisionError. Inputs: (5, 0), {}"


def test_log_to_file(tmp_path):
    """Тестирование успешного выполнения функции с записью лога в файл"""
    log_file = tmp_path / "test_dec.txt"

    @log(filename=str(log_file))
    def txt_func(a, b):
        return a + b

    txt_func(4, 5)

    assert log_file.exists()

    read_file = log_file.read_text(encoding="utf-8").strip()

    assert read_file == "txt_func ok"


def test_log_100_coverage(tmp_path):
    """Тестирование логирования исключений с записью лога в файл"""
    logg_file = tmp_path / "test_dec_second.txt"

    @log(filename=str(logg_file))
    def txt_func_(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):

        txt_func_(4, 0)

    assert logg_file.exists()

    read_file_ = logg_file.read_text(encoding="utf-8").strip()
    assert read_file_ == "txt_func_ error: ZeroDivisionError. Inputs: (4, 0), {}"
