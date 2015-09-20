from datetime import datetime
from .models import Usuario


class UsuarioBackend(object):

    def authenticate(self, username=None, password=None):

        try:
            user = Usuario.objects.get(usuario=username)

        except Usuario.DoesNotExist:
            return None
        if user.is_password_valid(password):
            user.last_login = datetime.now()
            user.save()
            return user

        return None

    def get_user(self, username_id):
        try:
            return Usuario.objects.get(id=username_id)
        except Usuario.DoesNotExist:
            return None
