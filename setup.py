from setuptools import setup

project = 'vault'
version = 0.2

setup(name=project,
      version=version,
      description="A simple wrapper around python-keyring to store and retrieve sensitive information like passwords and API keys from Shell scripts and Python programs.",
      long_description=open('README.rst').read(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development',
      ],
      platforms='any',
      keywords='keyring passwords vault',
      author='Sramana',
      author_email='sramana9@gmail.com',
      url='http://bitbucket.org/sramana/vault',
      license='BSD',
      py_modules=['vault'],
      install_requires=['keyring', 'scriptine'],
      entry_points = {
          "distutils.commands": [
          "upload_sphinx = sphinx_pypi_upload:UploadDoc",
         ]
      }

     )
