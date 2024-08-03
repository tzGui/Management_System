
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Users'

    def ready(self):
        # Remova a importação de signals se não for necessário
        pass