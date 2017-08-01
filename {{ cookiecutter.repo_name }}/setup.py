from setuptools import setup, find_packages

setup(
    name='{{ cookiecutter.project_name }}',
    version='0.1.0',
    description='{{ cookiecutter.project_short_description }}',
    url='{{ cookiecutter.url }}',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
