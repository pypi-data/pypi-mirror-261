try:
    import tomllib
except ImportError:
    import tomli as tomllib


def get_version():
    try:
        with open('../pyproject.toml', "rb") as f:
            pyproject = tomllib.load()
            return pyproject['tool']['poetry']['version']
    except Exception as e:
        return "Unknown version"


__version__ = get_version()
