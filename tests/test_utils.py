import pytest
import sass

import flit_sass.utils


def test_compile_sass(capsys, package):
    scss_file = package / "package/static/sass/styles.scss"
    scss_file.parent.mkdir(parents=True)
    scss_file.write_text(
        r"""
        $color: #abc;
        body {
            color: $color;
        }
        """
    )

    flit_sass.utils.compile_sass()

    assert (package / "package/static/css/styles.css").exists()
    captured = capsys.readouterr()
    assert captured.out == "\x1b[1m* Compiling Sass/SCSS files...\x1b[0m\n"
    assert captured.err == ""


def test_compile_sass__invalid(capsys, package):
    scss_file = package / "package/static/sass/styles.scss"
    scss_file.parent.mkdir(parents=True)
    scss_file.write_text(
        r"""
        body {
            color: $var-does-not-exist;
        }
        """
    )

    with pytest.raises(sass.CompileError):
        flit_sass.utils.compile_sass()
