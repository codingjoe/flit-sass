import os
import subprocess  # nosec
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def test_build_sdist(package):
    """Test that build_sdist() compiles Sass files."""
    # Create a dummy SCSS file
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

    output = subprocess.check_output(
        [sys.executable, "-m", "build", "--sdist"],
        cwd=package,
        env={**os.environ, "PYTHONPATH": f".:{ROOT}"},
    )

    # Check that the Sass compilation was logged
    assert b"* Compiling Sass/CSSS files..." not in output


def test_build_wheel(package):
    """Test that build_wheel() compiles Sass files."""
    # Create a dummy SCSS file
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

    output = subprocess.check_output(
        [sys.executable, "-m", "build", "--wheel"],
        cwd=package,
        env={**os.environ, "PYTHONPATH": f".:{ROOT}"},
    )

    # Check that the Sass compilation was logged
    assert b"* Compiling Sass/SCSS files..." in output


def test_editable_editable(package):
    """Test that build_editable() compiles Sass files."""
    # Create a dummy SCSS file
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

    packages_dir = package / "packages"
    packages_dir.mkdir(parents=True)

    output = subprocess.check_output(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--target",
            str(packages_dir),
            "-v",
            "-e",
            ".",
        ],
        cwd=package,
        env={**os.environ, "PYTHONPATH": f".:{ROOT}", "PEP517_BACKEND_PATH": str(ROOT)},
        stderr=subprocess.STDOUT,
    )

    # Check that the Sass compilation was logged
    assert b"* Compiling Sass/SCSS files..." in output
