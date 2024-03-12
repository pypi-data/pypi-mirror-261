from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='sqla-connector',
    version='0.0.1',
    license='MIT License',
    author='Mariano Tupã',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='marianotupa@gmail.com',
    keywords='sqlalchemy database',
    description=u'Melhora o acessibilidade ao sqla-connector',
    packages=['sqla_connector'],
    install_requires=['sqlalchemy'],)