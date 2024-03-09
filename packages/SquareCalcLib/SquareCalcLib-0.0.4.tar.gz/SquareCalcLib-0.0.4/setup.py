from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='SquareCalcLib',
    version='0.0.4',
    author='Rzilla',
    author_email='pavel.eliseev.work@yandex.ru',
    description='A module for calculating the areas of an ellipse and a triangle.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/RdZilla/SquareCalcLib',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='square, triangle, ellipse, calcutation',
    project_urls={
        'GitHub': 'https://github.com/RdZilla/'
    },
    python_requires='>=3.10'
)
