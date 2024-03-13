#! /usr/bin/env python3
import os
from pathlib import Path

from ratisbona_project_starter.licenses import _gplv2
from ratisbona_project_starter.templates import _gitignore


def writefile(name, content):
    print('writefile', name)
    with open(name, 'w') as file:
        file.write(content)


def makedirs(path):
    print('makedirs', path)
    os.makedirs(path, exist_ok=True)
    return path


def makeinit(path, content='# empty intentionally'):
    writefile(path / '__init__.py', content)


def create_package_strut(projectname):
    """
    Creates a package structure according to packaging.python.org
    Parameters
    ----------
    projectname - the project name

    Returns
    -------
    Nothing
    """

    # make project directory
    base_dir = Path('.')
    project_dir = makedirs(base_dir / projectname)
    writefile(project_dir / 'pyproject.toml',f'''\
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{projectname}"
version = "0.0.1"
authors = [
  {{ name="Example Author", email="author@example.com" }},
]
description = "A small example package"
readme = "README.md"
requires-python = ">=3.10"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    "Operating System :: OS Independent",
]
dependencies = [
    "typer",
]
[project.scripts]
{projectname}= "{projectname}.__main__:main"

[project.optional-dependencies]
dev = [
    "pylint",
    # Code style
    "black[d]",
    # Strict typing
    "mypy",
    # Test coverage
    "coverage",
]


[project.urls]
"Homepage" = "https://github.com/pypa/sampleproject"
"Bug Tracker" = "https://github.com/pypa/sampleproject/issues"


[tool.hatch.build.targets.wheel]
packages = ["src/{projectname}"]
''')
    writefile(project_dir / 'LICENSE', _gplv2.content())
    writefile(project_dir / 'README.md', '''\
# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Project-structure, Installing Dependencies and PYTHONPATH configuration.

This Project houses it's sources below the `src/{projectname}` directory. You have
to have this directory in your module-searchpath to execute the project. It should also
be present in the module-searchpath of your IDE.

If using pycharm or any other Jetbrains-based IDE, use 
`Settings->Project->Project Structure`
to `mark as sourcefolder` the `src`-folder of this.

The Project requirements, as well as the dev-requirements are intended to be listed in the 
`pyproject.toml`-file (see there)

By issuing:

```shell
pip install -e .
```

you add all the project dependencies as well as the projects sourcefolder to your 
[hopefully virtual!] environment, relieving you of the burden of having to manually 
installing anything or having to configure your python path by other means.

Likewise you can install all the dev-dependencies by:

```shell
pip install -e .'[dev]'
```

''')
    writefile(project_dir / '.gitignore', _gitignore.content())

    # make src folder
    src_dir = makedirs(project_dir / 'src')

    package_dir = makedirs(src_dir / projectname)
    makeinit(package_dir, f'''\
__app_name__ = "{projectname}"
__version__ = "0.0.1"
''')
    writefile(package_dir / 'example.py', f'''\
#! /usr/bin/env python3

def greet():
    print('Friendly Greetings from your pythonproject: {projectname}')

if __name__ == '__main__':
    greet()

''')
    writefile(package_dir / '__main__.py',f'''\
import typer
from {projectname}.example import greet

def main():
    typer.run(greet)

if __name__ == "__main__":
    main()
''')

    # make tests directory
    tests_dir = makedirs(project_dir / 'tests')
    makeinit(tests_dir)
    writefile(tests_dir / 'test_example.py', '''\
import unittest


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

if __name__ == '__main__':
    unittest.main()
''')

    # make data folder
    data_dir = makedirs(project_dir / 'data')
    writefile(data_dir / 'README.md', 'Your data goes here.')

    # make docs directory
    docs_dir = makedirs(project_dir / 'docs')
    
    docs_src_dir = makedirs(docs_dir / 'source')

    # make notebooks directory
    notebooks_dir = makedirs(project_dir / 'notebooks')
    writefile(notebooks_dir / 'README.md', 'Your notebooks go here.')

