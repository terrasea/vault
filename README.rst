Vault
=============================

What is it?
-----------------------------------------

Use case
^^^^^^^^^^
It's a common requirement for shell scripts and python programs to store third-party passwords (SMTP passwords, secret API keys etc) and use them later. Where do you save them?

Solutions and Pitfalls
^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Many people save this sensitive information as environment variables, because it is the most straightforward method. But it has serious security implications, particularly on shared hosting servers (That's why I don't like shared hosting. I wonder why people still use shared hosting when VPS is so cheap. For example, you can get a 256MB VPS slice from Rackspace Cloud for as cheap as $11 per month).
* Another approach recommended by several people is to store the passwords in a text file, remove read permissions for all others except the owner and read that file from your program at runtime to retrieve the passwords. But it too has security issues. What if you forgot to exclude this file from your VCS or from your backups?

My Solution
^^^^^^^^^^^^^
* My solution is a light wrapper around the excellent python-keyring_ library. Keyring allows us to store sensitive information in GnomeKeyring (for Gnome environments) or KDEWallet (for KDE environments) or Win32CryptoRegistry (for Windows). Vault makes it a little more convenient to use it in shell scripts.

.. _python-keyring: http://bitbucket.org/kang/python-keyring-lib/


How to use it?
-----------------------------------------

Python Programs
^^^^^^^^^^^^^^^^^^
* Just call ::

    vault.get(service, key)

* If the (key, value) pair for the service exists already, it simply returns the value.
* Otherwise it will prompt the user for the value and saves it.
* If you have to change the value of the key in future, simply call ::

    vault.set(service, key, new_value)

Shell Scripts
^^^^^^^^^^^^^^^^^^
* To get the password for testuser@gmail.com ::

    password=`python -m vault get gmail.com testuser`

* If the password is not found, it will prompt the user, saves it and populates password.
* To change the value of the key in future ::

    python -m vault set gmail.com testuser new_password

Latest Version
-----------------------------------------
The latest version of this project can be found at : http://bitbucket.org/sramana/vault


Documentation
-----------------------------------------
The documentation is distributed along with source repository in docs/ directory (in ReStructuredText format). You can run "make html" in that directory to generate HTML version.

Alternatively, you can browse the online documentation at http://packages.python.org/vault/


Installation
-----------------------------------------
* Run "pip install vault".
* Alternatively, if you have downloaded the source, run "python setup.py install" in the unzipped source directory.

Dependencies
-----------------------------------------
* python-keyring - http://pypi.python.org/pypi/keyring
* scriptine - http://pypi.python.org/pypi/scriptine

License
-----------------------------------------
This project is licensed under New BSD license.


Contribution and Feedback
-----------------------------------------
Contributions and Feedback are most welcome. Please email the author with your comments.


Author Information
-----------------------------------------
Ramana <sramana9@gmail.com>

* http://bitbucket.org/sramana
* http://github.com/sramana
