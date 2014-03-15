from qbittorrent import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='qbittorrent-python',
    version=__version__,
    packages=['qbittorrent'],
    url='https://github.com/fuzeman/qbittorrent-python',
    license='',
    author='Dean Gardiner',
    author_email='me@dgardiner.net',
    description=''
)
