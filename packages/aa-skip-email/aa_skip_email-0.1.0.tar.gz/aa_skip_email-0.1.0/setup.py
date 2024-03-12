# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aa_skip_email', 'aa_skip_email.authentication']

package_data = \
{'': ['*']}

install_requires = \
['allianceauth>=3.6']

setup_kwargs = {
    'name': 'aa-skip-email',
    'version': '0.1.0',
    'description': 'Allows you to skip entering your email after registering via EVE SSO',
    'long_description': '',
    'author': 'Boris Talovikov',
    'author_email': 'boris@talovikov.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/zima-corp/aa-skip-email',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
