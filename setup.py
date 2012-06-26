
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple project scaffolding for Python',
    'author': 'Aaron Stannard',
    'url': 'https://github.com/Aaronontheweb/scaffold-py',
    'download_url': 'https://github.com/downloads/Aaronontheweb/scaffold-py/Scaffold-0.1.1.tar.gz',
    'author_email': 'aaron@stannardlabs.com',
    'version': '0.1.1',
    'install_requires': ['nose'],
    'packages': ['scaffold'],
    'scripts': [],
    'name': 'Scaffold'
}

setup(**config)
