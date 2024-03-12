# AA Skip Email

This module allows you to skip the email asking when registering a user.

## Install

Use pip to install the module:

```bash
pip install aa-skip-email
```

Edit the settings/local.py settings file.

Add aa_skip_email to the INSTALLED_APPS list.

```python
INSTALLED_APPS += [
    ...
    'aa_skip_email'
    ...
]
```

Override the AUTHENTICATION_BACKENDS variable.

```python
AUTHENTICATION_BACKENDS = [
    'aa_skip_email.authentication.backends.SkipEmailBackend',
    'django.contrib.auth.backends.ModelBackend'
]
```

Restart the allianceauth server.

## See also

- [allianceauth.allianceauth.backends](https://gitlab.com/allianceauth/allianceauth/-/blob/master/allianceauth/authentication/backends.py)
- [github.com/allianceauth/allianceauth/issues/1060](https://github.com/allianceauth/allianceauth/issues/1060)
