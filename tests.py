from . import vault

service = 'service_from_vault_test_suite'
key = 'test_key'
value1 = 'some_secret_info'
value2 = 'some_new_secret_info'


def test_new():
    """ Test that we can create a new key-value pair
    """

    vault.set(service, key, value1)
    assert vault.get(service, key) == value1


def test_empty():
    """ Test that read_only attr does not create a new key-value pair
    """

    assert vault.get(service, 'some_junk_key', read_only=True) == None


def test_change():
    """ Test that we can change an existing key
    """
    vault.set(service, key, value1)
    vault.set(service, key, value2)
    assert vault.get(service, key) == value2
