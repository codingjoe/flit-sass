import contextlib
import os
import tempfile
from pathlib import Path

import pytest


@pytest.fixture()
def package():
    with tempfile.TemporaryDirectory() as tmpdirname:
        temp_dir = Path(tmpdirname)
        pyproject_toml = temp_dir / "pyproject.toml"
        pyproject_toml.write_text(
            "[project]\n"
            'name = "package"\n'
            'version = "0.1.0"\n'
            'description = "A package"\n'
            "[build-system]\n"
            'requires = ["flit_core", "libsass"]\n'
            'build-backend = "flit_sass.core"\n'
            "[tool.flit-sass]\n"
            'dirs = { "package/static/sass" = "package/static/css" }\n'
        )
        (temp_dir / "package").mkdir(parents=True)
        (temp_dir / "package" / "__init__.py").touch()

        with chdir(temp_dir):
            yield temp_dir


@pytest.fixture()
def package_scm():
    with tempfile.TemporaryDirectory() as tmpdirname:
        temp_dir = Path(tmpdirname)
        pyproject_toml = temp_dir / "pyproject.toml"
        pyproject_toml.write_text(
            "[project]\n"
            'name = "package"\n'
            'description = "A package"\n'
            'dynamic = ["version"]\n'
            "[build-system]\n"
            'requires = ["flit_core", "libsass", "flit_scm"]\n'
            'build-backend = "flit_sass.scm"\n'
            "[tool.setuptools_scm]\n"
            'write_to = "package/_version.py"\n'
            'fallback_version = "0.1.0"\n'
            "[tool.flit-sass]\n"
            'dirs = { "package/static/sass" = "package/static/css" }\n'
            'output_style = "nested"\n'
        )
        (temp_dir / "package").mkdir(parents=True)
        (temp_dir / "package" / "__init__.py").touch()
        (temp_dir / "package" / "_version.py").write_text('version = "0.1.0"\n')

        with chdir(temp_dir):
            yield temp_dir


@contextlib.contextmanager
def chdir(path):
    """Context manager to temporarily change the working directory."""
    cwd = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cwd)
