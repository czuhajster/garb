from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='garb',
    version='0.2.1',
    description='Request Builder for Google Analytics Reporting API v4 ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/czuhajster/garb',
    author='Arkadiusz Podkowa',
    author_email='18arek@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ],
    keywords='google analytics',
    project_url={
        'Tracker': 'https://github.com/czuhajster/garb/issues'
    },
    packages=find_packages(include=['garb', 'garb.*']),
    python_requires='>=3.9'
)

