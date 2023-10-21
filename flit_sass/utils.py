try:
    import tomllib
except ImportError:
    import tomli as tomllib

import sass


def compile_sass():
    """Compile Sass/SCSS files."""
    try:
        with open("pyproject.toml", "rb") as f:
            pyproject = tomllib.load(f)
    except OSError:
        pass  # Do nothing if unable to access `pyproject.toml`
    else:
        try:
            config = pyproject["tool"]["flit-sass"]
        except KeyError:
            pass  # Do nothing if `setuptools_scm` is not configured in `pyproject.toml`
        else:
            print("\33[1m* Compiling Sass/SCSS files...\33[0m")
            for dirname in config.get("dirs", {}).items():
                sass.compile(
                    dirname=dirname,
                    output_style=config.get("output_style", "compressed"),
                )
