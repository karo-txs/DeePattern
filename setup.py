from setuptools import setup, find_packages

setup(
    name='deepattern',
    version='0.1.0',
    author='Karolayne Teixeira',
    author_email='karo.txs@gmail.com',
    description='Deep Learning Project Patterns',
    package_dir={"": "src"}, 
    packages=find_packages(where="src"),
    install_requires=["toml"],
)
