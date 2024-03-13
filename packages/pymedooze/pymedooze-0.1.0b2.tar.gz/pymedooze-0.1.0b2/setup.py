# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pymedooze']

package_data = \
{'': ['*']}

install_requires = \
['semanticsdp>=0.1.0b3,<0.2.0']

setup_kwargs = {
    'name': 'pymedooze',
    'version': '0.1.0b2',
    'description': 'Python wrapper for medooze media-server.',
    'long_description': '',
    'author': 'RuslanUC',
    'author_email': 'dev_ruslan_uc@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
