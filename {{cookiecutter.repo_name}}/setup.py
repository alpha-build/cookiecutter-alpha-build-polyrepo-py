from pathlib import Path

from setuptools import setup

LIB_ROOT = Path(__file__).parent
REQS_FILE = LIB_ROOT / 'requirements.txt'
README_FILE = LIB_ROOT / 'README.md'


def main() -> None:
    setup(
        name='py_utils',
        version='0.1',
        packages=['{{cookiecutter.repo_name}}'],
        python_requires='>=3.8',
        install_requires=REQS_FILE.read_text(),
        zip_safe=False,  # for mypy
        package_data={'': ['py.typed']},  # expose types to users  # TODO
        author='{{cookiecutter.author}}',
        author_email='{{cookiecutter.email}}',
        description='',
        long_description=README_FILE.read_text(),
    )


if __name__ == '__main__':
    main()
