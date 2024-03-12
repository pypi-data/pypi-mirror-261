import toml


def get_version():
    try:
        pyproject = toml.load('../pyproject.toml')
        return pyproject['tool']['poetry']['version']
    except Exception as e:
        return "Unknown version"


__version__ = get_version()
