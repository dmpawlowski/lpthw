try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'My Project',
    'author': 'Don Pawlowski',
    'url': 'https://github.com/dmpawlowski',
    'download url': 'https://github.com/dmpawlowski',
    'author_email': 'don.m.pawlowski@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
