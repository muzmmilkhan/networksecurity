from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt', 'r') as f:
        return f.read().splitlines()
    
setup(
    name='networksecurity',
    version='0.1',
    author='muzmmil pathan',
    packages=find_packages(),
    install_requires=read_requirements(),
)