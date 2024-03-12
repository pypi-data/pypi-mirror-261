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
    'version': '0.1.1',
    'description': 'Allows you to skip entering your email after registering via EVE SSO',
    'long_description': "# AA Skip Email\n\nThis module allows you to skip the email asking when registering a user.\n\n## Install\n\nUse pip to install the module:\n\n```bash\npip install aa-skip-email\n```\n\nEdit the settings/local.py settings file.\n\nAdd aa_skip_email to the INSTALLED_APPS list.\n\n```python\nINSTALLED_APPS += [\n    ...\n    'aa_skip_email'\n    ...\n]\n```\n\nOverride the AUTHENTICATION_BACKENDS variable.\n\n```python\nAUTHENTICATION_BACKENDS = [\n    'aa_skip_email.authentication.backends.SkipEmailBackend',\n    'django.contrib.auth.backends.ModelBackend'\n]\n```\n\nRestart the allianceauth server.\n\n## See also\n\n- [allianceauth.allianceauth.backends](https://gitlab.com/allianceauth/allianceauth/-/blob/master/allianceauth/authentication/backends.py)\n- [github.com/allianceauth/allianceauth/issues/1060](https://github.com/allianceauth/allianceauth/issues/1060)\n",
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
