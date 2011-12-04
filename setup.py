
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple project scaffolding for Python',
    'author': 'Aaron Stannard',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'aaron@stannardlabs.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['scaffold'],
    'scripts': [],
    'name': 'Scaffold'
}

setup(**config)
