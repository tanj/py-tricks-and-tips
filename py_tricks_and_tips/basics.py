"basics.py is a collection of code to support basics.rst document"


def greet(name, greeting="Hi,"):
    return f"{greeting} {name}"


def greet_documented(name, greeting="Hi,"):
    """Greet `name` with `greeting`

    :param name: name of person we are greeting
    :param greeting: greeting we are using defaults to "Hi,"
    :returns: string of greeting and name

    """
    return f"{greeting} {name}"
