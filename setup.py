from setuptools import setup, find_packages

HYPHEN_DOT_E = "-e ."
def get_requirements():
    with open('requirements.txt', 'r') as f:
        lines = f.read().splitlines()
        if HYPHEN_DOT_E in lines:
            lines.remove(HYPHEN_DOT_E)
        return lines

setup(
    name='networksecurity',
    version='0.1',
    author='muzmmil pathan',
    packages=find_packages(),
    install_requires=get_requirements(),
)