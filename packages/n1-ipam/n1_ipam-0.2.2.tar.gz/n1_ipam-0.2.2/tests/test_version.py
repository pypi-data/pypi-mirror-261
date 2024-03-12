import tomllib

import n1.ipam as _ipam


def test_version():
    with open("pyproject.toml", "rb") as fp:
        proj = tomllib.load(fp)

    assert _ipam.__version__ == proj["project"]["version"]
