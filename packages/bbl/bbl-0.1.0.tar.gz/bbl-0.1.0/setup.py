# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bbl']

package_data = \
{'': ['*']}

install_requires = \
['pydantic==2.5.3', 'pylint>=2.17.2,<3.0.0']

setup_kwargs = {
    'name': 'bbl',
    'version': '0.1.0',
    'description': 'Base bricks library',
    'long_description': 'Base bricks library\n',
    'author': 'Mayorov Evgeny',
    'author_email': 'motormen@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4',
}


setup(**setup_kwargs)
