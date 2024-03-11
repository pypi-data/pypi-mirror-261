from setuptools import setup, find_packages

setup(
    name='keywads',
    version='0.1.1',
    author='Hashan Wickramasinghe',
    author_email='hashanwickramasinghe@gmail.com',
    description='A Python package for keyword analysis from Excel files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hashangit/keywads',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)