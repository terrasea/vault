#!/usr/bin/env python

import getpass
import keyring


def set(service, key, value):
    """ Adds (key, value) to service.
    """

    return keyring.set_password(service, key, value)


def ask(service, key):
    """ Prompts the user for the value of key for the service and returns it.
    """

    prompt = "Enter the value associated with {key} for {service} : "
    prompt = prompt.format(service=service, key=key)

    return getpass.getpass(prompt)


def get(service, key, read_only=False):
    """ Returns the value associated with key for the service.
    If the value is not found, prompts the user for the value, saves it and returns it.
    If the value is not found and read_only is True, returns None.
    """

    value = keyring.get_password(service, key)

    if value is None and not read_only:
        value = ask(service, key)
        set(service, key, value)

    # If running via command line, print it.
    if __name__ == '__main__' and value:
        print(value)

    return value


if __name__ == '__main__':
    import scriptine
    get_command = get
    set_command = set
    scriptine.run()
