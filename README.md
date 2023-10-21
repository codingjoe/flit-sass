# Flit Sass

[![PyPi Version](https://img.shields.io/pypi/v/flit-sass.svg)](https://pypi.python.org/pypi/flit-sass/)
[![Test Coverage](https://codecov.io/gh/codingjoe/flit-sass/branch/main/graph/badge.svg)](https://codecov.io/gh/codingjoe/flit-sass)
[![GitHub License](https://img.shields.io/github/license/codingjoe/flit-sass)](https://raw.githubusercontent.com/codingjoe/flit-sass/main/LICENSE)

Compile Sass/SCSS files to CSS during build time.

_"Binary files should never be committed to a repository to promote transparency and security."_
That is why this project was created.

### Usage

Simple, just add `flit-sass` to your `pyproject.toml`
build-system requirements and set the `build-backend`:

```toml
# pyproject.toml
[build-system]
requires = [
  "flit-sass[scm]",  # [scm] is optional
  # …others, like wheel, etc.
]
# using flit-core as a base build-backend
build-backend = "flit_sass.core"
# or using flit-scm as a base build-backend for git-based versioning
build-backend = "flit_sass.scm"
# To use use flit-scm, you will need to include the optional dependency above.

[tool.flit_sass]
dirs = { "package/static/scss" = "package/static/css" }
output_style = "compressed"  # optional: nested, expanded, compact, compressed
```

If you ship wheels, those will include the compiled `.css` files.

**That's it!**
