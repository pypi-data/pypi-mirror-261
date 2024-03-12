from allianceauth.authentication.backends import StateBackend
from allianceauth.authentication.models import CharacterOwnership
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class SkipEmailBackend(StateBackend):
    def create_user(self, token):
        username = self.iterate_username(token.character_name)
        user = User.objects.create_user(username, is_active=True)  # skip asking the email
        user.set_unusable_password()
        user.save()
        token.user = user
        co = CharacterOwnership.objects.create_by_token(token)
        user.profile.main_character = co.character
        user.profile.save()
        logger.debug(f'Created new user {user}')
        return user
