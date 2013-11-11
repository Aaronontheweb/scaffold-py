
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple project scaffolding for Python',
    'author': 'Aaron Stannard',
    'url': 'https://github.com/Aaronontheweb/scaffold-py',
    'download_url': 'https://github.com/Aaronontheweb/scaffold-py/archive/v0.1.5.tar.gz',
    'author_email': 'aaron@stannardlabs.com',
    'version': '0.1.5',
    'install_requires': ['nose'],
    'packages': ['scaffold'],
    'scripts': [],
    'name': 'Scaffold',
    'entry_points': {
        'console_scripts': [
            'pyscaffold = scaffold.__main__:main',
        ],
        'virtualenvwrapper.project.template': [
            'base = scaffold.virtualenvwrapper:template',
        ],
    }


}

setup(**config)
