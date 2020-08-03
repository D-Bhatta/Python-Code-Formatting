""" Tests for 'code_fmt' package """
import pytest

from code_fmt import code_fmt


def test_helloworld(capsys):
    """ Correct object argument prints """
    code_fmt.helloworld("cat")
    captured = capsys.readouterr()
    assert "cat" in captured.out


def test_helloworld_exception():
    with pytest.raises(TypeError):
        code_fmt.helloworld(1)
