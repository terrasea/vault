import fabric
from fabric.api import cd
import os

def local(cmd):
    fabric.api.local(cmd, capture=False)

def push():
    local("hg push")

def upload_docs_to_pypi():
    local("python setup.py build_sphinx")
    local("python setup.py upload_sphinx")

def upload_docs_github_pages():
    with cd('docs'):
        local('make html')

    with cd('docs/_build/html'):
        if not os.path.exists('.git'):
            local('git init')
            local('git symbolic-ref HEAD refs/heads/gh-pages')
            local('touch .nojekyll')

        local('git commit -a -m "Auto-commit from fabfile" || echo')
        local('git push -f git@github.com:sramana/vault.git gh-pages')

def docs():
    upload_docs_github_pages()
    upload_docs_to_pypi()


def sdist():
    local("cp README.rst README.txt")
    local("python setup.py sdist upload")
    local("rm README.txt")


def release():
    push()
    docs()
    sdist()
