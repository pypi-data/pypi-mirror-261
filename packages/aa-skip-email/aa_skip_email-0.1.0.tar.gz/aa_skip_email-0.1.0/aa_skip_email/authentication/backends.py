from allianceauth.authentication.backends import StateBackend

class SkipEmailBackend(StateBackend):
    def create_user(self, token):
        user = super(SkipEmailBackend, self).create_user(self, token)
        user.is_active = True
        user.save()
        return user
